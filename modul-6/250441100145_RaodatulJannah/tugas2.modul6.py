print("=== Program Gabung Dua Tuple ===")

t1_input = input("Masukkan angka untuk tuple pertama: ")
t2_input = input("Masukkan angka untuk tuple kedua: ")


gabung = t1_input + t2_input

unik = []
for angka in gabung:
    if angka not in unik:
        unik.append(angka)

hasil_urut = []
while len(unik) > 0:
    terbesar = unik[0]
    for a in unik:
        if int(a) > int(terbesar):
            terbesar = a
    hasil_urut.append(terbesar)
    unik.remove(terbesar)

hasil = tuple(int(x) for x in hasil_urut)

print("Hasil akhir:", hasil)