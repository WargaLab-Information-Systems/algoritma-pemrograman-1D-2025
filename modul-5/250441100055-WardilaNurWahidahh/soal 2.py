def hapus_spasi_manual(teks):
    hasil = ""
    for huruf in teks:
        if huruf != " ":
            hasil += huruf
    return hasil


def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()

    kata1 = hapus_spasi_manual(kata1)
    kata2 = hapus_spasi_manual(kata2)

    if sorted(kata1) == sorted(kata2):
        return True
    else:
        return False


print("=== Program Pengecekan Anagram ===")
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

hasil = cek_anagram(kata1, kata2)

if hasil:
    print(f"'{kata1}' dan '{kata2}' adalah anagram.")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram.")