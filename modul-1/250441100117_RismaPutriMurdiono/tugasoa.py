harga_buku = 5000
harga_pensil = 4500

jumlah_buku = 3
jumlah_pensil = 2

total = (harga_buku * jumlah_buku)+(harga_pensil * jumlah_pensil)

pajak = 0.10 * total

total_seluruh = total + pajak

print("total sebelum pajak: Rp", total)
print("pajak (10%): Rp", pajak)
print("total yang harus dibayar: Rp", total_seluruh)