# Analisis kalimat

kalimat = input("Masukkan kalimat: ").lower()

vokal = 0
konsonan = 0
kata = 1

for huruf in kalimat:
    if huruf in "aiueo":
        vokal = vokal + 1
    elif huruf == " ":
        kata = kata + 1
    else:
        konsonan = konsonan + 1

print("Jumlah huruf vokal:", vokal)
print("Jumlah huruf konsonan:", konsonan)
print("Jumlah kata:", kata)