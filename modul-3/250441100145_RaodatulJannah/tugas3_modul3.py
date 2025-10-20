kalimat = input("masukkan sebuah kalimat: ").lower()

vokal = 0
konsonan = 0

huruf_vokal = ("a", "i", "u", "e", "o")

for huruf in kalimat:
    if huruf.isalpha():
        if huruf in huruf_vokal:
            vokal +=1
        else:
            konsonan +=1

kata = kalimat.split()
jumlah_kata = len(kata)

print("\n===== HASIL ANALISIS KALIMAT=====")
print("jumlah huruf vokal    :", vokal)
print("jumlah huruf konsonan :", konsonan)
print("jumlah kata           :", jumlah_kata)