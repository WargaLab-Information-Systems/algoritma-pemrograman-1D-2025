
bk = 3
hrbk = 5000
ps = 2
hrps = 4500
pjk=0.10

total_bk=hrbk*bk
total_ps=hrps*ps
total_semuabrng=total_bk+total_ps

besar_pjk=total_semuabrng*pjk
hasil_pjk=total_semuabrng+besar_pjk

print(f"buku:{bk} x rp {hrbk:,}= rp {total_bk}")
print(f"buku: {ps} x rp {hrps :,} = rp {total_ps}")
print(f"subtotal: rp {total_semuabrng :,}")
print(f"pajak (10%): rp {besar_pjk:,.0f}")
print(f"total yang akan dibayar: rp {hasil_pjk:,.0f} ")