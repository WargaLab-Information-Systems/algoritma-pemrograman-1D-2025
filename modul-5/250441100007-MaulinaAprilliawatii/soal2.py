# Fungsi untuk mengecek apakah dua kata merupakan anagram
def cek_anagram(kata1, kata2):
    # Ubah kedua kata menjadi huruf kecil dan hilangkan spasi
    kata1 = kata1.lower().replace(" ", "")
    kata2 = kata2.lower().replace(" ", "")

    if kata1 == kata2:
        return False
    return sorted(kata1) == sorted(kata2)

# Program utama
kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

# Panggil fungsi dan tampilkan hasil
if cek_anagram(kata_pertama, kata_kedua):
    print(f"✅ '{kata_pertama}' dan '{kata_kedua}' adalah anagram!")
else:
    print(f"❌ '{kata_pertama}' dan '{kata_kedua}' bukan anagram.")
