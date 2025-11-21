def cek_anagram(kata1, kata2):
    
    kata1 = kata1.lower()
    kata2 = kata2.lower()
    
    kata1 = kata1.replace(" ", "")
    kata2 = kata2.replace(" ", "")
    
    
    return sorted(kata1) == sorted(kata2)

kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

hasil = cek_anagram(kata_pertama, kata_kedua)

if hasil:
    print(f"✅ '{kata_pertama}' dan '{kata_kedua}' adalah ANAGRAM.")
else:
    print(f"❌ '{kata_pertama}' dan '{kata_kedua}' BUKAN anagram.")