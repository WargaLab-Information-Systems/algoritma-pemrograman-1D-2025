# Data peserta
pendaftar = {"Andi", "Budi", "Citra", "Dewi", "Eka"}
hadir = {"Andi", "Citra", "Eka"}
bentrok_jadwal = {"Budi"}

# UNION: Semua yang terlibat
semua_peserta = pendaftar 
print("Semua yang terlibat:", semua_peserta)

# INTERSECTION: Pendaftar yang hadir
peserta_hadir = pendaftar & hadir
print("Pendaftar yang hadir:", peserta_hadir)

# DIFFERENCE: Pendaftar yang tidak hadir
tidak_hadir = pendaftar - hadir
print("Pendaftar yang tidak hadir:", tidak_hadir)

# Pendaftar yang TIDAK diperbolehkan ikut (karena bentrok jadwal)
pendaftar_ditolak = pendaftar & bentrok_jadwal
print("Pendaftar yang tidak diperbolehkan ikut:", pendaftar_ditolak)

# Pendaftar yang diperbolehkan ikut
pendaftar_diperbolehkan = pendaftar - bentrok_jadwal
print("Pendaftar yang diperbolehkan ikut:", pendaftar_diperbolehkan)
