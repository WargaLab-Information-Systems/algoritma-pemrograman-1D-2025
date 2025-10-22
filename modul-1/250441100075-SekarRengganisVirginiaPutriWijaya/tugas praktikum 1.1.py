# Menghitung total belanja

# Harga barang
harga_buku_tulis = int(input("Masukkan harga buku tulis: "))
harga_pensil = int(input("Masukkan harga pensil: "))

# Jumlah barang yang dibeli
jumlah_buku_tulis = int(input("Masukkan jumlah buku tulis: "))
jumlah_pensil = int(input("Masukkan jumlah pensil: "))

# Jumlah total harga sebelum kena pajak
total_harga = (jumlah_buku_tulis * harga_buku_tulis) + (jumlah_pensil * harga_pensil)

# Cara menghitung pajak
pajak = total_harga * 0.10

# Menghitung total belanja dengan pajak
total_bayar = total_harga + pajak

print ("Total harga sebelum pajak: Rp", total_harga)
print ("Pajak (10%): Rp", pajak)
print ("Total yang harus dibayar: Rp", total_bayar)