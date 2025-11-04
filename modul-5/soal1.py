print ("\n" + "="*60)
print (" program bilangan faktorial")
print ("="*60)

def faktorial (n) :
    if n == 0 or n == 1 :
        return 1
    else :
        return n * faktorial (n-1)
    
while True: 
    try : 
        n = int(input("masukkan bilangan bulat non-negatif: "))
        if n < 0 :
            print ("harus bilangan bulat non-negatif!")
        else :
            hasil = faktorial (n)
            print ("faktorial dari N : ", hasil)
            break 

    except :
        print ("input tidak valid! harap masukkan angka bilangan bulat positif, bukan huruf atau simbol")
