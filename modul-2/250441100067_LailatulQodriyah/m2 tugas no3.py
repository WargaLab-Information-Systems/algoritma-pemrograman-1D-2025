#menghitung biaya perkir di mall
#input lama parkir
lama_parkir = int (input("masukan lama parkir (jam):"))

#input status
status_vip = input("apakah anda member vip?(ya/tidak):")

#jika vip, biaya parkir gratis
if status_vip == "ya":
    total_biaya = 0
    print(f"total biaya : Rp {total_biaya}")
else:
    #tarif dasar
    if lama_parkir <=2:
        total_biaya =5000
    else:
        total_biaya = 5000 + (lama_parkir - 2)*3000

    #batas maksimal tarif perhari
    if total_biaya > 20000:
        total_biaya = 20000
    #output hasil
    print("=== RINCIAN BIAYA PARKIR===")
    print(f"lama parkir : {lama_parkir}jam")
    print(f"status vip : {status_vip}")
    print(f"total biaya : Rp{total_biaya}")