from random import *
from datetime import *
def getflag():
    flag="0xGame{JieFang!!!ChengHen@@@YouQu_GaoShu>>>YeRuCi!}"
    flag=flag.replace("!!!",str(randint(100,999)))
    flag=flag.replace("@@@",oct(randint(0o100,0o777))[2:])
    flag=flag.replace(">>>",hex(randint(0x100,0xfff))[2:])
    return flag

