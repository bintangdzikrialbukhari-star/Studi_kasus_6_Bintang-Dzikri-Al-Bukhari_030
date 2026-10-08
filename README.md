# Studi_kasus_6_Bintang-Dzikri-Al-Bukhari_030

# Program Sistem Manajemen Inventaris

**Nama:** Bintang Dzikri Al Bukhari  
**NIM:** 26091106030  
**Prodi:** Sistem Informasi  

## Tentang Program Ini
Program ini dibuat untuk mengelola data inventaris barang pada toko kelontong secara otomatis menggunakan file JSON (`fery.json`). Pengguna dapat menampilkan daftar barang yang tersimpan dalam format tabel serta menambahkan barang baru secara interaktif. Setiap perubahan data akan langsung tersimpan secara permanen ke dalam file JSON agar data tidak hilang saat program ditutup.

## Yang Ada di Dalam Program

- **Modular Functions (def)** = Dipakai untuk membagi logika program menjadi beberapa fungsi utama seperti `baca_data()`, `simpan_data()`, `tampilkan_barang()`, `tambah_barang()`, dan `main()` agar kode lebih rapi dan terstruktur.
- **File Handling & JSON Manipulation (`json.load`, `json.dump`, `open()`)** = Dipakai untuk membaca data dari file `fery.json` dan menyimpan pembaruan data inventaris dalam format teks JSON yang rapi (`indent=4`).
- **Error Handling (`try-except`)** = Dipakai untuk menangani error jika file JSON belum ada / rusak (`FileNotFoundError`, `JSONDecodeError`) serta mencegah program *crash* jika pengguna memasukkan input stok atau harga yang bukan berupa angka (`ValueError`).
- **Control Flow & Loops (`while True`, `if-elif-else`)** = Dipakai untuk menjalankan menu navigasi interaktif berbasis teks secara berulang hingga pengguna memilih menu keluar.
- **Formatted String & Print Formatting (`f-string`)** = Dipakai untuk menampilkan tabel daftar inventaris secara rapi dan presisi menggunakan *alignment padding* (seperti `:<8`, `:<20`, `:<6`).
- **List & Dictionary** = Dipakai sebagai struktur data utama di dalam program, di mana setiap barang disimpan dalam bentuk `dictionary` (berisi kode, nama, stok, dan harga) lalu dikumpulkan di dalam `list`.

## Hasil Output Pada Program

### Menu awal
<img width="407" height="108" alt="Screenshot 2026-10-08 173941" src="https://github.com/user-attachments/assets/74d018f6-60d6-4d0f-a7c2-c09719d31d9c" />

Berikut ini adalah output awal program yang dapat dilihat oleh user sebelum memilih ingin mengaktifkan program ke 1, 2, 3.

### Output Pilihan 1
<img width="477" height="193" alt="Screenshot 2026-10-08 172652" src="https://github.com/user-attachments/assets/c3aeb6d7-d20f-48d1-8335-a7a86e42c3c5" />

Berikut ini adalah hasil output tampilan menu 1 yang menampilkan semua barang yang di json.

### Output Pilihan 2
<img width="582" height="161" alt="Screenshot 2026-10-08 172711" src="https://github.com/user-attachments/assets/f1d53b8e-b2f7-4a70-9a18-4151e09ae9ce" />

Berikut ini adalah hasil output tampilan menu 2 dimana pengguna bisa menambahkan stock di json.

### Output Pilihan 3

Berikut ini adalah hasil output tampilan menu 3 dimana user bisa menghentikan program.

## Bukti Data Tersimpan

### Py
<img width="472" height="287" alt="image" src="https://github.com/user-attachments/assets/202dc887-1b89-408b-92af-93732b270f9d" />

Itu adalah jenis barang baru yang saya tambbahkan di terminal.

### JSON
<img width="393" height="597" alt="image" src="https://github.com/user-attachments/assets/6db50bf9-e6d4-4934-a72d-4eb3e0390b16" />

Itu adalah hasil dari data yang saya masukan dari terminal.
