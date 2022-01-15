配置新网站
=========

## 需要安装的包

* Nginx
* Python 3
* Git
* pip
* virtualenv


已ubuntu为例，执行下面的命令安装

	sudo apt-get install nginx git python3 python3-pip(可忽略，安装python中自带)
	sudo pip3 install virtualenv

## 配置Nginx虚拟主机

* 参考nginx.template.conf
* 把SITENAME替换成所需的域名，例如www.may19.cn

## 自启动任务

* 参考gunicorn-www.may19.cn
* 把SITENAME替换成所需的域名

## 文件夹结构

家目录为/home/elspeth

/home/elspeth
└── www.may19.cn
    ├── database
    ├── source
    ├── static
    └── virtualenv

