# menghitung volume dan luas permukaan sebuah balok
print ("===jawaban===")
# menghitung volume 
panjang = int(input("masukkan panjang balok: "))
lebar = int(input("masukkan lebar balok: "))
tinggi = int(input("masukkan tinggi balok: "))
volume = (panjang * lebar * tinggi)
print ("volume dari balok tersebut = ", volume)

# menghitung luas 
luas = 2 * ((panjang*lebar) + (panjang*tinggi) + (lebar*tinggi))
print ("luas permukaan balok tersebut adalah = ", luas)