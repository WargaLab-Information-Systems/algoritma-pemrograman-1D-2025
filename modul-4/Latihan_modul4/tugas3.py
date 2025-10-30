# Program dua piramida berhadapan (cermin)
n = int(input("Masukkan nilai n: "))
for i in range(1, n + 1):    
    for j in range(1, i + 1):
        print(j, end="")  
    for k in range( (n - i) * 2 + 1):
        print(" ", end="") 
    for l in range(i, 0, -1):
        print(l, end="")
    print()
