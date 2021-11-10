#Sagemath
from Crypto.Util.number import *
from sage.all import *
from pwn import *
sh = remote("47.101.38.213", 60710)
states = []
for i in range(90):
    sh.recvuntil(b">")
    sh.sendline(b"1")
    sh.recvuntil(b">")
    sh.sendline(b"1500000000")
    sh.recvuntil(b"is")
    states.append(int(sh.recvline(keepends=False)))
M = []
for i in range(45):
    M.append(states[i:i+45])
v = states[45:90]
M = matrix(Zmod(1435756429), M)
v = vector(Zmod(1435756429), v)
mask = v*(M**(-1))
v, mask = list(v), list(mask)
print(mask)
for i in range(601):
    s = 0
    for j in range(45):
        s += v[j]*mask[j]
    s %= 1435756429
    print(i, s)
    v = v[1:]+[s]
    sh.recvuntil(b">")
    sh.sendline(b"1")
    sh.recvuntil(b">")
    sh.sendline(str(s).encode())
sh.interactive()
