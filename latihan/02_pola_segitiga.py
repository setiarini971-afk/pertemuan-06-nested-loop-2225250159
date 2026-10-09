# Meminta jumlah baris
n = int(input("Masukkan n: "))

# Loop luar untuk menentukan baris
for i in range(1, n + 1):

    # Loop dalam untuk mencetak bintang
    for j in range(i):
        print("*", end=" ")

    # Pindah ke baris berikutnya
    print()