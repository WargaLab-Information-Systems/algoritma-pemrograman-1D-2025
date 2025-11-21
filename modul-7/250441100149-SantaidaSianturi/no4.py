klub_basket  = {"santa, budi,ria" }
klub_renang  = {"lala, budi,ani" }

siswa_kedua_club = klub_basket.intersection("santa, budi,ria")
print("siswa yang mengikuti kedua club:","santa, budi,ria")
siswa_kedua_club = klub_basket.intersection(klub_renang)
print("siswa yang mengikuti satu club:" "ala, budi,ani")

siswa_unik = klub_basket.union(klub_renang)
print ("siswa yang mengikuti club unik:",siswa_unik)

jumlah_siswa_unik = len(siswa_unik)
print("jumlah siswa yang mengikuti club unik:",jumlah_siswa_unik)



