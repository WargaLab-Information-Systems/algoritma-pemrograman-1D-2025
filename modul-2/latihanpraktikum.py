# Latihan Praktikum 1
usia_saya = int (input("Masukkan Usia Anda :"))
BATAS_USIA = 18

if usia_saya >= BATAS_USIA:
    print(" Boleh Menonton!")
    print("Anda telah mencapai usia minimum 18 tahun.")
else:
    print(" Tidak Boleh Menonton.")
    print(f"Usia Anda baru {usia_saya}, belum mencapai {BATAS_USIA} tahun.")

# Latihan Praktikum 2

kecepatan = int(input("Masukkan nilai kecepatan (dalam km/jam): "))
if kecepatan <= 30:
    print(f"Kecepatan: {kecepatan} km/jam.")
    print("Klasifikasi: Sangat Lambat.")
elif kecepatan <= 80:
    print(f"Kecepatan: {kecepatan} km/jam.")
    print("Klasifikasi: Sedang.")
else:
    print(f"Kecepatan: {kecepatan} km/jam.")
    print("Klasifikasi: Cepat!")

# Latihan praktikum 3
umur = int(input("Masukkan umur anda sekarang :"))
if umur <= 18 :
    print ("Anak Muda")
elif umur <= 30 :
    print ("Remaja")
else:
    print ("Tua bangka")