#program menghitung harga tiket bioskop dengan diskon terbesar
#harga anormal tiket
harga_normal= 50000

#pengguna
usia = int(input("masukan usia anda: "))
status_pelajar =input("apakah anda pelajar sma dengan kartu pelajar?(ya/tidak):")
hari= input ("masukan hari:")

#menetukan diskon
diskon= 0

if usia <12:
    diskon = 50
if status_pelajar == "ya" and diskon <30:
    diskon = 30
if hari == "selasa" and diskon < 20:
    diskon = 20
#hitung harga setelah diskon
harga_akhir = harga_normal - (harga_normal*diskon/100)

#hasil
print("/n=== RINCIAN PEMBAYARAN===")
print(f"harga tiket normal ; Rp{harga_normal:,}")
print(f"diskon yang didapatkan : {diskon}%")
print(f"harga yang harus dibayar : Rp{int(harga_akhir):,}")