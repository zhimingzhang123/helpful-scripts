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
