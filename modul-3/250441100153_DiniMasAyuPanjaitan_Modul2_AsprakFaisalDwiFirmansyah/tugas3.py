# Program untuk menganalisis kalimat
# Menghitung jumlah huruf vokal, konsonan, dan jumlah kata

kalimat = input("Masukkan sebuah kalimat: ")

# Inisialisasi
vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0

# Hitung huruf vokal dan konsonan
for huruf in kalimat:
    if huruf.isalpha():  # hanya huruf
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

# Hitung jumlah kata
jumlah_kata = len(kalimat.split())

# Tampilkan hasil
print("\n--- Hasil Analisis Kalimat ---")
print("Kalimat:", kalimat)
print("Jumlah huruf vokal    :", jumlah_vokal)
print("Jumlah huruf konsonan :", jumlah_konsonan)
print("Jumlah kata           :", jumlah_kata)