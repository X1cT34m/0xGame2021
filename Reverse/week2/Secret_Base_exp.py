import base64

cipher = "FbdbHqAUNzoiIDdUIDhSEnF54DHthDT5Hm05HVlREnoAhaF0Hn2dFBQVFC0="
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
mytable = "123DfgabcQeEFh4pklmnojqGHIJKLMNOPdRSTUVWXYZrstuvwxyz0ABCi56789+/"
print(base64.b64decode(cipher.translate(str.maketrans(mytable, table))))