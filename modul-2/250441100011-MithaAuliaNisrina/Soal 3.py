# Program menghitung tarif parkir mall

# Input data
lama = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

# Penyeleksian kondisi dengan perintah if bersarang
if vip == "ya":
    total = 0
else:
    if lama <= 2:
        total = 5000
    else:
        total = 5000 + (lama - 2) * 3000
        if total > 20000:
            total = 20000

# Output hasil
print("Total biaya parkir adalah Rp", total)
print("Lama waktu parkir sebesar", lama," jam")