from Crypto.Util.number import *
from pwn import *
sh = remote("47.101.38.213", 60713)
sh.recvuntil(b"> ")
sh.sendline(b"1")
n, e, c = [sh.recvline(keepends=False) for _ in range(3)]
n, e, c = int(n[2:]), int(e[2:]), int(c[2:])
print(n)
print(e)
print(c)
L, R, Clk = 0, n, 1
judge = n % 5
Table = [[0, 0, 0, 0, 0], [0, 4, 3, 2, 1], [
    0, 3, 1, 4, 2], [0, 2, 4, 1, 3], [0, 1, 2, 3, 4]]
j0, j1, j2, j3, j4 = Table[judge]
print(f"judge={judge}")
while L < R:
    # for i in range(1):
    D = (R-L)//5
    if Clk % 35 == 0:
        print(Clk)
        print(R-L)
    P20, P40, P60, P80 = L+D, L+2*D, L+3*D, L+4*D
    a = c*(pow(5, e*Clk, n)) % n
    sh.recvuntil(b">")
    sh.sendline(b"3")
    sh.recvuntil(b">")
    sh.sendline(str(a).encode())
    Rem = sh.recvline(keepends=False)[-1]-48
    if Rem == j0:
        L, R = L, P20
    elif Rem == j1:
        L, R = P20, P40
    elif Rem == j2:
        L, R = P40, P60
    elif Rem == j3:
        L, R = P60, P80
    elif Rem == j4:
        L, R = P80, R
    else:
        print(b"Error")
        break
    Clk += 1
L = long_to_bytes(L)
L = L.split(b"          ")
print(L[1])
sh.close()
