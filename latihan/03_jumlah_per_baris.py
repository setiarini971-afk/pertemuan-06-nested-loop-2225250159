# Loop luar untuk menentukan baris
for i in range(1, 5):

    # Mengatur ulang jumlah pada setiap baris
    total_baris = 0

    # Loop dalam untuk menghitung hasil perkalian
    for j in range(1, 4):
        total_baris += i * j

    # Menampilkan jumlah setiap baris
    print(f"Jumlah baris {i} = {total_baris}")