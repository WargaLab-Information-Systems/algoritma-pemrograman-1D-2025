#jumlah dan harga barang
jumlah_buku = 3
jumlah_pensil =2
harga_buku =5000
harga_pensil =4500
#total harga sebelum pajak
total_buku = jumlah_buku*harga_buku
total_pensil = jumlah_pensil*harga_pensil 
total_belanja = total_buku+total_pensil
#pajak 10%
pajak = 0.10*total_belanja 
total_setelah_pajak = total_belanja + pajak

print("total belanja sebelum pajak: Rp", total_belanja)
print("pajak(0.10):Rp", int (pajak))
print("total yang harus dibayar: Rp", int (total_setelah_pajak))



