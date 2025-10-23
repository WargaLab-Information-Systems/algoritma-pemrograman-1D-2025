panjang = float(input("masukkan panjang balok (cm):"))
lebar = float(input("masukkan lebar balok (cm):"))
tinggi = float(input("masukkan tinggi balok (cm):"))

volume = panjang*lebar*tinggi
luas = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)

print(f"volume balok :",volume)
print(f"luas permukaan =",luas) 