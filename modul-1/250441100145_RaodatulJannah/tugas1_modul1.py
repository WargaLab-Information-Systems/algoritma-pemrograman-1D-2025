harga_buku = 5000
harga_pensil = 4500

jumlah_buku = 3
jumlah_pensil = 2

pajak = 0.10 #10%

total_bayar_sebelum_pajak = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)
print ("total yang harus dibayar: ",total_bayar_sebelum_pajak)

jumlah_pajak = (total_bayar_sebelum_pajak * pajak)
print ("total pajak adalah: ",jumlah_pajak)

total_belanja_setelah_dihitung_pajak = (total_bayar_sebelum_pajak + jumlah_pajak)
print ("total keseluruhan yang harus dibayar adalah: ",total_belanja_setelah_dihitung_pajak)
