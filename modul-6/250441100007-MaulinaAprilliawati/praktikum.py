# #list
# list = [1, 2, 3, 'zaki']
# print(list)

#  #menambah nilai pda list
# list.append('apel')
# print(list)

#menghapus list
# list = [1, 2, 3, 'apel']
# # list.remove('apel')
# del list[3]
# print(list)

#operasi dasar pada list

#menghitung panjang list
# angka = [10,20,30,40,50]
# print("panjang list = ", len(angka))

#menggabungkan dua list
# list1 = [1,2,3,4]
# list2 = [2,3,4,5]
# print("menggabungkan dua list = ", list1 + list2)

#perulangan pada list
# list = ['mangga']
# print(list * 20)

#mengecek elemen didalam list
# list = [1,2,3,4, 'buah']
# print('buah' in list)
# print(15 in list)

#perulangan dalam list

#perulangan for
# for x in [1,2,3]:
#     print(x)

# #perulangan while
# angka = [1,2,3]
# i = 0
# while i < len(angka):
#     print(angka[i], end=' ')
#     i += 1

#tuple
#mengakses nilai pada tuple
# orang = ('zaki', 'wahyu', 'adit', 'dika')
# print(orang[3])

# buah = ('mangga', 'apel', 'jeruk', 'durian')
# buahbaru = buah + ('anggur',)
# print(buahbaru)

#menghapus nilai pada tuple
# buah1 = ('jeruk', 'manggis')
# buah2 = ('apel', 'mangga')
# del buah1
# print(buah2)

mahasiswa = ('zaki', 'wahyu', 'adit', 'dika')
mahasiswa_baru = mahasiswa + ('rani',)
print(mahasiswa_baru)
print("Total mahasiswa setelah penambahan:", len(mahasiswa_baru))



