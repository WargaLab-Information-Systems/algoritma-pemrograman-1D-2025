print ("\n" + "="*60)
print ("program menampilkan bilangan prima dari 1 sampai (n)")
print ("="*60)

n = int(input("masukkan batas angka terakhir(n): "))
print ("bilangan prima dari 1 sampai (n): ")

for angka in range (2, n+1):
    prima = True 
    for i in range (2, angka):
        if angka % i== 0:
            prima = False
            break 
    if prima :
        print (angka, end=" ")
