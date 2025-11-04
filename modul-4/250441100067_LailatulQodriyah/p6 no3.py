n = int(input("masukan jumlah baris(n):"))

for i in range (1, n +1): # ditambah +satu untuk menambah  variabel 
    for j in range(1, i+1):
        print(j, end=" ")

    for spasi in range(2 *(n - i)): #2 kali n - i (n= variabel dikurangi i(putaran) di kali 2)
        print(" ", end=" ")

    for k in range (i, 0, -1):#dikasih (-) karna  mundur
        print(k, end=" ")
    
    print()

# n = int(input("masukan jumlah baris(n):"))
``
# for i in range (n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")

#     for spasi in range(2 *(n - i)):
#         print(" ", end=" ")

#     for k in range (i, 0, -1):
#         print(k, end=" ")
    
#     print()

# n = int(input("masukan jumlah baris(n):"))

# for i in range (1, n +1):
#   for spasi in range(n - i):
#         print(" ", end=" ")  
        
#     for j in range(i, 0, -1):
#         print(j, end=" ")

#     for space in range(i - n):
#         print(" ", end=" ") 

#     for k in range (i, 0, -1):
#         print(k, end=" ")
    
#     print()