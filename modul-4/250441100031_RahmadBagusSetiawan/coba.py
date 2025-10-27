# # Perulangan Bersarang (Nested Loops)
n = int(input("Masukkan jumlah baris: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# # struktur perulangan dan kombinasi
# # contoh FPB

# a = int(input("masukkan Nilai Pertama :"))
# b = int(input("masukkan Nilai Kedua :"))

# while b != 0:
#     sisa = a % b
#     a = b
#     b = sisa
# print("FPB nya adalah :", a)

# # pola matematika dalam Perulangan
# # Fibonacci
# print("Deret Fibonacci")

# n = int(input("Masukkan Batas Akhir Deret Fibonacci Yang Diinginkan :"))

# a, b = 0, 1
# for i in range (n):
#     print(a, end=" ")
#     a, b = b , a + b

# # contoh lain (Nested Loop)

# n = int(input("Masukkan Angka :"))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for k in range (i, i + 1):
#         print(k, end=" ")
#     for l in range (i - 1, 0, -1):
#         print(l, end=" ")
#     print()