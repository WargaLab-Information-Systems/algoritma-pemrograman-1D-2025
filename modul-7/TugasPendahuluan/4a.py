data_asli = {"nama": "Andi", "nilai": 90}
data_salinan = data_asli   # KELIRU! Tidak membuat copy

data_salinan.update({"nilai": 60})   # Mengubah salinan
print("Data asli:", data_asli)
