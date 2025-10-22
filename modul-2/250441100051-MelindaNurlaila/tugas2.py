# program menghitung harga tiket

usia = int(input("Masukkan umur : "))
status = input("Apakah pelajar SMA dengan kartu pelajar ? (ya/tidak) : ")
hari = input("Masukkan hari : ")

harga_normal = 50000

if usia <= 12 :
    diskon = 50
    keterangan = "Anak-anak (< 12 tahun)"
elif status == "ya" :
        diskon = 30
        keterangan = "Pelajar SMA dengan kartu pelajar"
elif hari == "selasa" :
      diskon = 20
      keterangan = "Hari Selasa (Promo)"
else:
      diskon = 0
      keterangan = "Tidak Ada Diskon"
if diskon == 50:
      harga_akhir = harga_normal*50/100
elif diskon == 30:
      harga_akhir = harga_normal*70/100
elif diskon == 20:
      harga_akhir = harga_normal*80/100
else:
      harga_akhir = harga_normal

print(f"Diskon yang didapatkan : {diskon}% ({keterangan})")
print(f"Harga tiket yang harus dibayar : Rp. {harga_akhir :,}")