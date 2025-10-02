#praktikum 01

#input jumlah dan harga barang
jumlah_buku = int(input("masukkan jumlah buku tulis: "))
harga_buku = int(input("masukkan harga satuan buku tulis: "))

jumlah_pensil = int(input("masukkan jumlah pensil: "))
harga_pensil = int(input("masukkan harga satuan pensil:"))

#hitung total sebelum pajak 
total_harga = (jumlah_buku * harga_buku) + (jumlah_pensil * harga_pensil)

#hitung total pajak 10%
pajak = total_harga * 0.10

#total bayar 
total_bayar = total_harga + pajak

print("===========================")
print("buku tulis :", jumlah_buku, "x RP", harga_buku,"=", jumlah_buku * harga_buku )
print("pensil :",jumlah_pensil, "X RP", harga_pensil,"=", jumlah_pensil * harga_pensil)
print("total harga sebelum pajak: Rp", total_harga)
print("pajak 10%: Rp",int(pajak))
print("total yang harus di bayar Rp", int(total_bayar))


#praktikum 02

# Program menghitung volume dan luas permukaan balok

# Input ukuran balok
panjang = float(input("Masukkan panjang balok (cm): "))
lebar = float(input("Masukkan lebar balok (cm): "))
tinggi = float(input("Masukkan tinggi balok (cm): "))

# Hitung volume
volume = panjang * lebar * tinggi

# Hitung luas permukaan
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

print("\n=== Hasil Perhitungan Balok ===")
print("Volume balok =", volume, "cm")
print("Luas permukaan balok =", luas_permukaan, "cm")


#praktikum 03

# Fungsi faktorial manual
def faktorial(n):
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    return hasil

# Program menghitung kombinasi bola
bola_merah = int(input("Masukkan jumlah bola merah: "))
bola_biru = int(input("Masukkan jumlah bola biru: "))
ambil = int(input("Masukkan jumlah bola yang diambil: "))

# Hitung total bola
total_bola = bola_merah + bola_biru

# Rumus kombinasi: C(n, r) = n! / (r! * (n-r)!)
kombinasi = faktorial(total_bola) // (faktorial(ambil) * faktorial(total_bola - ambil))

print("\n=== Hasil Kombinasi ===")
print("Jumlah bola merah =", bola_merah)
print("Jumlah bola biru  =", bola_biru)
print("Total bola =", total_bola)
print("Jumlah kombinasi yang bisa diambil =", kombinasi)