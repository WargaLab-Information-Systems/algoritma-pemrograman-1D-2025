panjang = float(input("masukkan panjang:"))
lebar = float(input("masukkan lebar:"))
tinggi = float(input("masukkan tinggi:"))

volume_balok = panjang * lebar *tinggi

luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print ("\n=====HASIL PERHITUNGAN=====")
print ("panjang balok: ",panjang)
print ("lebar balok: ",lebar)
print ("tinggi balok: ",tinggi)
print ("volume balok adalah: ",{volume_balok,})
print ("luas balok adalah: ",{luas_permukaan,})
