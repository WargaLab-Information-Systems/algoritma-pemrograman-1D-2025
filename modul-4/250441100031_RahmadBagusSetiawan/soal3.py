# Program Pola Piramida Cermin
print("=== Pola Piramida Cermin ===")

n = int(input("Masukkan tinggi piramida (contoh 5): "))

for i in range(1, n + 1):
    # sisi kiri
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # spasi di tengah
    tengah = "  " * (n - i) * 2
    print(tengah, end="")
    
    # sisi kanan
    for l in range(i, 0, -1):
        print(l, end=" ")
    
    print()  # ganti baris