import socketserver
from Crypto.Util.number import *
import os
import signal
import string
from random import *
from s60709 import getflag
banner=r"""
 .d8888b.            .d8888b.                                   .d8888b.   .d8888b.   .d8888b.   d888   
d88P  Y88b          d88P  Y88b                                 d88P  Y88b d88P  Y88b d88P  Y88b d8888   
888    888          888    888                                        888 888    888        888   888   
888    888 888  888 888         8888b.  88888b.d88b.   .d88b.       .d88P 888    888      .d88P   888   
888    888 `Y8bd8P' 888  88888     "88b 888 "888 "88b d8P  Y8b  .od888P"  888    888  .od888P"    888   
888    888   X88K   888    888 .d888888 888  888  888 88888888 d88P"      888    888 d88P"        888   
Y88b  d88P .d8""8b. Y88b  d88P 888  888 888  888  888 Y8b.     888"       Y88b  d88P 888"         888   
 "Y8888P"  888  888  "Y8888P88 "Y888888 888  888  888  "Y8888  888888888   "Y8888P"  888888888  8888888 
                                                                                                        
                                                                                                        
                                                                                                        
8888888b.                       888 d8b          888               d888                                 
888   Y88b                      888 Y8P          888              d8888                                 
888    888                      888              888                888                                 
888   d88P 888d888 .d88b.   .d88888 888  .d8888b 888888             888                                 
8888888P"  888P"  d8P  Y8b d88" 888 888 d88P"    888                888                                 
888        888    88888888 888  888 888 888      888                888                                 
888        888    Y8b.     Y88b 888 888 Y88b.    Y88b.              888                                 
888        888     "Y8888   "Y88888 888  "Y8888P  "Y888           8888888                               
                                                                                                        
"""
menu=r"""
MENU:
1.Predict
2.Quit
"""
class LCG:
    def __init__(self):
        self.a=getPrime(90)
        self.b=getrandbits(90)
        self.p=getPrime(90)
        self.x=getrandbits(90)
    def nextstate(self):
        self.x=(self.a*self.x+self.b)%self.p
    def getstate(self):
        return self.x
class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 2048
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
    def recv(self, prompt='> '):
        self.printf(prompt, newline=False)
        return self._recvall()
    def handle(self):
    	signal.alarm(1200)
    	self.printf(banner)
    	money=19
    	flag=getflag()
    	lcg=LCG()
    	while True:
    	    if money<1:
    	        self.printf("Game Over: No Money")
    	        break
    	    if money<200:
    	        self.printf(menu)
    	    else:
    	        self.printf(menu+"\n"+flag)
    	    try:
    	        op=int(self.recv())
    	    except:
    	        self.printf("Error Input!")
    	        break
    	    if op==1:
    	        money-=1
    	        self.printf(f"You have ${money} left.")
    	        guessstate=int(self.recv("Guess the next number in decimal format>"))
    	        lcg.nextstate()
    	        if guessstate==lcg.getstate():
    	    	    money+=2
    	    	    self.printf(f"Great!,You Guessed it!")
    	        else:
    	    	    self.printf(f"Sorry,The Right Answer is {lcg.getstate()}")
    	    else:
    	    	break
    	self.printf("Quiting...")
class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass
if __name__ == "__main__":
    HOST, PORT = '0.0.0.0',60709
    while 1:
        try:
            server = ForkedServer((HOST, PORT), Task)
            server.allow_reuse_address = True
            print("Server at 127.0.0.1 port "+str(PORT))
            server.serve_forever()
        except:
            PORT=PORT+1 if PORT<64000 else 23333