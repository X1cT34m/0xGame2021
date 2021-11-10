from Crypto.Util.number import *
from secret import flag,p,q
assert q>p 
n=p*q
e=10007
assert len(flag)==42
for i in range(6):
    m=bytes_to_long(flag[i*7:i*7+7])
    print(pow(m,e,n))
print("Encryption using modulus n=",n)
"""
OutPut:
1150947306854980854
243703926267532432
1069319314811079682
688582941857504686
670683629344243145
1195068175327355214
Encryption using modulus n= 1687126110378632809
"""
