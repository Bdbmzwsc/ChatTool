#from unittest import result
#from email import message_from_binary_file
#from logging import root
import socket;from threading import Thread
#from turtle import width
#from numpy import byte
#import requests
from tkinter import *

def on_press_enter(event):
    print("Enter")
    msg=text_input.get("0.0",END)
    #发送信息
    s.send(bytes(msg,"utf8"))
    #text_msg.insert(END,msg)
    text_input.delete("0.0",END)
def get_msg():
    while True:
        try:
            recive_msg=s.recv(1024).decode("utf8")
            text_msg.insert(END,recive_msg + "\n")
            text_msg.see(END)
        except:
            break


host_ip=input("Please host ip:")
host_port=eval(input("Please host port:"))
root=Tk()
root.title('聊天群')
#监听回车键
root.bind("<Return>",on_press_enter)

#创建聊天面板
frame_msg=Frame(
    root,
    width=400,
    height=600
)

#输入面板
frame_input=Frame(
    root,
    width=400,
    height=100
)

frame_msg.grid_propagate(0)
frame_input.grid_propagate(0)

text_msg=Text(frame_msg)
text_input=Text(frame_input)

#布局
frame_msg.grid(
    row=0,
    padx=3,
    pady=6
)

frame_input.grid(
    row=1,
    padx=3,
    pady=6
)

text_msg.grid()
text_input.grid()

#连接服务器
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host_ip,host_port))
except:
    print("connect fails")

#接受服务端发送的信息
recive_thread=Thread(target=get_msg)
recive_thread.start()

root.mainloop()