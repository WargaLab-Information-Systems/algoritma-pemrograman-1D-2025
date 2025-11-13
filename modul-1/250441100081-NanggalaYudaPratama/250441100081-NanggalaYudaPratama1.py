# TUGAS PRAKTIKUM NO.1
harga_bukuTulis = 5000
harga_pensil = 4500

total_itemBuku = int(input("Masukkan total buku: "))
total_itemPensil = int(input("Masukkan total pensil: "))

total = (total_itemBuku * harga_bukuTulis)+(total_itemPensil * harga_pensil)
pajak = 0.1 * total
setelah_pajak = (total + pajak)


print("Harga Buku tulis adalah:", harga_bukuTulis)
print("Harga Pensil adalah:", harga_pensil)
print("Total harga setelah pajak:",setelah_pajak)
print(" \n")



