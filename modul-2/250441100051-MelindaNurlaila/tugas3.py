# program menghitung tarif parkir

lama_parkir = int(input("Masukkan lama parkir (jam) : "))
status = input("Apakah anda member VIP? (ya/tidak) : ")

if status == "ya":
    biaya = 0
else:
    if lama_parkir <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (lama_parkir - 2) * 3000
if biaya > 20000:
    biaya = 20000

print("Total biaya parkir : Rp.", biaya)