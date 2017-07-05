#!/usr/bin/python

from Crypto.Cipher import AES
import base64

def xor(a,b):
	hasil = ''
	for i in range(0, len(a)):
		hasil += chr(ord(a[i]) ^ ord(b[i]))
	return hasil

def decrypt(block1, key, block2):
	aes = AES.new(key)
	hasil = xor(block1, aes.decrypt(block2))
	return hasil

key = "YELLOW SUBMARINE"
iv = '\x00'*16
a = base64.b64decode(open('file').read())

hasil = ''
for i in range(0, len(a), 16):
	if i == 0:
		hasil += decrypt(iv, key, a[i:i+16])
	else:
		hasil += decrypt(a[i-16:i], key, a[i:i+16])

print hasil
