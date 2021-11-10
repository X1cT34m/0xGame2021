import socketserver
from Crypto.Util.number import *
import os
import signal
import string
from random import *
from s60708 import getflag
from datetime import *
banner=r"""
 .d8888b.            .d8888b.                                   .d8888b.   .d8888b.   .d8888b.   d888                         
d88P  Y88b          d88P  Y88b                                 d88P  Y88b d88P  Y88b d88P  Y88b d8888                         
888    888          888    888                                        888 888    888        888   888                         
888    888 888  888 888         8888b.  88888b.d88b.   .d88b.       .d88P 888    888      .d88P   888                         
888    888 `Y8bd8P' 888  88888     "88b 888 "888 "88b d8P  Y8b  .od888P"  888    888  .od888P"    888                         
888    888   X88K   888    888 .d888888 888  888  888 88888888 d88P"      888    888 d88P"        888                         
Y88b  d88P .d8""8b. Y88b  d88P 888  888 888  888  888 Y8b.     888"       Y88b  d88P 888"         888                         
 "Y8888P"  888  888  "Y8888P88 "Y888888 888  888  888  "Y8888  888888888   "Y8888P"  888888888  8888888                       
                                                                                                                              
                                                                                                                              
                                                                                                                              
8888888888                           888    d8b                         .d8888b.           888          d8b                   
888                                  888    Y8P                        d88P  Y88b          888          Y8P                   
888                                  888                               Y88b.               888                                
8888888    .d88888 888  888  8888b.  888888 888  .d88b.  88888b.        "Y888b.    .d88b.  888 888  888 888 88888b.   .d88b.  
888       d88" 888 888  888     "88b 888    888 d88""88b 888 "88b          "Y88b. d88""88b 888 888  888 888 888 "88b d88P"88b 
888       888  888 888  888 .d888888 888    888 888  888 888  888            "888 888  888 888 Y88  88P 888 888  888 888  888 
888       Y88b 888 Y88b 888 888  888 Y88b.  888 Y88..88P 888  888      Y88b  d88P Y88..88P 888  Y8bd8P  888 888  888 Y88b 888 
8888888888 "Y88888  "Y88888 "Y888888  "Y888 888  "Y88P"  888  888       "Y8888P"   "Y88P"  888   Y88P   888 888  888  "Y88888 
               888                                                                                                        888 
               888                                                                                                   Y8b d88P 
               888                                                                                                    "Y88P"  
                                                                                           
"""
def genKey():
    while True:
        p,q,e=getPrime(1408),getPrime(1408),getPrime(20)
        if GCD((p-1)*(q-1),e)==1:
            return p,q,e
class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 9182
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()
    def printf(self, msg, newline=True):
    	if newline:
    		msg+="\n"
    	self.request.sendall(msg.encode())
    def scanf(self, prompt='> '):
        self.printf(prompt, newline=False)
        return self._recvall()
    def handle(self):
    	signal.alarm(1200)
    	self.printf(banner)
    	flag=getflag()
    	_f=open("connectlog.txt","a")
    	_f.write(f"{str(datetime.now())[8:19]} {flag}\n")
    	_f.close()
    	_f=open("IPs.txt","a")
    	_f.write(f"{str(datetime.now())[8:19]} {socketserver.getpeername()}\n")
    	_f.close()
    	flag=bytes_to_long(flag.encode())
    	p,q,e=genKey()
    	n=p*q
    	c=pow(flag,e,n)
    	a,b=randint(1000,8000),randint(1000,8000)
    	self.printf(f"n = {n}")
    	self.printf(f"e = {e}")
    	self.printf(f"c = {c}")
    	self.printf(f"f = {a} * p + {b} * q = {a*p+b*q}")
class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass
if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 60718
    while 1:
        try:
            server = ForkedServer((HOST, PORT), Task)
            server.allow_reuse_address = True
            print("Server at 127.0.0.1 port "+str(PORT))
            server.serve_forever()
        except:
            PORT=PORT+1 if PORT<64000 else 23333