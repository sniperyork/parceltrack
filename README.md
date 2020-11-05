# 使用须知

<<<<<<< HEAD
该软件通过 flask 建立起一个 server 来接收 get 数据请求相应。
请在使用前，在服务器安装最新 Python 版本，以及以下几个 python modules：

- flask (安装 command： pip install Flask)
- requests (安装 command： pip install requests)
- markupsafe (安装 command： pip install MarkupSafe)
- selenium (安装 command： pip install selenium)
- webdrivermanager (安装 command： pip install webdrivermanager)

安装完后，需要在 webapp.py 的目录下面打开 terminal 并且执行下列命令：

=======
该软件通过flask建立起一个server来接收get数据请求并响应。
请在使用前，在服务器安装最新Python版本，以及以下几个python modules：
- flask (安装command： pip install Flask)
- requests (安装command： pip install requests)
- markupsafe (安装command： pip install MarkupSafe)
- selenium (安装command： pip install selenium)
- webdrivermanager (安装command： pip install webdrivermanager)

安装完后，需要在webapp.py的目录下面打开terminal并且执行下列命令：
>>>>>>> a36c3a5cdda18e0c87b7ac80cc9cd5ea341a27e2
- FLASK_APP=Webapp.py (此处注意文件名大小写)
- python -m flask run (注：如果 Python 版本为 python 3,命令则需要改为‘python3 -m flask run')

或者

- export FLASK_APP=Webapp.py
- flask run

server 运行起来之后，terminal 将会显示以下信息：

Serving Flask app "Webapp.py"
<<<<<<< HEAD

- Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
- Debug mode: off
- Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

这个时候可以尝试访问测试链接来检查是否 json 数据显示正常

- 打开浏览器并输入 'http://127.0.0.1:5000/search/SF1042653880061'
  一切正常则会看到物流 json 数据
=======
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

这个时候可以尝试访问测试链接来检查是否json数据显示正常
- 打开浏览器并输入 'http://127.0.0.1:5000/search/FPS2219006CA'
一切正常则会看到物流json数据

**当server运行起来的时候，后台可以通过以下的path来获取json数据
localhost:5000/search/Consumer_number
>>>>>>> a36c3a5cdda18e0c87b7ac80cc9cd5ea341a27e2
