def hitung_total_belanja():
    harga_buku = 5000
    harga_pensil = 4500
    jumlah_buku = 3
    jumlah_pensil = 2
    total_barang = (jumlah_buku * harga_buku) + (jumlah_pensil * harga_pensil)
    pajak = total_barang * 0.1
    total_bayar = total_barang + pajak
    return total_bayar


total_harus_dibayar = hitung_total_belanja()
print(f"Total uang yang harus dibayar Hallim ke kasir adalah: Rp {int(total_harus_dibayar)}")
