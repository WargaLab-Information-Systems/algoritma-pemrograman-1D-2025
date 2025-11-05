print("program menentukan dua kata apakah anagram atau tidak\n")

def cek_anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    
    return sorted(kata1) == sorted(kata2)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if cek_anagram(kata1, kata2):
    print("Kedua kata tersebut merupakan anagram!")
else:
    print("Kedua kata tersebut bukan anagram.")

