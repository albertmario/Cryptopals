#!/usr/bin/python

#looping setiap byte
def cari_hasil(a):
	kamus ='etaoinshrdlu '
	for x in range(0,256):

		#looping setiap baris di file
		for i in a:
			hasil = ''
			jum = 0
#			i = i.decode("hex") #decode dulu jadi hex
		
			#setiap hasil di baris itu, dixor
			for j in i:
				hasil += chr(ord(j) ^ x)
			for k in hasil:
				if k.lower() in kamus:
					jum += 5
			
			if jum > 100:
				print "byte - ", x
				print "baris yg isinya : ", i
				print "jawaban : ", hasil
