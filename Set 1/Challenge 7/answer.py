#!/usr/bin/python
#AES - 128 bit

import base64
from Crypto.Cipher import AES

key = 'YELLOW SUBMARINE' #16 byte = 128 bit
a = base64.b64decode(open('file').read())
aes = AES.new(key, AES.MODE_ECB)

print aes.decrypt(a)
