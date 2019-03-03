# 树莓派+opencv+flask家庭监控系统

### 首先树莓派上需要安装python3
```
    	$ sudo  apt-get  update
    	$ sudo  apt-get  upgrade
```	
    	
- 安装python依赖环境
- install python Dependent environment
```
    $ sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev
 ```
    
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


		$ ls -al /usr/local/bin/python*
  
### python3自带pip3

### 接下来安装模块

- 安装flask
- install flask


    	$ pip3 install flask==0.10.1
    	
- 安装opencv
- install opencv


     	$ pip3 inshall opencv_python
  
### 然后
- Then

- 下载所有文件运行即可
- run main.py


    	$ python3 main.py
    	
 - 2019.2.21更新
 - 增加了登录，很简单的一个登录接口，并不需要数据库
 - Increased login, a simple login interface, does not need a database
 
 - 测试账户
 - Test account
 ```
     username: admin
     password: admin
 
 ```
  
### 写在最后
<<<<<<< HEAD
- 以后还会更新更多项目啊！
- 加油吧！！！！！
- Have a good time!
=======
- 大哥们给个star吧！
- Have a good time!
>>>>>>> f9bc1964f84eac7fc04966baca746053c06dee9e
