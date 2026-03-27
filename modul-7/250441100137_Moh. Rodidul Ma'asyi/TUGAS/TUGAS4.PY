klub_basket = {"radit", "anam", "rifki"}
klub_renang = {"dani", "sukron", "ilham", "radit", "rifki"}

ikut2klub = klub_basket.intersection(klub_renang)

ikut1klub = klub_basket.difference(klub_renang)

semua = klub_basket.union(klub_renang)

print("siswa yang mengikuti 2 klub langsung", semua)
print("siswa yang ikut 1 klub", ikut1klub)
print("siswa yang sebagian ikut di 2 klub", ikut2klub)