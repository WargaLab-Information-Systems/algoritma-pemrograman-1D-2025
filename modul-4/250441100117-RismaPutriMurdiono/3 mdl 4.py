# # Meminta input jumlah baris piramida
# n = int(input("Masukkan jumlah baris (n): "))

# # Perulangan baris luar
# for i in range(1, n + 1):

#     # --- Piramida kiri ---
#     for j in range(1, i + 1):
#         print(j, end=" ")

#     # --- Spasi di tengah (jarak antara dua piramida) ---
#     spasi = 2 * (n - i)
#     for k in range(spasi):
#         print(" ", end=" ")

#     # --- Piramida kanan (cermin) ---
#     for j in range(i, 0, -1):
#         print(j, end=" ")

#     # Pindah ke baris berikutnya
#     print()

n = int(input("Masukkan jumlah baris (n): "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    # spasi = 2 * (n - i)
    # for k in range(spasi):
    #     print(" ", end=" ")

    for j in range(i, 0, -1):
        print(j, end=" ")

    print()

# n = int(input("Masukkan nilai n: "))

# width = len(str(n)) + 1

# for i in range(1, n + 1): 
#     # l
#     for j in range(1, i + 1):
#         print(f"{j:{width}}", end="")

#     # m 
#     space = (n - i) * width * 2 
#     print(" " * space, end="")

#     # r
#     for j in range(i, 0, -1):
#         print(f"{j:{width}}", end="")
#     print()
