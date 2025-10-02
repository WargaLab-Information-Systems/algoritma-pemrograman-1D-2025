# total per barang
Harga_buku = 5000 * 3
Harga_pensil = 4500 * 2
persentase = 0.10
# Hitung total sebelum pajak
sebelum_pajak = Harga_buku + Harga_pensil
# Hitung pajak
pajak = persentase * sebelum_pajak
# Hitung total setelah pajak
setelah_pajak = sebelum_pajak + pajak
# Menampilkan hasil
print("Total sebelum pajak: Rp.", sebelum_pajak)
print(" Pajak: Rp.", pajak)
print(" Total setelah pajak: Rp.", setelah_pajak)