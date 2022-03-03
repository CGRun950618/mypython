# encoding= utf-8
import socket
import threading
import time


#服务端
def dealClient(sock,addr):
    #第四步：接收传来的数据，并发送给对方数据
    print('Accept new connection from %s:%s...'%addr)
    sock.send(b'Hello,I am server!')
    while True:
        date=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        print('-->%s!'%data.decode('utf-8'))
        sock.send(('loop_Msg:%s!'%date.decode('utf-8')).encode('utf-8'))
    #第五步 ，关闭Socket
    sock.close()
    print('Connection from %s:%s closed.'%addr)

if __name__=='__main__':
    #第一步：创建一个基于IPV4和tcp协议的socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',9999))
    #第二部：监听连接
    s.listen(5)
    print('Wating for connection...')
    while True:
        #第三步：接收一个新连接：
        socket,addr=s.accept()
        #创造新线程来处理TCP连接：
        t=threading.Thread(target=dealClient,args=(sock,addr))
        t.start()

#客户端
    #初始化Socket
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #连接目标的ip和端口
    s.connect(('127.0.0.1',9999))
    #接收消息
    print('——》'+s.recv(1024).decode('utf-8'))
    #发送消息
    s.send(b'hello,I am a client')
    print('——》'+s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    #关闭Socket
    s.close()