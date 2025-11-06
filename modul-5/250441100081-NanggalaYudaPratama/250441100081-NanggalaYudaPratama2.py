while True:
    def anagram(kata1, kata2):
        kata1 = kata1.replace(" ", "")
        kata2 = kata2.replace(" ", "")

        kata1 = kata1.lower()
        kata2 = kata2.lower()
    
        return sorted(kata1) == sorted(kata2)

    kata_pertama = input("Masukkan kata pertama: ")
    kata_kedua = input("Masukkan kata kedua: ")

    if anagram(kata_pertama, kata_kedua):
        print(f"Kata '{kata_pertama}' dan '{kata_kedua}' adalah anagram")
    else:
        print(f"Kata '{kata_pertama}' dan '{kata_kedua}' bukan anagram")

    lanjut = input("Apakah ingin lanjut (y/n): ")
    if lanjut == "n":
        break