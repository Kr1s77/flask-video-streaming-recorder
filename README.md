<h2 align="center"><code>Raspberry Pi flask+opencv Surveillance System</code></h2>

<br>

<p align="center">
    <img src="https://github.com/Kr1s77/Python-crawler-tutorial-starts-from-zero/blob/master/images/%E6%80%81%E5%BA%A6CoderClub.jpeg?raw=true" 
        alt="Master">
</p>

<br>

<p align="center">"<i>推荐一波我的公众号，想要学习爬虫，大数据的可以关注一下，绝对满满的干货哦！</i>" - 一个诈尸的人，哈哈</p>

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

# Installing
### 🐍First you should install ``Python3.x`` on your Raspberry Pi

>   $ sudo  apt-get  update
>   $ sudo  apt-get  upgrade
	
    	
- Install python``dependent environment``
- install python ``Dependent environment``

>    $ sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev

    
- Download the python3.6 version source and extract it
- Download the python version 3.6 source code and decompress it

>    	$ wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
>    	$ tar zxvf Python-3.6.1.tgz
  	
- Compilation and installation

>	    $ cd Python-3.6.1
>	    $ sudo ./configure
>	    $ sudo make
>	    $ sudo make install
	    
- Check installation

> 	$ ls -al /usr/local/bin/python*


### Next install the module

- Install flask

> 	$ pip3 install flask==0.10.1
    	
- Install opencv
- install opencv

> $ pip3 install opencv_python
  
# Running the tests

- Download all files to run
- run main.py

> 	$ python3 main.py -p 0.0.0.0
> 当然你也可以使用Gunicorn来当做你的多线程服务器
    	
 - 2019.2.21 update

 - Increased login, a simple login interface, does not need a database
 
 - Test account
 ```
     Username:  admin
     Password:  admin
 ```
 - 2019.3.4 update
 - Add multi-threading and recording downloads
 - Support multi-device access, logout login is normal

 - 2019.3.14 update
 - 现在的目录结构是这个样子

 ![](./img/tree.png)
 
- 抽取了代码，进行了优化，就是这样目录看起来会很多
 
 - Added a beautiful login interface
 ![Alt text](./img/login.png)
 
 - Optimization homepage

 ![Alt text](./img/index.jpg)
 
 - Add video recording and download capabilities
 - Realized the ``high performance``, using the yield generator, and multi-threading, silky smooth!
 
# Author
- Crise LYJ
  
# Acknowledgments
- Thanks for all!

- Have a good time!

 ![Alt text](./img/hha.jpeg)
