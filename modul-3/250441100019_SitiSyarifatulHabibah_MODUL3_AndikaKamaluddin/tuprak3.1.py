print("=== MENAMPILKAN BILANGAN PRIMA ===")

n = int(input("Masukkan batas akhir:"))
print("Bilangan prima dari 1 sampai", n, ":")
for i in range(2, n + 1):
    jufak = 0
    for j in range(1, i + 1):
        if i % j == 0:
            jufak = jufak + 1
    if jufak == 2:
        print(i)