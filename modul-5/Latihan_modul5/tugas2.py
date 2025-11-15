def cek_anagram(kata1, kata2):
    if len(kata1) != len(kata2):
        return False

    cocok = 0
    for huruf in kata1:
        for huruf2 in kata2:
            if huruf == huruf2:
                cocok += 1
                break
    return cocok == len(kata1)

def huruf_saja(teks):
    for c in teks:
        if not ('a' <= c <= 'z'):
            return False
    return True

k1 = input("Masukkan kata pertama: ")
k2 = input("Masukkan kata kedua: ")

if not (huruf_saja(k1) and huruf_saja(k2)):
    print("Input hanya boleh huruf tanpa angka atau spasi!")
elif cek_anagram(k1, k2):
    print("Kedua kata adalah anagram.")
else:
    print("Kedua kata bukan anagram.")