
jumlah_buku = 3
jumlah_pulpen = 2
 
harga_buku = 5000
harga_pulpen = 4500

total_harga_buku = (jumlah_buku * harga_buku)
total_harga_pulpen= (jumlah_pulpen * harga_pulpen)

print("Total biaya Buku: Rp", total_harga_buku)
print("Total biaya pulpen: Rp", total_harga_pulpen)

harga_asli = total_harga_buku + total_harga_pulpen
print("harga asli: Rp",harga_asli)

pajak = harga_asli // 10
print ("pajak dari barang tersebut adalah :",pajak)

total_bayar = pajak + harga_asli
print("Jadi total harga yang harus dibayar: Rp",total_bayar)