# jumlah buku dan pensil 
buku = int(input("Masukkan jumlah buku: "))
pensil = int(input("Masukkan jumlah pensil: "))
pajak = 10 / 100

# Harga satuan buku tulis dan pensil
harga_buku = buku * 5000
harga_pensil = pensil * 4500

# Total belanja sebelum pajak
total_harga = harga_buku + harga_pensil

# Pajak pembelian
pajak = total_harga * pajak

# Total belanja setelah pajak
total_belanja_setelah_pajak = int(total_harga + pajak)

print("Total belanja setelah pajak = Rp", total_belanja_setelah_pajak)