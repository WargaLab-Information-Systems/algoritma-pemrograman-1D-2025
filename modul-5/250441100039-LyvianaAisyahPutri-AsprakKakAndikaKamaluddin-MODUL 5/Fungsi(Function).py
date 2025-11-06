#PERTEMUAN 5 - FUNGSI (FUNCTION)
# def morning():
#     print("Selamat pagi")
# morning()

#hitungLuasPersegiPanjang(non-function)
# panjang = 5
# lebar = 3
# luas1 = panjang * lebar
# panjang2 = 8
# lebar = 2
# luas2 = panjang2 * lebar
# print(luas1, luas2)

#hitungLuasPersegiPanjang(function)
# def hitungLuas(panjang, lebar):
#     luas = panjang * lebar
#     print("Luas Persegi Panjangnya adalah:", luas)
# hitungLuas(10, 6)
# hitungLuas(5, 2)

#fungsi dengan return value
# def perkalian(a, b):
#     c = a * b
#     return c
# print(perkalian(3, 5))

# def perkalian(a):
#     c = a * a
#     return c
# # print(perkalian(int(input("masukkan angka:"))))
# print("makan")

#lambda
# tambah = lambda a, b, : a + b
# print(tambah(1, 2))

# def tambah(a,b):
#     return a + b
# print(tambah(1,2))

#fungsi rekursif
# def spillAngka(n):
#     if n == 0:
#         print("Selesai wes!")
#     else:
#         print(n)
#         spillAngka(n-1)
# spillAngka(5)

#scope variabel
# x = 10 #global
# def ubah_x():
#     x = 5 #lokal
#     print("Nilai x di dalam fungsi:", x)
# ubah_x()
# print("Nilai x di luar fungsi:", x)



#TUGAS PRAKTIKUM MODUL 5#
#NOMER 1
def factorial(n):
    if n < 0:
        return "Tidak bisa menghitung faktorial bilangan negatif!"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input dari pengguna
n = int(input("Masukkan bilangan N: "))
print(f"Faktorial dari {n} adalah {factorial(n)}")

# NOMER 2
def cek_anagram(kata1, kata2):
    # Hilangkan spasi dan ubah jadi huruf kecil
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    # Cek apakah huruf-hurufnya sama setelah diurutkan
    return sorted(kata1) == sorted(kata2)

# Input dari pengguna
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if cek_anagram(kata1, kata2):
    print(f"{kata1} dan {kata2} adalah anagram!")
else:
    print(f"{kata1} dan {kata2} bukan anagram!")

#NOMER 3
def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    gaji_bersih = (gaji_pokok + tunjangan) - pajak

    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan       : {jabatan}")
    print(f"Gaji Pokok    : Rp{gaji_pokok:,.2f}")
    print(f"Tunjangan     : Rp{tunjangan:,.2f}")
    print(f"Pajak (5%)    : Rp{pajak:,.2f}")
    print(f"Gaji Bersih   : Rp{gaji_bersih:,.2f}")

# Input dari pengguna
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)

