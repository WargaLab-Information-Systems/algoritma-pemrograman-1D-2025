buku_tulis = int(input("Masukkan harga buku tulis: "))
pensil = int(input("Masukkan harga pensil: "))
pajak = float(input("Masukkan pajak: "))

jumlah_buku_tulis = int(input("Masukkan jumlah buku tulis: "))
jumlah_pensil = int(input("Masukkan jumlah pensil: "))

# buku_tulis = 5000
# pensil = 4500
# pajak = 0.10

# jumlah_buku_tulis = 3
# jumlah_pensil = 2

total_harga = (jumlah_buku_tulis * buku_tulis) + (jumlah_pensil * pensil)
total_pajak = total_harga * pajak
total_bayar = total_harga + total_pajak

print("Total harga sebelum pajak: Rp", total_harga)
print("Total pajak: Rp", total_pajak)
print("Total yang harus dibayar: Rp", total_bayar)