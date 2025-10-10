# if

x = 5
if x == 5:
    print("x samadengan 5")

print("="*50)

x = "alpro_d"
if x == "alpro_d":
    print("saya ada di kelas ",x)



# if-else

password = "alprod"

if password == "alprob":
    print("Password anda benar")
else:
    print("Password anda salah")

# if-elif-else

nilai = int(input("masukkan nilai anda : "))
if nilai <0 or nilai >100:
    print("input tidak valid")
elif nilai >= 80 <=100:
    print("Nilai anda sangat bagus")
elif nilai >=70 <=79:
    print("Nilai anda bagus")
elif nilai >=40 <=69:
    print("Nilai anda cukup bagus")
else:
    print("Nilai anda kurang bagus")

# print("="*50) 

angka = int(input("masukkan angka"))

if angka > 0:
    print("Angka merupakan bilangan positif")
elif angka <0:
    print("Angka merupakan bilangan negatif")
else:
    print("Angka merupakan 0")

# if bersarang (Nested If)

x = int(input("Masukkan nilai x : "))
y = int(input("Masukkan nilai y : "))

if x == y:
    print("Nilai x sama dengan y")
else:
    if x > y:
        print("Nilai x lebih besar y")
    if x < y:
        print("Nilai x lebih kecil dari y")

nilai = int(input("Masukkan nilai anda : "))

if nilai >=70:
    print("Anda lulus")
    if nilai >= 90:
        print("Nilai anda sangat bagus")
    else:
        print("Nilai anda cukup")
else:
    print("Anda tidak lulus")

# if ternary

nilai = int(input("Masukkan nilai : "))

print("lulus") if nilai >=75 else print("Coba lagi")

umur = int(input("Masukkan umur anda : "))
anggota = input("Apakah anggota club (y/n)")

if umur < 12:
    kategori = "anak-anak"
else:
    if umur  < 18:
       if anggota == "y":
           kategori = "dewasa"
       else:
           kategori = ("Dewasa (Non-anggota)")
    else:
        if umur < 60 :
                kategori = "dewasa dan termasuk anggota"