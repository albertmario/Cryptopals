#!/usr/bin/python

#hamming_distance pake xor secara matematis
def hamming_distance(a,b):
	jum = 0
	
	for i in range(len(a)):
		if a[i] != b[i]:
			jum += 1		
#		jum += int(a[i]) ^ int(b[i])
	return jum

def cari_panjang_key(a):
	cipher = ''.join(format(ord(x), '08b') for x in a)
	min_size = 1000
	
	for i in range(2,40):
		#ambil i byte cipher, 1 byte = 8 bit
		cipher1 = cipher[i*0*8:i*1*8]
		cipher2 = cipher[i*1*8:i*2*8]
		cipher3 = cipher[i*2*8:i*3*8]
		cipher4 = cipher[i*3*8:i*4*8]
		
		#normalisasi
		jarak12 = hamming_distance(cipher1,cipher2) / float(i)
		jarak13 = hamming_distance(cipher1,cipher3) / float(i)
		jarak14 = hamming_distance(cipher1,cipher4) / float(i)
		jarak23 = hamming_distance(cipher2,cipher3) / float(i)
		jarak24 = hamming_distance(cipher2,cipher4) / float(i)
		jarak34 = hamming_distance(cipher3,cipher4) / float(i)
		
		jarak = (jarak12 + jarak13 + jarak14 + jarak23 + jarak24 + jarak34) / 6
		
		#cari jarak terkecil -> sebagai keysize
		if jarak < min_size:
			min_size = jarak
			b = i
	
#	print "Panjang key : ", b
#	print "Dengan jarak terkecil : ", min_size
	return b
