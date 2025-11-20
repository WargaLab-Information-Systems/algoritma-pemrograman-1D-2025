set_asli = {"A", "B"}
set_baru = set_asli    # Bukan copy!

set_baru.update({"C"})  # Mengubah set_baru tapi set_asli ikut berubah
print(set_asli)
