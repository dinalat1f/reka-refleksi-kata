def solusi_reflektif(perasaan):
    respon = {
        "insecure": """Kamu merasa nggak cukup baik? Itu wajar banget. Tapi ingat, kamu berkembang setiap harinya, meskipun nggak kelihatan secara instan. Bandingkan dirimu dengan dirimu yang dulu, bukan orang lain.""",

        "capek": """Kalau kamu capek, itu tandanya kamu sudah berjuang. Istirahat itu bukan malas, tapi bagian dari merawat diri. Ambil waktu sebentar untuk bernapas, kamu berhak merasa tenang.""",

        "gagal": """Gagal itu bukan akhir, tapi bagian dari proses. Banyak orang hebat juga jatuh sebelum berdiri kokoh. Jangan takut gagal, takutlah kalau kamu berhenti mencoba.""",

        "bingung": """Kalau kamu lagi bingung, itu artinya kamu sedang dalam proses mencari arah. Ambil waktu untuk mengenal dirimu. Tanyakan: 'Apa yang sebenarnya penting buatku?' Jawabannya akan datang perlahan."""
    }

    return respon.get(perasaan.lower(), "Maaf, aku belum punya refleksi untuk perasaan itu. Tapi kamu tidak sendiri.")

def reka_refleksi():
    print("🧠 Reka Refleksi – Temukan makna di balik perasaanmu 🌿")
    print("Pilih perasaan yang sedang kamu alami:")
    print("1. Insecure\n2. Capek\n3. Gagal\n4. Bingung")
    
    pilihan = input("Masukkan pilihan kamu (1/2/3/4): ")

    mapping = {
        "1": "insecure",
        "2": "capek",
        "3": "gagal",
        "4": "bingung"
    }

    perasaan = mapping.get(pilihan, None)

    if perasaan:
        print("\nRefleksi untuk kamu yang sedang merasa", perasaan + ":\n")
        print(solusi_reflektif(perasaan))
    else:
        print("Pilihan tidak valid. Silakan jalankan ulang dan pilih antara 1 sampai 4.")

# Jalankan program
reka_refleksi()
