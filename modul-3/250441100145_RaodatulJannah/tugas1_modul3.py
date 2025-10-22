n = int(input("masukkan batas akhir bilangan:"))
print("bilangan prima dari 1 sampai",n, "adalah:")

for i in range(2, n + 1):
    faktor = 0
    for j in range(1, i + 1):
        if i % j == 0:
            faktor +=1

    if faktor == 2:
        print (i, end=" ")            