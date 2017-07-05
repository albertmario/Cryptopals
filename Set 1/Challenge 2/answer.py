a = '1c0111001f010100061a024b53535009181c'.decode("hex")
b = '686974207468652062756c6c277320657965'.decode("hex")
hasil = ''

for i in range(len(a)):
	hasil += chr(ord(a[i]) ^ ord(b[i]))

'746865206b696420646f6e277420706c6179' == hasil.encode("hex")