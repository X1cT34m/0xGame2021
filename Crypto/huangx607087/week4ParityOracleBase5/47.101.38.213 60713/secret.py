from random import *
def getflag():
    flag1='0xGame{'
    flag2=''
    flag3='-6076-8067-8848-taijinshouji}'
    table="0123456789abcdef"
    for i in range(4):
        flag2+=choice(table)
    for i in range(4):
        flag2+=choice(table[:8])
    return flag1+flag2+flag3

