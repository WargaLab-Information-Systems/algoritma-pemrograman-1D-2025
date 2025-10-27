#tugas pendahuluan modul 4 nomer 2
# Program pola segitiga angka menggunakan nested loop

# n = int(input("Masukkan jumlah baris: "))

# for i in range(1, n + 1):       
#     for j in range(1, i + 1):    
#         print(j, end=" ")
#     print()  

# Contoh perulangan for
# for i in range(1, 6):
#     print("Ini pengulangan ke-", i)

# Contoh perulangan while
# ulang = True
# while ulang:
#     jawab = input("Apakah kamu ingin lanjut (y/t)? ")
#     if jawab == "t":
#         ulang = False
#         print("Program berhenti.")

# for i in range(10000):
#     for j in range(10000):
#         if i == j:
#             print(i)

# a, b = 0, 1
# for i in range(10):
#     print(a, end=" ")
#     a, b = b, a + b

# n = int(input("Masukkan jumlah baris pola piramida: "))

# for i in range(1, n + 1):
#     print(" " * (n - i) * 3, end="")  # spasi depan
#     for j in range(1, i + 1):
#         print(f"{j:2}", end=" ")      # angka dengan lebar 2 karakter
#     print()


#pertemuan modul 4

##perulangan bersarang (nested loops)
# n = int(input("masukkan jumlah baris yang diinginkan: "))

# for i in range(1, 6):
#     for j in range (1, i + 1):
#         print(j, end=" ")
#     print()

##struktur perulangan dan kombinasi
##fpb
# a = int(input("masukkan nilai pertama: "))
# b = int(input("masukkan nilai kedua: "))

# while b != 0:
#     sisa = a%b
#     a = b
#     b = sisa
# print("FPB nya adalah : ", a)

##pola matematika dalam perulangan
# print("deret fibonacci")
# n = int(input("masukkan batas akhir deret fibonacci yang diinginkan: "))

# a, b = 0, 1
# #for i in range(n):
# while a <= n:
#     print(a, end=" ")
#     a, b = b, a + b

#contoh lain nested loops (piramida)
# n = int(input("masukkan angka: "))

# for i in range (n):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print(k, end=" ")
#     for l in range(i -1, 0, -1):
#         print(l, end=" ")
#     print()  

#Loop luar (outer loop)
# for i in range(1, 4): #loop  ini akan berjalan 3 kali ( i = 1 2 3)
#     print(f"Loop luar i = {i}")

#     #Loop dalam (inner loop)
#     for j in range(1, 4): #loop ini juga akan berjalan 3 kali untuk setiap iterasi dari loop luar
#         print(f"loop dalam j = {j}")

# a = 24
# b = 36

# while b != 0 :
#     a, b = b, a % b
#     print (f"FPB-nya adalah : {a}")

# n = 100 #batas angka
# a, b = 0, 1

# print("Bilangan Fibonacci hingga", n)
# while a <= n:
#     print(a, end=" ")
#     a, b= b, a + b

# n = 5

# for i in range(1, n+1):

#     for j in range(n-i):
#         print('', end='')
#     for k in range(1, i+1):
#         print(k, end='')
#     print()

#TUGAS PRAKTIKUM MODUL 4
#nomer 1
# print("CEK KONDISI LAMPU")
# jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

# for baris in range(1, jumlah_baris + 1):
#     jumlah_lampu = int(input(f"Masukkan jumlah lampu di baris {baris}: "))
    
#     for lamp in range(1, jumlah_lampu + 1):
#         if lamp % 3 == 0:
#             print(f"Lampu ke-{lamp} pada baris {baris} menyala")
#         else:
#             print(f"Lampu ke-{lamp} pada baris {baris} rusak.")
    
#     if baris == jumlah_baris:
#         print("Periksa sambungan daya utama.")
    
# print ("-"*40)

#nomer 2
# print("GAJI PAK WOWO")
# gaji_pokok = 100000
# bonus_shift_malam = 50000

# total_jam_lembur = 0
# total_bonus = 0
# total_gaji = 0

# for hari in range(1, 8):
#     print(f"--- Hari ke-{hari} ---")
    
#     jam = int(input("Jumlah jam lembur: "))
#     while jam <=0:
#         print("Jam lembur tidak valid!")
#         jam = int(input("Jumlah jam lembur: "))

#     shift = input("Shift malam? (y/n): ").lower()

#     if jam > 8:
#         print("Lembur melebihi batas, tidak dihitung.")
#         jam = 0
#         bayar_lembur = 0
#     else:
#         if jam >= 1 and jam <= 3:
#             bayar_lembur = jam * 25000
#         elif jam == 4:
#             bayar_lembur = 100000
#         elif jam == 6:
#             bayar_lembur = 200000
#         elif jam == 8:
#             bayar_lembur = 300000
    
#     if shift == "y":
#         bonus = bonus_shift_malam
#     elif shift == "n":
#         bonus = 0
#     else:
#         print("Input salah, Bonus gagal di dapatkan.")
#         bonus = 0
    
#     total_jam_lembur += jam
#     total_bonus += bonus
#     total_gaji += gaji_pokok + bayar_lembur + bonus

# print("=== REKAP GAJI SEMINGGU ===")
# print(f"Total jam lembur: {total_jam_lembur} jam")
# print(f"Total bonus shift malam: Rp{total_bonus}")
# print(f"Total gaji: Rp{total_gaji}")

# #nomer 3
# n = int(input("Masukkan tinggi piramida: "))

# while n <= 0:
#     print("Tidak Valid!")
#     n = int(input("Masukkan tinggi piramida: "))

# for i in range(n, 0, -1):
#     # sisi kiri: angka naik dari 1 sampai i
#     for j in range(1, i + 1):
#         print(format(j, '2d'), end='')
#     # spasi tengah
#     for k in range(2 * (n - i)):
#         print('  ', end='')


#     # sisi kanan: angka turun dari i ke 1
#     for l in range(i, 0, -1):
#         print(format(l, '2d'), end='')
#     print()
