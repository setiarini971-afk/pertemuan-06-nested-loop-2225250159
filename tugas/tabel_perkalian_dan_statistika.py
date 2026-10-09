print("Tabel Perkalian dan Statistik")

# Meminta input n
n = int(input("n: "))

# Validasi agar n harus positif
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# Inisialisasi total keseluruhan dan counter genap
total_semua = 0
count_genap = 0

# Loop luar untuk baris
for i in range(1, n + 1):

    # Reset jumlah setiap baris
    total_baris = 0

    # Loop dalam untuk kolom
    for j in range(1, n + 1):

        # Menghitung hasil perkalian
        hasil = i * j

        # Menampilkan isi tabel
        print(f"{hasil:4}", end="")

        # Menghitung jumlah baris dan total keseluruhan
        total_baris += hasil
        total_semua += hasil

        # Menghitung banyak hasil genap
        if hasil % 2 == 0:
            count_genap += 1

    # Dilakukan setelah satu baris selesai
    print(f"   | jumlah baris = {total_baris}")

# Menampilkan statistik keseluruhan
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")