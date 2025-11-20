nilai_mahasiswa = {
    "Andi": 85,
    "Budi": 90,
    "Citra": 78,
    "Dewi": 92
}

nilai_tertinggi = max(nilai_mahasiswa.values())
mahasiswa_tertinggi = [nama for nama, nilai in nilai_mahasiswa.items() 
                       if nilai == nilai_tertinggi]

rata_rata = sum(nilai_mahasiswa.values()) / len(nilai_mahasiswa)

print("Mahasiswa dengan nilai tertinggi:", mahasiswa_tertinggi)
print("Nilai tertinggi:", nilai_tertinggi)
print("Rata-rata nilai:", rata_rata)
