def cek_anagram(kata_satu, kata_dua):
    kata_satu = kata_satu.replace(" ", "").lower()
    kata_dua = kata_dua.replace(" ", "").lower()

    return sorted(kata_satu) == sorted(kata_dua)

kata_satu = input("Masukkan kata first: ")
kata_dua = input("Masukkan kata second: ")

if cek_anagram(kata_satu, kata_dua):
    print(f"'{kata_satu}' dan '{kata_dua}' adalah anagram!")
else:
    print(f"'{kata_satu}' dan '{kata_dua}' BUKAN anagram.")