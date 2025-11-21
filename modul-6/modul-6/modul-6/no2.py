print("PROGRAM PENGGABUNGAN DAN PENGURUTAN TUPLE MAC ALLISTER\n")


while True:
    try:
        data1 = input("Masukkan elemen tuple pertama (pisahkan dengan spasi): ")
        elemen1 = data1
        tuple1 = tuple(int(i) for i in elemen1)
        break
    except:
        print("Input tidak valid! Pastikan hanya memasukkan angka dan dipisahkan dengan spasi.\nSilakan masukkan ulang.\n")

while True:
    try:
        data2 = input("Masukkan elemen tuple kedua (pisahkan dengan spasi): ")
        elemen2 = data2
        tuple2 = tuple(int(i) for i in elemen2)
        break
    except:
        print("Input tidak valid! Pastikan hanya memasukkan angka dan dipisahkan dengan spasi.\nSilakan masukkan ulang.\n")

tuple_gabungan = tuple1 + tuple2

tuple_unik = ()
for angka in tuple_gabungan:
    if angka not in tuple_unik:
        tuple_unik = tuple_unik + (angka,)


tuple_list = list(tuple_unik)
for i in range(len(tuple_list)):
    for j in range(i + 1, len(tuple_list)):
        if tuple_list[i] < tuple_list[j]:
            temp = tuple_list[i]
            tuple_list[i] = tuple_list[j]
            tuple_list[j] = temp

hasil_akhir = tuple(tuple_list)

print("\nTuple pertama:", tuple1)
print("Tuple kedua:", tuple2)
print("Tuple gabungan tanpa duplikat (descending):", hasil_akhir)