# harga Barang
buku_tulis = 5000
pensil = 4500

# Menhitung Total Harga
jumlah_buku = int(input("Masukkan jumlah buku : "))
jumlah_pensil = int(input("Masukkan Jumlah pensil : "))

harga = (buku_tulis * jumlah_buku) + (pensil * jumlah_pensil)
print("total harga adalah : ", harga)

# Menghitung Pajak
pajak = harga * 0.1
print("total pajak adalah : ", pajak)

# Menghitung harga setelah di pajak
bayar = harga + pajak
print("total harga yang harus dibayar adalah : ", bayar)

