print("=================================================")
print("=================================================")
print("==PROGRAM GABUNG 2 TUPLE (TERBESAR KE TERKECIL)==\n")

while True:
    try:
        satu1 = input("Masukkan elemen tuple pertama (pisahkan dengan spasi): ")
        list_angka1 = satu1.split()
        tuple1 = tuple(int(i) for i in list_angka1)
        break
    except:
        print("Ups! input salah. Pastikan cuma angka dan pastikan pakai spasi\nSilakan masukkan ulang.\n")

while True:
    try:
        dua2 = input("Masukkan elemen tuple kedua (pisahkan dengan spasi): ")
        list_angka2 = dua2.split()
        tuple2 = tuple(int(i) for i in list_angka2)
        break
    except:
        print("Masih salah. Isi cuma angka aja dan pisahkan dengan spasi\n")

mix = tuple1 + tuple2

tanpa_kembar = ()
for angka in mix:
    if angka not in tanpa_kembar:
        tanpa_kembar = tanpa_kembar + (angka,)

tuple_list = list(tanpa_kembar)
for i in range(len(tuple_list)):
    for j in range(i + 1, len(tuple_list)):
        if tuple_list[i] < tuple_list[j]:
            tukar = tuple_list[i]
            tuple_list[i] = tuple_list[j]
            tuple_list[j] = tukar

hasil_akhir = tuple(tuple_list)

print("\nDeret Pertama:", satu1)
print("Deret Kedua:", dua2)
print("Hasil akhirnya (tanpa angka kembar & urut menurun / descending): ", hasil_akhir)
print()