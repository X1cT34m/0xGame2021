import socketserver
from Crypto.Util.number import *
import os
import signal
import string
from random import *
from secret import getflag
banner=r"""
 .d8888b.            .d8888b.                                   .d8888b.   .d8888b.   .d8888b.   d888   
d88P  Y88b          d88P  Y88b                                 d88P  Y88b d88P  Y88b d88P  Y88b d8888   
888    888          888    888                                        888 888    888        888   888   
888    888 888  888 888         8888b.  88888b.d88b.   .d88b.       .d88P 888    888      .d88P   888   
888    888 `Y8bd8P' 888  88888     "88b 888 "888 "88b d8P  Y8b  .od888P"  888    888  .od888P"    888   
888    888   X88K   888    888 .d888888 888  888  888 88888888 d88P"      888    888 d88P"        888   
Y88b  d88P .d8""8b. Y88b  d88P 888  888 888  888  888 Y8b.     888"       Y88b  d88P 888"         888   
 "Y8888P"  888  888  "Y8888P88 "Y888888 888  888  888  "Y8888  888888888   "Y8888P"  888888888  8888888 
                                                                                                        
                                                                                                        
                                                                                                        
 .d88888b.                           888          888888b.                             888888888        
d88P" "Y88b                          888          888  "88b                            888              
888     888                          888          888  .88P                            888              
888     888 888d888 8888b.   .d8888b 888  .d88b.  8888888K.   8888b.  .d8888b   .d88b. 8888888b.        
888     888 888P"      "88b d88P"    888 d8P  Y8b 888  "Y88b     "88b 88K      d8P  Y8b     "Y88b       
888     888 888    .d888888 888      888 88888888 888    888 .d888888 "Y8888b. 88888888       888       
Y88b. .d88P 888    888  888 Y88b.    888 Y8b.     888   d88P 888  888      X88 Y8b.    Y88b  d88P       
 "Y88888P"  888    "Y888888  "Y8888P 888  "Y8888  8888888P"  "Y888888  88888P'  "Y8888  "Y8888P"        
                                                                                           
"""
menu=r"""
MENU:
1.GetKey
2.Encrypt
3.Decrypt
4.Quit
"""
def GenerateRSAKey():
    n,phi=1,1
    for i in range(4):
        p=getPrime(randint(1000,1200))
        n*=p
        phi*=(p-1)
    e=getPrime(randint(20,24))
    d=inverse(e,phi)
    return n,e,d
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
    	flag=getflag()
    	self.printf(banner)
    	n,e,d=GenerateRSAKey()
    	flag=bytes_to_long(os.urandom(390)+b"          "+flag.encode()+b"          "+os.urandom(30))
    	for ___ in range(1607087):
    	    self.printf(menu)
    	    try:
    	        op=int(self.scanf())
    	        if op==1:
    	            self.printf(f"n={n}")
    	            self.printf(f"e={e}")
    	            self.printf(f"c={pow(flag,e,n)}")
    	        elif op==2:
    	            m=int(self.scanf("Enter your plaintext in decimal format >"))
    	            c=pow(m,e,n)
    	            self.printf(f"Your Cipher mod 5 is: {c%5}")
    	        elif op==3:
    	            c=int(self.scanf("Enter your ciphertext in decimal format >"))
    	            m=pow(c,d,n)
    	            self.printf(f"Your PlainText mod 5 is: {m%5}")
    	        else:
    	            break
    	    except:
    	        self.printf("Wrong Input")
    	        break
    	self.printf("Quitting...")
    	    
class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass
if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 60713
    while 1:
        try:
            server = ForkedServer((HOST, PORT), Task)
            server.allow_reuse_address = True
            print("Server at 0.0.0.0 port "+str(PORT))
            server.serve_forever()
        except:
            PORT=PORT+1 if PORT<64000 else 23333
