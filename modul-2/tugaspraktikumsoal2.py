#Soal Nomor 2
harga_tiket = 50000
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA membawa kartu pelajar? (ya/tidak): ")
hari = input("Hari apa yang dikunjungi: ") 

diskon = 0

if usia < 12:
    diskon = 0.5  
if pelajar == "ya":
    diskon = max(diskon, 0.3)  
if hari == "Selasa":
    diskon = max(diskon, 0.2) 

harga_diskon = harga_tiket * (1 - diskon)
print("Harga tiket yang harus dibayar: Rp.", int(harga_diskon))
