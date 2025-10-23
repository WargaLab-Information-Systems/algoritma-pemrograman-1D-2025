#Harga satuan

satuan_buku= 5000
satuan_pensil= 4500

# Jumlah yang dibeli
jumlah_buku_dibeli=3
jumlah_pensil_dibeli=2

# Total price sebelom pajak
total_price= (satuan_buku * jumlah_buku_dibeli) + (satuan_pensil * jumlah_pensil_dibeli)

# Hitung pajak 10%
tax= total_price * 0.10

# Hitung total setelah pajak
total_bayar= total_price + tax

print("Total Harga Sebelom Tax: Rp", total_price)
print("Tax (10%): Rp", int(tax))
print("Total yang harus dibayar: Rp", int(total_bayar))
