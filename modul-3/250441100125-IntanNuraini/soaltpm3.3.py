kalimat = input("Tulis kalimat: ")
vokal = 0
konsonan = 0
for huruf in kalimat:
    huruf_kecil = huruf.lower()
    
    if huruf_kecil.isalpha():
        if huruf_kecil == 'a' or huruf_kecil == 'e' or huruf_kecil == 'i' or huruf_kecil == 'o' or huruf_kecil == 'u':
            vokal = vokal + 1
        else:
            konsonan = konsonan + 1
kata = kalimat.split()
jumlah_kata = len(kata)  
print("Hasil:")
print("Vokal:", vokal)
print("Konsonan:", konsonan)
print("Kata:", jumlah_kata)