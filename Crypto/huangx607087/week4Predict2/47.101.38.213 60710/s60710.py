from random import *
def getflag():
    flag1='0xGame{87087788-7777-'
    flag2="5-3"
    flag3="-51284432****}"
    s=""
    table="0123456789abcdef"
    for i in range(3):
        flag2=choice(table)+flag2
    for i in range(3):
        flag2+=choice(table)
    for i in range(4):
        s+=choice(table[:10])
    flag3=flag3.replace("****",s)
    return flag1+flag2+flag3

#print(getflag())
