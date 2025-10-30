n = int(input("Masukkan jumlah baris:"))

for i in range(1, n + 1):
   for j in range(1, i + 1):
    print(j, end="")
   for spasi in range((n - i) * 2):
    print(" ", end="")
   for k in range(i, 0, -1):
    print(k, end="")
   print()

   
# Meminta input jumlah baris
# n = int(input("Masukkan jumlah baris pola: "))

# # Loop untuk setiap baris
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for angka in range(1, i + 1):
#         print(angka, end="")
#     for angka in range(i - 1, 0, -1):
#         print(angka, end="")
#     print()