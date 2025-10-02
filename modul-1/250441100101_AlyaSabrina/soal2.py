print ("soal no 2 : menghitung luas dan volume balok ")

panjang = int(input("masukkan panjang balok (CM): " ))
lebar = int(input("masukkan lebar balok (CM): "))
tinggi = int (input("masukkan tinggi balok (CM): "))

volume_balok = panjang * lebar * tinggi 
luas_balok = 2 * ( panjang * lebar + panjang *  tinggi + lebar * tinggi  )

print ("volume baloknya adalah (CM³): " , volume_balok )
print ("luas permukaan balok adalah (cm²): " , luas_balok )