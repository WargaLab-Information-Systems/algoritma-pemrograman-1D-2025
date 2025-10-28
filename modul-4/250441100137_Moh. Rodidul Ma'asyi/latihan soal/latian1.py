# CONTOH NESTED LOOPS

# n = int(input("masukkan jumlah baris yang diinginkan : "))

# for i in range (1,n) :
#     for j in range (1, i - 1) :
#         print(j, end= " ")
#     print()

# STRUKTUR PERULANGAN DAN KOMBINASI
# FPB

# a = int(input("masukkan nilai pertama : "))
# b = int(input("masukkan nilai kedua : "))

# while b != 0:
#     sisa = a%b
#     a = b
#     b = sisa
#     print("FPB m=nya adalah : ", a)

# POLA MATEMATIKA DALAM PERULANGAN
# FOR

# print("DERET FIBONACCI")

# n = int(input("masukkan batas akhir deret fibonacci yang diinginkkan : "))
# a, b = 0, 1
# for i in range (n):
#     print(a, end= " ")
#     a,b = b, a + b

# WHILE 

# n = int(input("masukkan batas akhir deret fibonacci yang diinginkkan : "))
# a, b = 0, 1
# while a <= n :
#     print(a, end= " ")
#     a, b = b, a + b

# CONTOH LAIN NESTED LOOPS 

# n = int(input("masukkan angka : "))

# for i in range (1, n + 1) :
#     for j in range (n-i):
#         print(" ", end=" ")
#     for k in range (1, i + 1):
#         print(k, end=" ")
#     for l in range (i - 1, 0, -1):
#         print(l, end=" ")
#     print()

# for i in range(1, 3):
#     print("Luar I ada : ", i)
#     for j in range(1, 5):
#         print("Dalam J ada : ", j)

# Program simulasi jam digital sederhana
# Menggunakan nested loop: jam → menit → detik

# for jam in range(0, 24):         # jam dari 0 sampai 23
#     for menit in range(0, 60):   # menit dari 0 sampai 59
#         for detik in range(0, 60):  # detik dari 0 sampai 59
#             print(f"{jam:02d}:{menit:02d}:{detik:02d}")

# print("\nPola segitiga bintang:")

# for i in range(1, 6):          # perulangan baris
#     for j in range(1, i + 1):  # perulangan kolom
#         print("*", end=" ")
#     print()  # pindah ke baris baru

# Program menampilkan pola piramida menggunakan perulangan bersarang (nested loop)

# tinggi = int(input("Masukkan tinggi piramida: "))

# for i in range(1, tinggi + 1):          # perulangan baris
#     for spasi in range(tinggi - i):     # perulangan untuk memberi jarak/spasi di depan
#         print(" ", end=" ")
#     for bintang in range(2 * i - 1):    # perulangan untuk menampilkan bintang
#         print("*", end=" ")
#     print()  # pindah ke baris baru setelah satu baris selesai

# Program menampilkan pola segitiga angka
# Menggunakan struktur perulangan bersarang (nested loop)

# tinggi = int(input("Masukkan tinggi pola: "))

# for i in range(1, tinggi + 1):        # perulangan baris
#     for j in range(1, i + 1):         # perulangan kolom
#         print(j, end=" ")             # menampilkan angka secara berurutan
#     print()                           # pindah ke baris berikutnya

# # Meminta input tinggi segitiga
# n = int(input("Masukkan tinggi pola: "))

# # Perulangan baris
# for i in range(1, n + 1):
#     # Perulangan kolom untuk mencetak bintang di setiap baris
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     # Pindah ke baris baru setelah satu baris selesai
#     print()
