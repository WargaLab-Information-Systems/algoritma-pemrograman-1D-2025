kalimat = input("Masukkan kalimat: ")

vokal = 0
jumlah_vokal = 0
jumlah_konsonan = 0
kata = 0

for karakter in kalimat:
    if karakter >= "a" and karakter <= "z":
        if karakter == "a":
            vokal = vokal + 1
        elif karakter == "i":
            vokal = vokal + 1
        elif karakter == "u":
            vokal = vokal + 1
        elif karakter == "e":
            vokal = vokal + 1
        elif karakter == "o":
            vokal = vokal + 1
        else:
            jumlah_konsonan = jumlah_konsonan + 1
else:
    kata_list = kalimat.split()
    for item in kata_list:
        kata = kata + 1

print("Jumlah huruf vokal : ", vokal)
print("jumlah huruf konsonan : ", jumlah_konsonan)
print("jumlah kata dalam kalimat : ", kata)