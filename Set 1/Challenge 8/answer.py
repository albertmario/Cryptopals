#!/usr/bin/python

def detect_ecb(text):
	blocks = []
	for i in range(0, len(text), 16):
		blocks.append(text[i:i+16])
	
	#fungsi set menghitung elemen yg unik saja dalam array
	if len(set(blocks)) == len(blocks):
		return False
	else:
		return True
	
a = open('file').read().split()

for i in range(0,len(a)):
	if detect_ecb(a[i].decode("hex")):
		print "di sini kyknya", i
		print "dengan text : ", a[i]
		break
