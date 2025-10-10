nilai = int(input("masukkan nilai anda : "))
hadir = int(input("Masukkan kehadiran : " ))

if nilai <0 or nilai >100:
    print("input tidak valid")
elif nilai >= 85 <=100:
    print("A")
elif nilai >=70 <=84:
    print("B")
elif nilai >=60 <=69:
    print("C")
elif nilai >=50 <=59:
    print("D")
else:
    print("E")

if nilai >=85 and hadir >=90:
    print("Lulus Dengan Pujian")
else :
     ()