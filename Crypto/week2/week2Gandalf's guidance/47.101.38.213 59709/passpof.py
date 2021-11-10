from hashlib import sha256
import socketserver
import signal
import string
import random
table = string.ascii_letters + string.digits


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
        self.send(b'''I'm Flame of Udun, I can tell you this: ''')
        self.send(b"sha256(XXXX+" + proof[4:] + b") == " + sha)
        XXXX = self.recv(prompt=b'Plz Tell Me XXXX :')
        if len(XXXX) != 4 or sha256(XXXX + proof[4:]).hexdigest().encode() != sha:
            return False
        return True

    def handle(self):
        signal.alarm(50)
        self.send(b'I am a servant of the Secret Fire, wielder of the flame of Anor.')
        self.send(b'Go back to the Shadow.')
        self.send(b'The dark fire will not avail you, Flame of Udun!')
        if not self.proof_of_work():
            self.send(b'You shall not PASS!!!')
            return
        self.send(b'How dare you are!')
        self.send(b'But here is a reward for the brave.')
        f = open('flag.txt', 'rb')
        flag = f.read()
        f.close()
        self.send(flag)


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 59709
    print("HOST:POST " + HOST + ":" + str(PORT))
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
