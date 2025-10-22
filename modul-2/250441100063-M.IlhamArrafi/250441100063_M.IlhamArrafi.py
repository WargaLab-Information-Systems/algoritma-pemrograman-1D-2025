#2504411-M.IlhamArrafi

#praktikum

#modul2

#soal2


# Program Menghitung Harga Tiket Bioskop

harga_normal = 50000

usia = int(input("Masukkan usia: "))
pelajar = input("Apakah Anda pelajar SMA? (Ya/Tidak): ")
hari = input("Masukkan hari (contoh: Senin, Selasa, dst): ")

diskon = 0

# Cek kondisi diskon
if usia < 12:
    diskon = 50
elif pelajar == "Ya":
    diskon = 30
elif hari == "Selasa":
    diskon = 20

# Hitung harga akhir
harga_bayar = harga_normal - (harga_normal * diskon / 100)

print(f"Diskon yang didapat: {diskon}%")
print(f"Harga yang harus dibayar: Rp{int(harga_bayar)}")


#soal3


# Program Menghitung Biaya Parkir Mall

# Input data dari pengguna
lama = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (Ya/Tidak): ")

# Cek apakah VIP
if vip == "Ya":
    total = 0
else:
    # Jika bukan VIP
    if lama <= 2:
        total = 5000
        #kalau bukan itu, maka laukan yang ini
    else:
        total = 5000 + (lama - 2) * 3000

    # Batasi maksimal biaya parkir
    if total > 20000:
        total = 20000

# Tampilkan hasil
print(f"Total biaya parkir: Rp{total}")