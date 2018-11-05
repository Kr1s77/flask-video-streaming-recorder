# 树莓派+opencv+flask家庭监控系
## 树莓派操作
- 首先树莓派上需要安装python3
  - $ sudo  apt-get  update
  - $ sudo  apt-get  upgrade
- 安装python依赖环境
  - $ sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev
- 下载python3.6版本源码并解压
  - $ wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
  - $ tar zxvf Python-3.6.1.tgz
- 编译安装
  - $ cd Python-3.6.1
  - $ sudo ./configure
  - $ sudo make
  - $ sudo make install
- 检查安装
  - $ ls -al /usr/local/bin/python*
  
##python3自带pip3
###接下来安装模块
- 安装flask
  - $ pip3 install flask
- 安装opencv
  - $ pip3 inshall opencv_python
###然后
- 下载所有文件运行即可
  - $ python3 serve.py
###写在最后
- 以后还会更新更多项目啊！
- 加油吧！！！！！
