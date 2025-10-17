kalimat = str(input("Masukkan sebuah kalimat "))

vokal = "aeiou"
jumlah_huruf_vokal = 0
jumlah_huruf_konsonan = 0
jumlah_kata = 0

for karakter in kalimat:
    if karakter.isalpha(): 
        if karakter in vokal:
            jumlah_huruf_vokal += 1
        else:
            jumlah_huruf_konsonan += 1


jumlah_kata = len(kalimat.split())


print("Kalimat :", kalimat)
print("Jumlah huruf vokal     :", jumlah_huruf_vokal)
print("Jumlah huruf konsonan  :", jumlah_huruf_konsonan)
print("Jumlah kata            :", jumlah_kata)