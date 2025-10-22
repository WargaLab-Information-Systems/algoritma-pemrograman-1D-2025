n = int(input("masukan batas akhir (n): "))

print("bilangan prima dari 1 sampai", n, "adalah")

#didalam kurung,contoh (23) namanya parameter
for angka in range (23):
    prima = True

    for pembagi in range (2, angka):
        if angka % pembagi == 0:
            prima = False
            break

    if prima:
        print(angka) 