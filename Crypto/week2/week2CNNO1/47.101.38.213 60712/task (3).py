from Crypto.Util.number import *
from hashlib import sha256
import socketserver
import signal
import string
import random
import os

table = string.ascii_letters + string.digits
BANNER = br'''

 .d8888b.  888b    888      888b    888  .d88888b.       d888   
d88P  Y88b 8888b   888      8888b   888 d88P" "Y88b     d8888   
888    888 88888b  888      88888b  888 888     888       888   
888        888Y88b 888      888Y88b 888 888     888       888   
888        888 Y88b888      888 Y88b888 888     888       888   
888    888 888  Y88888      888  Y88888 888     888       888   
Y88b  d88P 888   Y8888      888   Y8888 Y88b. .d88P d8b   888   
 "Y8888P"  888    Y888      888    Y888  "Y88888P"  Y8P 8888888 
                                                                
'''


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

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def recv(self, prompt=b'[-] '):
        self.send(prompt, newline=False)
        return self._recvall()

    def proof_of_work(self):
        proof = (''.join([random.choice(table) for _ in range(12)])).encode()
        sha = sha256(proof).hexdigest().encode()
        self.send(b"[+] sha256(XXXX+" + proof[4:] + b") == " + sha)
        XXXX = self.recv(prompt=b'[+] Plz Tell Me XXXX :')
        if len(XXXX) != 4 or sha256(XXXX + proof[4:]).hexdigest().encode() != sha:
            return False
        return True

    def getnumber(self, m):
        e = 3
        p = getPrime(512)
        q = getPrime(512)
        c = pow(m, e, p * q)
        return p * q, c

    def getmessage(self):
        m = os.urandom(90)
        return bytes_to_long(m)

    def handle(self):
        signal.alarm(1000)
        self.send(BANNER)
        m = self.getmessage()
        if not self.proof_of_work():
            self.send(b'Oops,you are wrong. Bye~')
            return
        for i in range(3):
            n, c = self.getnumber(m)
            self.send(f'n{i}={n}'.encode())
            self.send(f'c{i}={c}'.encode())
        check = int(self.recv(b"Time's up. Now tell me why CN NO.1:"))
        if check == m:
            self.send(b'OHHHHH! You know CN NO.1 well! Here is what you want:')
            f = open('flag.txt', 'rb')
            flag = f.read()
            f.close()
            self.send(flag)
        self.request.close()


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 60712
    print("HOST:POST " + HOST + ":" + str(PORT))
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
