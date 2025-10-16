#program menentukan kategori umur
umur = int(input("masukkan umur kamu: "))

if umur <= 8:
    print("kamu masih anak-anak")
elif umur <= 15:
    print("kamu sudah remaja")
elif umur <= 25:
    print("kamu sudah dewasa muda")
elif umur <= 35:
    print("kamu sudah dewasa")
elif umur <= 59:
    print("kamu sudah jompo")
else:
    print("kamu sudah lanjut usia") 