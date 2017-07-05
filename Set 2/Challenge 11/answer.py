#!/usr/bin/python

from Crypto.Cipher import AES
import random
import os

def pad_PKCS7(text, blocks):
	pad = blocks - len(text) % blocks
	return text + chr(pad) * pad

def encrypt_ecb(text, key):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(pad_PKCS7(text,16))
	
def encrypt_cbc(text, key, iv):
	aes = AES.new(key, AES.MODE_CBC, iv)
	return aes.encrypt(pad_PKCS7(text,16))
	
def detect_mode(encrypt):
	blocks = []
	for i in range(0, len(encrypt), 16):
		blocks.append(encrypt[i:i+16])
		
	if len(blocks) == len(set(blocks)):
		return len(blocks), len(set(blocks)), "CBC"
	else:
		return len(blocks), len(set(blocks)), "ECB"
	
iv = os.urandom(16)
key = os.urandom(16)
append = random.randint(5,10)
text = os.urandom(append)+"A"*1024+os.urandom(append)
i = random.randint(0,1)

print "Plain : ", text
if i:
	encrypt = encrypt_ecb(text,key)
	print "Hasil encrypt : ", encrypt
else:
	encrypt = encrypt_cbc(text,key,iv)
	print "Hasil encrypt : ", encrypt
	
print "Metode encrypt: ", detect_mode(encrypt)
