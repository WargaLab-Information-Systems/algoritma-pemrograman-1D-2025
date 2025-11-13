# def input_tuple(nama):
#     while True:
#         data = input(f"Masukkan angka untuk {nama} (pisahkan dengan spasi): ").split()
#         try:
#             angka = tuple(map(int, data))
#             return angka
#         except ValueError:
#             print("Input hanya boleh berisi angka! Ulangi lagi.\n")
# t1 = input_tuple("tuple 1")
# t2 = input_tuple("tuple 2")

# gabung = t1 + t2

# unik = []
# for angka in gabung:
#     if angka not in unik:
#         unik.append(angka)
# for i in range(len(unik)):
#     for j in range(i + 1, len(unik)):
#         if unik[i] < unik[j]:
#             unik[i], unik[j] = unik[j], unik[i]
# hasil = tuple(unik)
# print("Hasil:", hasil)