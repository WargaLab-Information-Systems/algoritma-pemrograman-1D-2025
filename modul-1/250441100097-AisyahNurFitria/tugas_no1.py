#harga barang
buku_tulis = 5000
pensil = 4500

#menghitung total harga
jumlah_buku = int (input("masukkan jumlah buku : "))
jumlah_pensil = int(input("masukkan jumlah pensil : "))

harga = (buku_tulis * jumlah_buku) + (pensil * jumlah_pensil)
print("total harga adalah : " , harga)

#menghitung pajak
pajak = harga * 0.1
print = input("total pajak adalah : ", pajak)

#menghitung harga setelah dipajak 
bayar = harga + pajak
print("total harga yang harus dibayar adalah : ", bayar)