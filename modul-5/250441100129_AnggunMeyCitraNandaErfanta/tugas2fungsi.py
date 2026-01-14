def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()

    if sorted(kata1) == sorted(kata2):
        return True
    else:
        return False
    
print("=== Program Mengecek Anagram ===")
print()

kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

hasil = cek_anagram(kata_pertama, kata_kedua)

if hasil:
    print("hasil: kedua kata merupakan anagram")
else:
    print("hasil: kedua kata bukan anagram")