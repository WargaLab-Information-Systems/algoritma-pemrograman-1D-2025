n = int(input("Masukkan nilai n : "))
print("Bilangan prima dari 1 hingga", n, "adalah:")
for angka in range(2, n + 1):  
    adalah_prima = True  
  
    for pembagi in range(2, angka):  
        if angka % pembagi == 0:
            adalah_prima = False  
            break  

    if adalah_prima:
        print(angka, end=" ")  

print()
