> centos7简易安装python3

```
python install_python.py
输入需要安装的Python版本，等待自动安装，就可以了
```
> SSO Authentication
```bash
实现SSO单点登录，使用session的方式， （不同域名之间暂未验证）

使用方法：
  在settings.py中配置session，使用数据库方式存储session，
  
  在settings.py的Middleware中添加： utils.SSOAuthenticationMiddleware.SSOAuthenticationMiddleware即可

```
> sdbm-hash Python实现
```bash
  验证HAproxy的分发规则： 对agent的hostid取sdbm-hash，然后求mod(2)
```

> django-session自定义长度
```bash
  在settings.py中添加：  SESSION_ENGINE = '自定义session认证后端的位置(精确到文件即可)'
  数据库中添加新的Session表, 执行： python manage.py makemigrations ; python manage.py migrate 
  
```
