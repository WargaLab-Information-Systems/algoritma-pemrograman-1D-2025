list_genap = [2, 4, 6, 8]
tuple_ganjil = (1, 3, 5, 7)

list_ganjil = list(tuple_ganjil)

gabungan = list_genap + list_ganjil

jumlah_elemen = len(gabungan)

angka_5 = 5 in gabungan

hasil_ulang = gabungan * 2

print("hasil dari gabungan:", gabungan)
print("total elemen keseluruhan:", jumlah_elemen)
print("angka 5 ada didalam gabungan: ", angka_5)
print("Hasil gabungan jika diulang 2 kali:", hasil_ulang)
