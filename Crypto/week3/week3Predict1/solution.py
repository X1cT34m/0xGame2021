from Crypto.Util.number import *
from pwn import *
sh=remote("47.101.38.213",60709)
u,detla=[],[]
for i in range(16):
    sh.recvuntil(b">")
    sh.sendline(b"1")
    sh.recvuntil(b">")
    sh.sendline(b"1")
    numb=sh.recvline(keepends=False)
    numb=numb.split(b"is")[1]
    u.append(int(numb))
for i in range(12):
    detla.append(abs((u[i+2]-u[i+1])*(u[i+2]-u[i+1])-(u[i+3]-u[i+2])*(u[i+1]-u[i])))
p=detla[0]
for i in detla:
    p=GCD(p,i)
print(p)
assert isPrime(p)
a=(u[3]-u[2])*inverse(u[2]-u[1],p)%p
b=(u[1]-a*u[0])%p
print(a,b,p)
x=u[-1]
for i in range(205):
    if i%15==0:
        print(i)
    x=(a*x+b)%p
    sh.recvuntil(b">")
    sh.sendline(b"1")
    sh.recvuntil(b">")
    sh.sendline(str(x).encode())
sh.recvuntil(b"0xGame{")
flag=sh.recvline(keepends=False)
print("0xGame{"+flag.decode())
sh.close()
