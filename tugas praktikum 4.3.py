n = int(input("Masukkan jumlah angka (n): "))

lebar = len(str(n))
for i in range(1, n + 1):  
    

    for j in range(1, i + 1):   
        print(str(j).rjust(lebar), end=" ")

    spasi_tengah = 2 * (n - i) * (lebar + 1)
    
    for k in range(spasi_tengah):  
        print(" ", end="")
        
    for l in range(i, 0, -1):    
        print(str(l).rjust(lebar), end=" ")
        
    print()