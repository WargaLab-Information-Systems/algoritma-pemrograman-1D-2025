# Program pola piramida angka

# Meminta input jumlah baris dari pengguna
n = int(input("Masukkan jumlah baris piramida: "))

# Loop luar untuk setiap baris
for i in range(1, n + 1):
    # Loop pertama untuk mencetak spasi agar piramida rapi
    for j in range(n - i):
        print(" ", end=" ")
    
    # Loop kedua untuk mencetak angka secara berurutan
    for k in range(1, i + 1):
        print(k, end=" ")
    
    # Pindah ke baris berikutnya
    print()
