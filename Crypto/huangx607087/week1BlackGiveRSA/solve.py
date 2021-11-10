from Crypto.Util.number import *
p,q=1175078221,1435756429
n,phi=p*q,(p-1)*(q-1)
d=inverse(10007,phi)
cipher=[
    1150947306854980854,
    243703926267532432,
    1069319314811079682,
    688582941857504686,
    670683629344243145,
    1195068175327355214
    ]
m=b""
for c in cipher:
    m+=long_to_bytes(pow(c,d,n))
print(m)
#0xGame{ChuTiRenDeQQShiJiShangJiuShiQDeZhi}
