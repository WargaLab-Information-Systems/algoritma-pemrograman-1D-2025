def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()

    if sorted(kata1) == sorted(kata2):
        return True
    else:
        return False

kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

hasil = cek_anagram(kata_pertama, kata_kedua)

if hasil:
    print("Kedua kata tersebut adalah ANAGRAM!")
else:
    print("Kedua kata tersebut BUKAN anagram.")