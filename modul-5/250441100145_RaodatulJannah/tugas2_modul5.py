def cek_anagram(kata1, kata2):
    kata1 = kata1.replace(" ","").lower()
    kata2 = kata2.replace(" ","").lower()
    
    if kata1 == kata2:
        return False

    if sorted(kata1) == sorted(kata2):
        return True
    else:
        return False
    

kata1 = (input("masukkan kata pertama: "))
kata2 = (input("masukkan kata kedua: "))

hasil = cek_anagram(kata1, kata2)
print(f"hasil dari cek anagram adalah:{hasil}")

if cek_anagram(kata1, kata2):
    print(f"{kata1} dan {kata2} merupakan anagram")
else:
    print(f"{kata1} dan {kata2} bukan anagram ")