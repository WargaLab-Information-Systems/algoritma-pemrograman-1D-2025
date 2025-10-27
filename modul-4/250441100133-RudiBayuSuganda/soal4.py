n = int(input("Masukkan jumlah baris yang di inginkan:"))
lebar=len(str(n)) + 1 
for i in range(1,n+1):
    
    for j in range(i,0,-1):
        print(f"{j:{lebar}}", end="")
    
    spasi = (n - i) * lebar * 2 
    print(" " * spasi, end="")
    
    for k in range(1,i+1):
         print(f"{k:{lebar}}", end="")
    # # for k in range(i,0,-1):
    #     print(f"{k:{lebar}}", end="")
    print()