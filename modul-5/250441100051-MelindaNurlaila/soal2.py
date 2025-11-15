def cek_anagram(kata1, kata2): 
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    
    if sorted(kata1) == sorted(kata2):
        return True
    else:
        return False

kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

hasil = cek_anagram(kata_pertama, kata_kedua)
print(f"Hasil fungsi : {hasil}")

if hasil:
    print(f"'{kata_pertama}' dan '{kata_kedua}' adalah anagram!")
else:
    print(f"'{kata_pertama}' dan '{kata_kedua}' bukan anagram.")

    # saya
    # yaaas
    # 1 (aasy)
    #  2 (aaasy)
    # false