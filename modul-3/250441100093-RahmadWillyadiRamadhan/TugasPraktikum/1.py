# Program menampilkan bilangan prima dari 1 sampai n

# Meminta input dari pengguna
n = int(input("Masukkan batas angka (n): "))

print(f"Bilangan prima dari 1 sampai {n} adalah:")

# Perulangan dari 2 sampai n
for i in range(2, n + 1):
    # Asumsikan i adalah bilangan prima
    prima = True

    # Cek apakah i bisa dibagi oleh angka selain 1 dan dirinya sendiri
    for j in range(2, i):
        if i % j == 0:
            prima = False
            break  # hentikan pengecekan jika sudah terbukti bukan prima

    # Jika tetap prima, tampilkan angkanya
    if prima:
        print(i)
