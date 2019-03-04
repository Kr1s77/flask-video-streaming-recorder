<h2 align="center"><code>树莓派 flask+opencv监控系统</code></h2>

<br>

<p align="center">
    <img src="https://github.com/CriseLYJ/flask-video-streaming-recorder/blob/master/img/main.jpg?raw=true" 
        alt="Master">
</p>

<br>

<p align="center">"<i>Did you know all your doors were locked?</i>" - Riddick (The Chronicles of Riddick)</p>

<br>

<p align="center">
  <a href="https://github.com/CriseLYJ/flask-video-streaming-recorder/tree/master">
    <img src="https://img.shields.io/badge/Branch-master-green.svg?longCache=true"
        alt="Branch">
  </a>
  <a href="https://github.com/CriseLYJ/flask-video-streaming-recorder/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?longCache=true"
        alt="Pull Requests">
  </a>
  <a href="http://www.gnu.org/licenses/">
    <img src="https://img.shields.io/badge/License-GNU-blue.svg?longCache=true"
        alt="License">
  </a>
</p>

<div align="center">
  <sub>Created by
  <a href="https://criselyj.github.io/">CriseLYJ</a>
</div>

<br>

****


### 🐍First you should install ``Python3.x`` on your Raspberry Pi
```
    	$ sudo  apt-get  update
    	$ sudo  apt-get  upgrade
```	
    	
- 安装python``依赖环境``
- install python ``Dependent environment``

>    $ sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev

    
- 下载python3.6版本源码并解压
- Download the python version 3.6 source code and decompress it

```
    	$ wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
    	$ tar zxvf Python-3.6.1.tgz
 ```   	
- 编译安装
- Compilation and installation
```
	    $ cd Python-3.6.1
	    $ sudo ./configure
	    $ sudo make
	    $ sudo make install
```	    
- 检查安装
- Inspection and installation

> $ ls -al /usr/local/bin/python*
  
### python3自带pip3

### 接下来安装模块

- 安装flask
- install flask


> $ pip3 install flask==0.10.1
    	
- 安装opencv
- install opencv
> $ pip3 install opencv_python
  
### 最后一步
- Then

- 下载所有文件运行即可
- run server.py

> $ python3 server.py
    	
 - 2019.2.21更新
 - 增加了登录，很简单的一个登录接口，并不需要数据库
 - Increased login, a simple login interface, does not need a database
 
 - 测试账户
 - Test account
 ```
     Username: admin
     Password: admin
 
 ```
 - 2019.3.4更新
 - 添加多线程和录制下载等功能
 - 支持多设置访问，退出登录回复正常
 
 - 添加了优美的登录界面
 ![Alt text](./img/login.png)
 
 - 优化前端

 ![Alt text](./img/index.jpg)
 
 - 添加视频录制和下载功能
  
### 写在最后
- Fiting !!!!!

- If you like this project ! Please give me a star! cool man!

- Have a good time!

 ![Alt text](./img/hha.jpeg)

