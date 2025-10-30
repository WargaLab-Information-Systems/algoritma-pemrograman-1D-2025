print("soal no 1 : menghitung harga setelah pajak " )

harga_buku = int (input ( "masukkan harga buku tulis : " ))
harga_pensil = int (input("masukkan harga pensil : ")) 

jumlah_buku = int (input("masukkan jumlah buku =" )) 
jumlah_pensil = int (input("masukkan jumlah pensil =")) 

total_buku = harga_buku * jumlah_buku
total_pensil = harga_pensil * jumlah_pensil
total_harga = total_buku + total_pensil

pajak = total_harga * 0.10
total_bayar = total_harga + pajak
total_pajak = total_bayar - total_harga 

print("total belanja adalah :" , total_harga)
print ("total diskon adalah : ",total_pajak )
print("total belanja setelah pajak adalah : ", total_bayar) 


