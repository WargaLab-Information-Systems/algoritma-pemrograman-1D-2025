
lama_parkir = int(input("Berapa lama kamu parkir(jam): "))

vip = input("Apakah memmber VIP? (ya/tidak): ")

if vip == "ya":
    total = 0
else:
    if lama_parkir <= 2:
        total = 5000
    else:
        total = 5000 + (lama_parkir - 2) * 3000

    # Maksimal tarif parkir perhari Rp20.000
    if total >= 20000:
        total = 20000

# Output hasil
print("\nTotal biaya parkir: Rp", total)