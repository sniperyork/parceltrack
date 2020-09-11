# 使用须知

该软件通过flask建立起一个server来接收get数据请求相应。
请在使用前，在服务器安装最新Python版本，以及以下几个python modules：
- flask (安装command： pip install Flask)
- requests (安装command： pip install requests)
- markupsafe (安装command： pip install MarkupSafe)
- selenium (安装command： pip install selenium)
- webdrivermanager (安装command： pip install webdrivermanager)

安装完后，需要在webapp.py的目录下面打开terminal并且执行下列命令：
- FLASK_APP=webapp.py
- python -m flask run (注：如果Python版本为python 3,命令则需要改为‘python3 -m flask run')

server运行起来之后，terminal将会显示以下信息：

Serving Flask app "Webapp.py"
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

这个时候可以尝试访问测试链接来检查是否json数据显示正常
- 打开浏览器并输入 'http://127.0.0.1:5000/search/FPS2219006CA'
一切正常则会看到物流json数据
