# Program Analisis Kalimat 

kalimat = input("Masukkan sebuah kalimat: ")

vokal_huruf = 'aeiouAEIOU'
semua_huruf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

vokal = 0
konsonan = 0

for huruf in kalimat:
    if huruf in semua_huruf:  
        if huruf in vokal_huruf:  
            vokal += 1
        else:  
            konsonan += 1

jumlah_kata = 0
dalam_kata = False  

for huruf in kalimat:
    if huruf != ' ':  
        if not dalam_kata:  
            jumlah_kata += 1
            dalam_kata = True
    else:  
        dalam_kata = False  


print("Hasil Analisis:")
print("a. Jumlah huruf vokal:", vokal)
print("b.  Jumlah huruf konsonan:", konsonan)
print("c. Jumlah kata:", jumlah_kata)
