kalimat = input("Masukkan sebuah kalimat: ")

vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0
in_kata = False

for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1
    elif ('A' <= huruf <= 'Z') or ('a' <= huruf <= 'z'):
        jumlah_konsonan += 1

    if huruf != ' ' and not in_kata:
        jumlah_kata += 1
        in_kata = True
    elif huruf == ' ':
        in_kata = False

print("Jumlah huruf vokal:", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata:", jumlah_kata)