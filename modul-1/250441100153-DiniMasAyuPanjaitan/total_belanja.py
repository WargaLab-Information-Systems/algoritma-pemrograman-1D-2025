# Data barang
harga_buku = 20000    # contoh harga per buku
jumlah_buku = 3

harga_pensil = 4500
jumlah_pensil = 2

# Hitung total harga barang
total_buku = harga_buku * jumlah_buku
total_pensil = harga_pensil * jumlah_pensil
total_harga = total_buku + total_pensil

# Pajak 10%
pajak = 0.10 * total_harga

# Total bayar
total_bayar = total_harga + pajak

# Output
print("=== Struk Belanja ===")
print("Jumlah buku \t: ", jumlah_buku, "x Rp", harga_buku, "= Rp", total_buku)
print("Jumlah pensil \t: ", jumlah_pensil, "x Rp", harga_pensil, "= Rp", total_pensil)
print("Total harga barang : Rp", total_harga)
print("Pajak (10%) \t: Rp", int(pajak))
print("Total yang dibayar : Rp", int(total_bayar))
