#  #perulangan bersarang (nested loop)
#  n = int(input("masukkan jumlah baris yang diinginkan:"))

#  for i in range(1, n+1):
#      for j in range (1, i+1):
#          print (j, end="")
#      print()


# # #pola matemtika dalam perulangan 
# print("deret fibonacci")
#  n = int(input("masukkan batas akhir deret fibonacci yang diinginkan:"))



# #contoh lain nested loop
# n = int(input("masukkan angka: "))

# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" ", end= " ")
#     for k in range(1, i+1):
#         print(k, end= " ")
#     for l in range(i - 1, 0, -1):
#         print(l, end= " ")
#     print()

# # n = int(input("masukkan: "))
# for i in range(n, 0, -1):
#     for j in range (1, i):
#         print(j, end= " ")
#     print()