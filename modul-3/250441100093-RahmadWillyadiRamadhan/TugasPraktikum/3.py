kalimat = input("Masukan sebuah kalimat : ")

hurufvokal = "aiueoAIUEO"
vokal = 0
konsonan = 0

kata = len(kalimat.split())  

for huruf in kalimat:
    if huruf.isalpha():
        if huruf in hurufvokal:
            vokal += 1
        else:
            konsonan += 1
            
print(f"Jumlah Kata : {kata}")
print(f"Jumlah Huruf vokal : {vokal}")
print(f"Jumlah Hurud konsonan : {konsonan}")



# Fungsi .split() memecah kalimat menjadi daftar kata berdasarkan spasi.
# Contoh: "Saya suka Python".split() → ["Saya", "suka", "Python"]
# Fungsi len() menghitung berapa banyak kata di dalam daftar tersebut.
# Jadi kata = 3
# Fungsi .isalpha() mengembalikan True jika karakter adalah huruf (A–Z atau a–z).
# Spasi atau tanda baca akan diabaikan karena bukan huruf.