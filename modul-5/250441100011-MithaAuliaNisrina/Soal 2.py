print ("Program Menentukan Dua Kata Anagram atau Bukan\n")

def cek_anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    
    if kata1 == kata2:
        return False
    
    if sorted(kata1) == sorted(kata2):
        return True
    else:
        return False
    
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

hasil = cek_anagram(kata1, kata2)
print ("Hasil Fungsi:", hasil)

if cek_anagram(kata1, kata2):
    print("Kedua kata antara", kata1, "dan", kata2, "tersebut merupakan anagram.")
else:
    print("Kedua kata antara", kata1, "dan", kata2, "tersebut bukan anagram.")