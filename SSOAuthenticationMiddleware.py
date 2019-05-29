"""
ctyun SSO Authentication Middleware

"""
import requests
import xmltodict
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin
from django.contrib.sessions.models import Session

SSO_LOGIN_URL = "xxx"
SSO_VALID_URL = "xxxx"


class SSOAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):

        callback_url = request.build_absolute_uri().split('?')[0]
        ticket = request.GET.get('ticket', None)

        session_key = request.session.session_key

        if ticket:
            # valid ticket
            params = {
                "service": callback_url,
                "ticket": ticket
            }
            req = requests.request('GET', SSO_VALID_URL, params=params)
            resp = xmltodict.parse(req.text, encoding='utf-8')
            if not resp['cas:serviceResponse'].get('cas:authenticationFailure', None):
                cas_userId = resp['cas:serviceResponse']['cas:authenticationSuccess']['cas:attributes']['userId']
                cas_domainId = resp['cas:serviceResponse']['cas:authenticationSuccess']['cas:attributes']['domainId']
                cas_user = resp['cas:serviceResponse']['cas:authenticationSuccess']['cas:user']

                print(cas_userId, cas_domainId, cas_user)
                user = User(username=cas_user, is_superuser=True, is_active=True)
                request.session['ctyun_key'] = cas_user
                request.session.set_expiry(60 * 30) # write setting.py
                request.user = user
            else:
                # login html
                return self.redirect_login(callback_url)
        elif session_key:
            try:
                session = Session.objects.get(session_key=session_key)
                user = session.get_decoded().get('ctyun_key')
                request.user = User(username=user, is_superuser=True, is_active=True)
            except Session.DoesNotExist, e:
                return self.redirect_login(callback_url)
        else:
            return self.redirect_login(callback_url)

    def redirect_login(self, callback_url):
        return redirect('%s?service=%s' % (SSO_LOGIN_URL, callback_url))
