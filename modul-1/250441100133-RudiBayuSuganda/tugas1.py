print("=="*20)
print()
print("           Tugas Pertama")
print("=="*20)
buku_tulis=5000
pensil=4500
harga_buku=buku_tulis*3
harga_pensil=pensil*2
pajak=0.10
total_harga=harga_buku+harga_pensil
tarif_pajak=total_harga*pajak
total_bayar=total_harga+tarif_pajak
print("    Harga Awal ",harga_buku,"+",harga_pensil,"=",total_harga)
print("    Pajak      ",total_harga,"x 10%  =",int(tarif_pajak))
print("    Total Bayar",total_harga,"+",int(tarif_pajak),"=",int(total_bayar))

print("=="*20)
