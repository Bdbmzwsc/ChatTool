# ChatTool
一个使用python编写的基于tcp协议的聊天工具

# 依赖
python3.8或以上版本
# 辅助工具
服务端可以使用natapp内网穿透等工具实现外网聊天
# 使用教程
首先clone此仓库
```
	git clone https://github.com/Bdbmzwsc/ChatTool.git
	cd ChatTool
```
你将会在文件夹中看到serve.py和reques.py,其中，serve.py是服务端，reques.py则是客户端

启动服务端
```
python3 serve.py
```
此操作将会在127.0.0.1的ip地址启动一个7130端口
接下来启动客户端

```
python3 reques.py
```
启动后需要输入服务端ip和port,这里将服务端和客户端放在同一台设备上，故ip输入```127.0.0.1```,port输入```7130```
输入完后，如果连接成功，则会弹出一个界面，最下面的grid是输入文本信息的，最上面的grid是显示服务器发送的信息的


**注意！**
服务端将默认客户端发送的第一条信息为客户端的nickname


在没有出现bug或不是特殊情况下，任意一个客户端没连接服务端服务端都会广播
~~小彩蛋：首先发送一条信息```change_name```,在发送一条信息，然后nickname就会变成第二条信息~~
