kalimat = input("Masukkan sebuah kalimat: ").lower()
vokal = "aiueo"
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0
sebelum_spasi = False  
for huruf in kalimat:    
    if huruf.isalpha():
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1
    if huruf != " " and not sebelum_spasi:
        jumlah_kata += 1
        sebelum_spasi = True
    elif huruf == " ":
        sebelum_spasi = False
print("Jumlah huruf vokal:", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata:", jumlah_kata)