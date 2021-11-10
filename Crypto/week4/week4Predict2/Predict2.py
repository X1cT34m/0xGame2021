import socketserver
from Crypto.Util.number import *
import os
import signal
import string
from random import *
from s60710 import getflag
banner=r"""
 .d8888b.            .d8888b.                                   .d8888b.   .d8888b.   .d8888b.   d888   
d88P  Y88b          d88P  Y88b                                 d88P  Y88b d88P  Y88b d88P  Y88b d8888   
888    888          888    888                                        888 888    888        888   888   
888    888 888  888 888         8888b.  88888b.d88b.   .d88b.       .d88P 888    888      .d88P   888   
888    888 `Y8bd8P' 888  88888     "88b 888 "888 "88b d8P  Y8b  .od888P"  888    888  .od888P"    888   
888    888   X88K   888    888 .d888888 888  888  888 88888888 d88P"      888    888 d88P"        888   
Y88b  d88P .d8""8b. Y88b  d88P 888  888 888  888  888 Y8b.     888"       Y88b  d88P 888"         888   
 "Y8888P"  888  888  "Y8888P88 "Y888888 888  888  888  "Y8888  888888888   "Y8888P"  888888888  8888888 
                                                                                                        
                                                                                                        
                                                                                                        
8888888b.                       888 d8b          888               .d8888b.                             
888   Y88b                      888 Y8P          888              d88P  Y88b                            
888    888                      888              888                     888                            
888   d88P 888d888 .d88b.   .d88888 888  .d8888b 888888                .d88P                            
8888888P"  888P"  d8P  Y8b d88" 888 888 d88P"    888               .od888P"                             
888        888    88888888 888  888 888 888      888              d88P"                                 
888        888    Y8b.     Y88b 888 888 Y88b.    Y88b.            888"                                  
888        888     "Y8888   "Y88888 888  "Y8888P  "Y888           888888888                                    
                                                                                                        
"""
menu=r"""
MENU:
1.Predict
2.Quit
"""
class LFSR:
    def __init__(self):
        self.state=[randint(0,1435756429) for _ in range(45)]
        self.mask=[1]+[randint(0,1435756429) for _ in range(44)]
        print(self.mask)
    def next(self):
        s=0
        for i in range(45):
            s=(s+self.state[i]*self.mask[i])%1435756429
        self.state=self.state[1:]+[s%1435756429]
        return s
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
    	money=97
    	lfsr=LFSR()
    	flag=getflag()
    	while True:
    	    if money<0:
    	        self.printf("Game Over: No Money")
    	        break
    	    if money<600:
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
    	        ans=lfsr.next()
    	        if guessstate==ans:
    	    	    money+=2
    	    	    self.printf(f"Great!,You Guessed it!")
    	        else:
    	    	    self.printf(f"Sorry,The Right Answer is {ans}")
    	    else:
    	    	break
    	self.printf("Quiting")
    	    
class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass
if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 60710
    while 1:
        try:
            server = ForkedServer((HOST, PORT), Task)
            server.allow_reuse_address = True
            print("Server at 0.0.0.0 port "+str(PORT))
            server.serve_forever()
        except:
            PORT=PORT+1 if PORT<64000 else 23333
