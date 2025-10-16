print("====Menghitung Vol dan Luas Permukaan Balok====")

P = int(input("Masukkan Panjang Balok (cm): "))
L = int(input("Masukkan Luas Balok (cm): "))
T = int(input("Masukkan Tinggi Balok (cm): "))

print("====Hasil Perhitungan Balok====")
print("Volume Balok: ", P*L*T, "cm")
print("Luas Permukaan Balok: ", 2 *  (P*L + P*T + L*T), "cm")