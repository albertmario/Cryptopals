#scoring english plaintext (alpha)

kamus ='etaoinshrdlu ETAOINSHRDLU'

a = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode("hex")


for x in range(0,256):
	hasil = ''
	jum = 0
	
	#hasil xor
	for i in a:
		hasil += chr(ord(i) ^ x)
	
	#untuk setiap hasil, cek dia inggris atau bukan
	for j in hasil:
		if j in kamus:
			jum+=5 #pake bobot 5
	
	#batasnya kira2 yg ada bahasa inggrisnya
	if jum > 100:
		print hasil
		
	hasil = ''
