from random import *
def getflag():
    flag1='0xGame{86767788-6000-7608-6777-54'
    table="0123456789abcdef"
    for i in range(10):
        flag1+=choice(table)
    return flag1+"}"
#print(getflag())
