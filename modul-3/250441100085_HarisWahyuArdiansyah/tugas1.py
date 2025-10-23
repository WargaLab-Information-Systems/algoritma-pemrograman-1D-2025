angka = int(input("masukan batas angka : "))

for i in range(2,angka + 1):
    prima = True
    for a in range(2,i):
        if i % a == 0:
            prima = False
            break
    if prima:
        print(i)
