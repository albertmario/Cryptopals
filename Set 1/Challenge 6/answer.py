#!/usr/bin/python

#breaking xor repeating key
import keysize
import base64

def single_xor_crack(a):
	kamus ='etaoinshrdlu ETAOINSHRDLU'
	for i in range(0,256):
		hasil = ''
		jum = 0
		
		for j in a:
			hasil += chr(i ^ ord(j))
		
		for k in hasil:
			if k.lower() in kamus:
				jum += 5
		
		if jum > 300:
			return i

def crack_repeat_key(a, key):
	hasil = ''
	for i in range(len(a)):
		hasil += chr(ord(a[i]) ^ ord(key[i % len(key)]))
	
	return hasil
	

a = base64.b64decode(open('file').read())
keysize = keysize.cari_panjang_key(a)
print "panjang key : ", keysize

key = ''

for j in range(keysize):
	block = ''
	for i in range(j, len(a), keysize):
		block += a[i]
		
	key += chr(single_xor_crack(block))

print "Key : ", key
print "Hasil : ", crack_repeat_key(a,key)
