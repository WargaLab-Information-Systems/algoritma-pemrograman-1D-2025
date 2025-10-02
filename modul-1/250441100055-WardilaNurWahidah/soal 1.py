#harga satuan barang
harga_buku = 5000
harga_pensil = 4500

#jumlah barang yang dibeli
jumlah_buku = 3
jumlah_pensil = 2

#hitung total harga barang sebelum pajak
total_sebelum_pajak = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)

#pajak 10%
pajak = 0.10 * total_sebelum_pajak

#total bayar setelah pajak
total_setelah_pajak = total_sebelum_pajak + pajak

#output hasil
print("Total sebelum pajak: Rp", total_sebelum_pajak)
print("Pajak 10%: Rp", int(pajak))
print("Total yang harus dibayar: Rp", int(total_setelah_pajak)) 