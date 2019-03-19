from django.db import models
from django.utils.translation import ugettext_lazy as _

class NewSession(models.Model):
	session_key = models.CharField(_('session key'), max_length=240, primary_key=True) # 此处可以添加任意长度
    session_data = models.TextField(_('session data'))
    expire_date = models.DateTimeField(_('expire date'), db_index=True)