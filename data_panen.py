# Data hasil panen
data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {
            "padi": 1200,
            "jagung": 800,
            "kedelai": 500
        }
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {
            "padi": 1500,
            "jagung": 900,
            "kedelai": 450
        }
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {
            "padi": 1100,
            "jagung": 750,
            "kedelai": 600
        }
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {
            "padi": 1300,
            "jagung": 850,
            "kedelai": 550
        }
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {
            "padi": 1400,
            "jagung": 950,
            "kedelai": 480
        }
    }
}

# 1. Tampilkan semua data
print("Semua data panen:")
for lokasi in data_panen:
    nama = data_panen[lokasi]["nama_lokasi"]
    hasil = data_panen[lokasi]["hasil_panen"]
    print(f"{lokasi} - {nama}: {hasil}")
print()

# 2. Jumlah panen jagung di lokasi2
jagung_lokasi2 = data_panen["lokasi2"]["hasil_panen"]["jagung"]
print(f"Jumlah jagung di lokasi2: {jagung_lokasi2}")
print()

# 3. Nama lokasi dari lokasi3
nama_lokasi3 = data_panen["lokasi3"]["nama_lokasi"]
print(f"Nama lokasi3: {nama_lokasi3}")
print()

# 4. Masukkan hasil padi dan kedelai ke variabel baru
hasil_padi = {lokasi: data_panen[lokasi]["hasil_panen"]["padi"] for lokasi in data_panen}
hasil_kedelai = {lokasi: data_panen[lokasi]["hasil_panen"]["kedelai"] for lokasi in data_panen}
print(f"Hasil padi: {hasil_padi}")
print(f"Hasil kedelai: {hasil_kedelai}")
print()

# 5. Cek lokasi yang butuh perhatian
for lokasi in data_panen:
    padi = data_panen[lokasi]["hasil_panen"]["padi"]
    jagung = data_panen[lokasi]["hasil_panen"]["jagung"]
    nama = data_panen[lokasi]["nama_lokasi"]
    if padi > 1300 or jagung > 800:
        print(f"{nama} perlu perhatian khusus!")
    else:
        print(f"{nama} dalam kondisi baik.")
print()

# 6. Push ke GIT
# Sayangnya ini nggak bisa langsung dilakukan dari script ini,
# tapi cara simpelnya:
# 1. Simpan file ini, misalnya `data_panen.py`
# 2. Gunakan command berikut di terminal/git bash:
#    git add data_panen.py
#    git commit -m "Tambah kode untuk olah data panen"
#    git push

print("Kode selesai! Jangan lupa push ke GIT yaaa! ✨")
