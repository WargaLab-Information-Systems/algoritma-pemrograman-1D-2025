# Program sederhana untuk menghitung vokal, konsonan, dan jumlah kata

kalimat = input("Masukkan sebuah kalimat: ")

vokal = 0
konsonan = 0

for huruf in kalimat:
    if huruf.lower() in "aiueo":
        vokal = vokal + 1
    elif huruf.lower() in "bcdfghjklmnpqrstvvwxyz":
        konsonan = konsonan + 1

kata = kalimat.split()
jumlah_kata = len(kata)

print("Jumlah huruf vokal    :", vokal)
print("Jumlah huruf konsonan :", konsonan)
print("Jumlah kata           :",jumlah_kata)