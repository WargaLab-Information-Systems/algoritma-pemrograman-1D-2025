print("\nPROGRAM PENGGABUNGAN DUA KUMPULAN ANGKA DAN PENGURUTANNYA (TERBESAR KE TERKECIL) DALAM TUPLE\n")

while True:
    try:
        data1 = input("Masukkan elemen tuple pertama (jangan lupa untuk pisahkan dengan spasi): ")
        elemen1 = data1.split()
        tuple1 = tuple(int(i) for i in elemen1)
        break
    except:
        print("Input tidak valid! Pastikan hanya memasukkan angka dan dipisahkan dengan spasi.\nSilakan masukkan ulang.\n")

while True:
    try:
        data2 = input("Masukkan elemen tuple kedua (jangan lupa untuk pisahkan dengan spasi): ")
        elemen2 = data2.split()
        tuple2 = tuple(int(i) for i in elemen2)
        break
    except:
        print("Input tidak valid! Pastikan hanya memasukkan angka dan dipisahkan dengan spasi.\nSilakan masukkan ulang.\n")

tuple_gabungan = tuple1 + tuple2

tuple_tanpa_duplikat = ()
for angka in tuple_gabungan:
    if angka not in tuple_tanpa_duplikat:
        tuple_tanpa_duplikat = tuple_tanpa_duplikat + (angka,)

tuple_list = list(tuple_tanpa_duplikat)
for i in range(len(tuple_list)):
    for j in range(i + 1, len(tuple_list)):
        if tuple_list[i] < tuple_list[j]:
            tukar = tuple_list[i]
            tuple_list[i] = tuple_list[j]
            tuple_list[j] = tukar

hasil_akhir = tuple(tuple_list)

print("\nTuple Pertama:", tuple1)
print("Tuple Kedua:", tuple2)
print("Tuple Gabungan tanpa angka yang sama (duplikat) dan secara menurun (descending):", hasil_akhir)
print()