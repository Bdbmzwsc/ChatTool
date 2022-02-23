from base64 import decode
import socket
from threading import Thread
from tkinter import *

from sqlalchemy import false, true

client={}
addresses={}
clientindex={}
index=-1

connect_people=10
host_ip="127.0.0.1"
host_port=7130

def addresses_find_user(nickname):
    for con in addresses:
        if addresses[con] == nickname + "\n\n":
            return con


def find_user(nickname):
    for i1 in range(0,len(clientindex)):
        if clientindex[i1]==nickname + "\n\n":
            return i1

def send_msg(nickname,msg):
    for con in addresses:
        if addresses[con] == f"{nickname}\n\n":
            con.send(bytes(msg,"utf8"))

def radio(msg,name=""):
    try:
        for con in addresses:
            con.send(bytes(name,"utf8") + msg)
    except:
        return 0

#一个客户端一个线程
def get_client_msg(con,addr):
    name=con.recv(1024).decode("utf8")
    i=index
    clientindex[index]=name
    client[con]=name
    radio(bytes(f"Welcome {name} to here!","utf8"))
    ischange=false
    ismsg=true

    #获取此线程对应的用户发来的消息
    try:
        while True:
            msg=con.recv(1024)
            if ischange == true:
                ischange=false
                print(f"{name}change_name to ")
                name1=name
                name=msg.decode("utf8")
                client[con]=name
                clientindex[i]=name
                #radio(bytes(f"{name1}更改了名字为{name}"))
               # ismsg=false
            if msg.decode("utf8") == "change_name\n\n":
                ischange=true
                print(f"{name}change_name")
               # ismsg=false
            if msg.decode("utf8").split()[0] == "9213dc7c9c8606fe":
                common=msg.decode("utf8").split()
                print(common[1])

                try: 
                    print("e")
                    if common[1] == "change_usernickname":
                        
                        print("d")
                        for i1 in range(0,len(clientindex)):
                            print("f")
                            if clientindex[i1]==common[2] + "\n\n":
                                print(f"{clientindex[i]}改变了{clientindex[i1]}的名字为{common[3]}")
                                clientindex[i1]=common[3] + "\n\n"
                                ismsg=false
                    if common[1] == "quit":
                        print(f"{clientindex[i]}改变了{clientindex[i1]}的名字为{common[3]}")
                        i1=find_user(common[2])
                        #clientindex[i1]=common[3] + "\n\n"
                        send_msg(common[2],f"您被{clientindex[i]}踢出服务器")
                        del client[addresses_find_user(common[2])]
                        del addresses[addresses_find_user(common[2])]
                        con1=addresses_find_user(common[2])
                        con1.close()
                        radio(bytes(f"{common[2]}已被{clientindex[i]}踢出服务器"))
                        del clientindex[find_user(common[2])]
                        ismsg=false
                except:
                    radio(msg,clientindex[i] + ":")
                    ismsg=false
                    
            print(msg.decode("utf8"))
            print(msg)
            if ismsg==true: 
                radio(msg,clientindex[i] + ":")
            else:
                ismsg=true
    #判断为此线程对应的用户离开了
    except:
        del addresses[con]
        del client[con]
        radio(bytes(f"在尝试给{clientindex[i]}发送信息时报错，被系统判定为已退出服务器","utf8"),"系统:")
        del clientindex[i]
 



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host_ip,host_port))

if __name__ == "__main__":
    s.listen(connect_people)
    print("Listen")
    while True:
        conn,address=s.accept()
        print(f"{address}建立连接")
        conn.send("Serve message:Welcome to here!The serve will think the first message is your name".encode('utf8'))
        addresses[conn]=address
        index=index+1
        Thread(target=get_client_msg,args=(conn,address)).start()