print("=== PROGRAM ANALISA KALIMAT ===")

kalimat = input("Masukkan kalimat:")
vokal = 0
konsonan = 0
kata = 1

for huruf in kalimat:
    if huruf == " ":
        kata = kata + 1
    elif huruf in "aiueoAIUEO":
        vokal = vokal + 1
    elif huruf != " ":
        konsonan = konsonan + 1

print("Jumlah huruf vokal", vokal)
print("Jumlah konsonan:", konsonan)
print("Jumlah kata:", kata)