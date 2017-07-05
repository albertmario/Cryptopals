#!/usr/bin/python

#repeating XOR
a = open('file').read()
key = 'ICE'
hasil =''

for i in range(len(a)):
	hasil += chr(ord(a[i]) ^ ord(key[i%len(key)]))

print hasil.encode("hex")

