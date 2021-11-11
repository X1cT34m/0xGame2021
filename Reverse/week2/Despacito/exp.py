from Crypto.Cipher import DES
import hashlib
f = open('cipher.txt', 'rb')
plaintext = f.read()
key = b'0xgame21'
cipher = DES.new(key, DES.MODE_ECB)
message = cipher.decrypt(plaintext)
print("plain.text is ", str(message, encoding = "utf-8"))

md5 = hashlib.md5()
md5.update(message)
print('0xGame{' + md5.hexdigest() + '}')