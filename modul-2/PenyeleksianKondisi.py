# # # ## Tugas Pendahuluan Modul 2
#Penyeleksian Kondisi

# # # ## Latihan 1
# # # ##1. Di bawah ini adalah contoh program Penyeleksian kondisi pada Bahasa pemrograman Python

# # # nomor_acak = 7
# # # print('Tebak nomor acak antara 1-10')
# # # tebakan = int(input('Masukkan tebakan Anda (bil bulat): '))
# # # if tebakan == nomor_acak:
# # #     print('Selamat! tebakan Anda benar')
# # #     print('tapi tidak ada hadiah untuk anda :(')
# # # elif tebakan < nomor_acak:
# # #     print('Tebakan Anda terlalu kecil')
# # # else:
# # #     print('Tebakan Anda terlalu besar')
# # # print('selesai')

# # # ## 2. contoh program penyeleksian kondisi
# # # a = int(input("Masukkan umur: "))
# # # if a <= 15:
# # #     print("Muda")
# # # elif a <= 20:
# # #     print("Remaja")
# # # else:
# # #     print("Tua")

# # # ## 3. Menentukan Ganjil Genap
# # # #genjil genap
# # # nilai = int(input("Masukkan angka: "))
# # # if nilai % 2:
# # #     print("Bilangan Ganjil")
# # # else:
# # #     print("Bilangan Genap")

# # # ##Latihan 2
# # # ##Buatlah program jika andi memasukan nilai 1 sampai 9 , maka outputnya “angka anda satu “ –“angka anda Sembilan “ menggunakan operasi if elif dan else

# # # #buatlah program j
# # # #angka ke kata
# # # a = int(input("Masukkan angka (0-9): "))
# # # if a == 0:
# # #     print("angka anda nol")
# # # elif a == 1:
# # #     print("angka anda satu")
# # # elif a == 2:
# # #     print("angka anda dua")
# # # elif a == 3:
# # #     print("angka anda tiga")
# # # elif a == 4:
# # #     print("angka anda empat")
# # # elif a == 5:
# # #     print("angka anda lima")
# # # elif a == 6:
# # #     print("angka anda enam")
# # # elif a == 7:
# # #     print("angka anda tujuh")
# # # elif a == 8:
# # #     print("angka anda delapan")
# # # elif a == 9:
# # #     print("angka anda sembilan")
# # # else:
# # #     print("angka anda not found")




















#Tugas Pendahuluan Modul 2
#Nomor 2  
# Apa perbedaan antara if, if-else, if-elif-else, dan if bersarang? Jelaskan dengan Bahasa kalian sendiri dan berikan contoh kodenya!
# # #Jawab:
# Perbedaan antara if, if-else, if-elif-else, dan if bersarang adalah sebagai berikut:
# 1. if: untuk blok kode dalam kondisi tertentu dan terpenuhi.
#Contoh:
# nilai = 75
# if nilai >= 60:
#     print("Lulus")
# #2. if-else: untuk menjalankan satu blok kode jika terpenuhi atau tidak terpenuhi.
# #Contoh:
# nilai = 50
# if nilai >= 60:
#     print("Lulus")
# else:
#     print("Tidak Lulus")
#3. if-elif-else: Digunakan untuk beberapa kondisi secara berurutan. Jika salah satunya terpenuhi, blok kode yang sesuai akan dijalankan.
#Contoh:
# nilai = 95
# if nilai >= 90:
#     print("A")
# elif nilai >= 80:
#     print("B")
# elif nilai >= 70:
#     print("C")
# else:
#     print("D") 
# Output: B
# # # #4. if bersarang: untuk menjalankan blok kode di dalam blok kode lain. memungkinkan untuk membuat keputusan yang lebih kompleks.
# # # # Contoh:
# nilai = 95
# if nilai >= 60:
#     if nilai >= 90:
#         print("A")
#     elif nilai >= 80:
#         print("B")
#     else:
#         print("C")
# else:
#     print("D")  
#Output: A
# # ##Nomor 5# Buatlah Program dengan Studi Kasus Berikut :
# Sebuah jalan tol memberikan ketentuan pembayaran sebagai berikut: Tarif
# dasar tol berbeda sesuai jenis kendaraan:
# • Mobil pribadi → Rp15.000
# • Truk kecil → Rp25.000
# • Truk besar → Rp40.000
# Diskon tarif tol berlaku jika:
# • Jika pembayaran menggunakan e-money → diskon 10%
# • Jika pembayaran menggunakan e-money dan dilakukan pada jam sepi
# (23.00 – 05.00) → diskon 20%
# • Jika pembayaran tunai → tidak ada diskon

# Buatlah program untuk menghitung tarif tol yang harus dibayar
# berdasarkan jenis kendaraan, metode pembayaran, dan waktu pembayaran
# (jam sepi atau tidak). Gunakan struktur penyeleksian kondisi yang
# sesuai untuk menyelesaikan masalah ini.
# jenis_kendaraan = input("Masukkan jenis kendaraan (mobil pribadi/truk kecil/truk besar): ").lower()
# metode_pembayaran = input("Masukkan metode pembayaran (e-money/tunai): ").lower()
# waktu_pembayaran = int(input("Masukkan jam pembayaran (0-23): "))
# if jenis_kendaraan == "mobil pribadi":
#     tarif_dasar = 15000
# elif jenis_kendaraan == "truk kecil":
#     tarif_dasar = 25000
# elif jenis_kendaraan == "truk besar":
#     tarif_dasar = 40000
# else:
    # print("Jenis kendaraan tidak valid")
#     tarif_dasar = 0
# diskon = 0
# if metode_pembayaran == "e-money":
#     if 23 <= waktu_pembayaran or waktu_pembayaran < 5:
#         diskon = 0.20
#     else: 
#         diskon = 0.10
# elif metode_pembayaran == "tunai":
#     diskon = 0
# else:
#     print("Metode pembayaran tidak valid")
#     diskon = 0
# tarif_akhir = tarif_dasar * (1 - diskon)
# if tarif_dasar > 0:
#     print(f"Tarif tol yang harus dibayar: Rp{tarif_akhir:.2f}")


























# tugas praktikum modul 2 

# soal nomer 2
# harga_normal = 50000
# diskon = 0

# usia = int(input("masukkan usia penonton:"))
# pelajar = input("apakah kamu pelajar SMA dengan kartu pelajar? (ya/tidak):").lower()
# hari = input("masukkan hari :").capitalize()

# if usia < 12:
#     diskon = 50

# if pelajar == "ya":
#     if diskon < 30:
#        diskon = 30

# if hari == "":
#     if diskon < 20:
#         diskon = 20
    
# harga_bayar = harga_normal - (harga_normal * diskon / 100)
# print(f"\nDiskon yang didapat : {diskon}%")
# print(f"Harga yang harus dibayar:Rp{harga_bayar:,.0f}")

#soal nomer 3
# Program Menghitung Biaya Parkir

# lama_parkir = float(input("Masukkan lama parkir (jam): "))
# vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

# if vip == "ya":
#     total = 0
# else:
#     if lama_parkir <= 2:
#         total = 5000
#     else:
#         total = 5000 + (lama_parkir - 2) * 3000
    
#     # Batas maksimal
#     if total > 20000:
#         total = 20000

# print(f"Total biaya parkir: Rp{total:,.0f}")