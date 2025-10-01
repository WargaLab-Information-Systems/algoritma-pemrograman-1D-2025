#soal no1
print("======================================")
harga_bukuTulis = 5000
harga_pensil = 4500

jumlah_bukuTulis = int(input("masukkan jumlah buku : "))
jumlah_pensil = int(input("masukkan jumlah pensil :"))

total = (harga_bukuTulis * jumlah_bukuTulis) + (harga_pensil * jumlah_pensil)
pajak = 0.1  * total

total_keseluruhan = total + pajak
print("total sebelum pajak: Rp", total)
print("pajak (10%): Rp", pajak)
print("total yang harus dibayar: Rp", total_keseluruhan)