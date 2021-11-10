from Crypto.Util.number import *
from math import log
s=""
D=open("output.txt","r").readlines()
for i in range(len(D)):
    y=float(D[i])
    for x in range(1,128):
        if abs(x*log(x)-y)<0.1:
            s+=chr(x)
print(s)
#0xGame{ChuTiRenDeQQShiJiShangJiuShiQDeZhi}
