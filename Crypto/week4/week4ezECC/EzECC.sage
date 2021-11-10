#Alice do this
p=14050339
a=1
b=3243167
E = EllipticCurve(GF(p),[a,b])
G=E(7112688,7410262)
k=random.randrange(1,G.order())
K=k*G
print(K)
#(6562993 : 2753874 : 1)
######################################
######################################
#Bob do this
import random
flag="0xGame{xxxxxxxx}"
table='abcdefghijklmnopqrstuvwxyz'
m=flag[7:-1]
m1=m[:4]
m2=m[4:]
m_1=''
m_2=''
for i in m1:
    s=str(table.index(i)+1)
    if len(s)<2:
        s='0'+s
    m_1+=s
for i in m2:
    s=str(table.index(i)+1)
    if len(s)<2:
        s='0'+s
    m_2+=s
x=int(m_1)
y=int(m_2)
P=E(x,y)
r=random.randrange(1,G.order())
C1=P+r*K
C2=r*G
print(C1)
#(3095063 : 1465594 : 1)
print(C2)
#(6437074 : 4385056 : 1)
######################################
######################################
#Eva wants to know the flag.
#Can you help Eva?