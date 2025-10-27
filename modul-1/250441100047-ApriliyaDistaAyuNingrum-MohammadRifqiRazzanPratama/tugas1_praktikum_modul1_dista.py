# Program untuk menghitung total belanja Hallim setelah pajak 10%
# Harga satuan barang
harga_buku_tulis = 5000
harga_pensil = 4500

# Jumlah barang yang dibeli
jumlah_buku_tulis = 3
jumlah_pensil = 2

# Hitung total harga sebelum pajak
total_harga = (harga_buku_tulis * jumlah_buku_tulis) + (harga_pensil * jumlah_pensil)

# Hitung pajak 10%
pajak = 1 * total_harga

# Hitung total harga setelah pajak
total_bayar = total_harga + pajak

# Tampilkan hasil
print("Total harga sebelum pajak: Rp", total_harga)
print("Pajak (10%): Rp", float(pajak))
print("Total yang harus dibayar: Rp", float(total_bayar))
