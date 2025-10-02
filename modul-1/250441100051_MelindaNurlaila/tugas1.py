print("Rincian Total Belanja")

harga_buku = 5000
harga_pensil = 4500
jumlah_buku = 3
jumlah_pensil = 2

# harga sebelum pajak
total_harga = (jumlah_buku*harga_buku) + (jumlah_pensil* harga_pensil)

# harga setelah pajak
pajak = 0.10 * total_harga

total_bayar = total_harga + pajak

print("Total harga sebelum pajak adalah : Rp", total_harga)
print("Total harga setelah pajak adalah : Rp", total_bayar)