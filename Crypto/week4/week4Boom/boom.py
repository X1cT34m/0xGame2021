from Crypto.Util.number import *

f = open('flag.txt', 'r')
flag = f.read()
f.close()
assert flag[:7] == "0xGame{"


class LCG:
    def __init__(self):
        self.a = getRandomNBitInteger(32)
        self.b = getRandomNBitInteger(32)
        self.m = getPrime(32)
        self.seed = getRandomNBitInteger(32)

    def next(self):
        self.seed = (self.a * self.seed + self.b) % self.m
        return self.seed >> 16

    def output(self):
        print("a = {}\nb = {}\nm = {}".format(self.a, self.b, self.m))
        print("state1 = {}".format(self.next()))
        print("state2 = {}".format(self.next()))


lcg = LCG()
lcg.output()
c = b''.join([long_to_bytes(ord(flag[i]) ^ (lcg.next() % 10))
              for i in range(len(flag))])
print(bytes_to_long(c))
# a = 2223895827
# b = 2180283007
# m = 3462137369
# state1 = 14216
# state2 = 2162
# 405876446443434716158061994680916497969770152218293569911902716429842633796269271924
