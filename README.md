# Pertemuan 06 Nested Loop Python

Nama: Ririn Setiarini
NIM: 2225250159
Kelas: 3F

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan dalam Python.

## Cara Menjalankan
Jalankan program melalui terminal VS Code:

python tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
Loop luar digunakan untuk menentukan baris, sedangkan loop dalam digunakan untuk menentukan kolom.

Variabel total_baris digunakan untuk menghitung jumlah setiap baris.
Variabel total_semua digunakan untuk menghitung seluruh hasil perkalian.
Variabel count_genap digunakan untuk menghitung banyak hasil perkalian genap.

## Hasil Pengujian

| Input n | Total semua | Hasil genap | Status |
|---|---:|---:|---|
| 1 | 1 | 0 | Berhasil |
| 2 | 9 | 3 | Berhasil |
| 3 | 36 | 5 | Berhasil |

## Analisis Efisiensi
Untuk input n positif, loop dalam dijalankan sebanyak n kali pada setiap iterasi loop luar. Dengan demikian, jumlah iterasi badan loop dalam adalah n x n atau n² kali.

## Refleksi
Kesalahan yang perlu dihindari adalah menempatkan inisialisasi akumulator pada lokasi yang salah. total_baris harus direset pada setiap baris, sedangkan total_semua tetap diinisialisasi sebelum kedua loop.