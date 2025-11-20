def cek_anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    if kata1 == kata2:
        return False

    if sorted(kata1) == sorted(kata2):
        return True
    else:
        return False

print("==== Validasi Kata ====")
kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

hasil = cek_anagram(kata_pertama, kata_kedua)

if hasil:
    print(f'"{kata_pertama}" dan "{kata_kedua}" adalah anagram')
else:
    print(f'"{kata_pertama}" dan "{kata_kedua}" bukan anagram')