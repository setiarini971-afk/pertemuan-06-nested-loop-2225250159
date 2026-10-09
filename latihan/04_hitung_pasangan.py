# Meminta nilai n
n = int(input("Masukkan n: "))

# Menghitung banyak pasangan yang memenuhi syarat
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):

        # Memeriksa kondisi pasangan
        if i + j <= n:
            count += 1

# Menampilkan jumlah pasangan
print(f"Banyak pasangan = {count}")