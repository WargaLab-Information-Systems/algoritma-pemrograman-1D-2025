kalimat = input("Masukkan sebuah kalimat: ")

vokal = 0
konsonan = 0
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
            konsonan = konsonan + 1
else:
    kata_list = kalimat.split()
    for item in kata_list:
        kata = kata + 1

print("Jumlah huruf vokal : ", vokal)
print("jumlah huruf konsonan : ", konsonan)
print("jumlah kata dalam kalimat : ", kata)