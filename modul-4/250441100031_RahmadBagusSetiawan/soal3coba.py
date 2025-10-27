# SOAL 3
# Meminta pengguna memasukkan angka
n = int(input("Masukkan nilai n: "))

# Menghitung lebar maksimum berdasarkan digit angka terbesar
lebar = len(str(n))  + 1# +1 supaya ada jarak antar angka

# Perulangan untuk setiap baris
for i in range(1, n + 1):
    # Bagian kiri
    for j in range(1, i + 1):
        print(f"{j:{lebar}}", end="")

    tengah = (n - 1) * lebar * 2
    print(" " * tengah, end="")

    # Bagian kanan
    for j in range(i, 0, -1):
        print(f"{j:{lebar}}", end="")

    # Pindah ke baris berikutnya
    print()                                                  