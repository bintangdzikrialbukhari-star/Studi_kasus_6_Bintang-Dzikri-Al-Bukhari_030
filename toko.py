import json
import os

FILE_PATH = "inventaris.json"

def muat_data():
    """Membaca data dari file JSON. Jika file belum ada, kembalikan list kosong."""
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def simpan_data(data_inventaris):
    """Menyimpan data inventaris kembali ke file JSON secara permanen."""
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data_inventaris, file, indent=4)

def tampilkan_barang():
    """Menampilkan seluruh data barang dari file JSON."""
    data = muat_data()
    print("\n" + "="*50)
    print("         DAFTAR INVENTARIS BARANG TOKO")
    print("="*50)
    
    if not data:
        print("Belum ada data barang yang tersimpan.")
    else:
        print(f"{'Kode':<8} | {'Nama Barang':<20} | {'Kategori':<12} | {'Harga':<10} | {'Stok':<5}")
        print("-" * 65)
        for barang in data:
            print(f"{barang['kode_barang']:<8} | {barang['nama_barang']:<20} | {barang['kategori']:<12} | Rp{barang['harga']:<8} | {barang['stok']:<5}")
    print("="*50)

def tambah_barang():
    """Menambahkan data barang baru ke dalam file JSON."""
    print("\n--- Tambah Data Barang Baru ---")
    data = muat_data()
    
    kode_barang = input("Masukkan Kode Barang (misal B004): ").strip()
    
    # Cek apakah kode barang sudah ada
    for b in data:
        if b['kode_barang'].upper() == kode_barang.upper():
            print("⚠️ Kode barang sudah terdaftar! Gunakan kode lain.")
            return

    nama_barang = input("Masukkan Nama Barang: ").strip()
    kategori = input("Masukkan Kategori Barang: ").strip()
    
    try:
        harga = int(input("Masukkan Harga Barang (Rp): "))
        stok = int(input("Masukkan Jumlah Stok: "))
    except ValueError:
        print("⚠️ Input harga dan stok harus berupa angka integer!")
        return

    barang_baru = {
        "kode_barang": kode_barang,
        "nama_barang": nama_barang,
        "kategori": kategori,
        "harga": harga,
        "stok": stok
    }
    
    data.append(barang_baru)
    simpan_data(data)
    print(f"Barang '{nama_barang}' berhasil ditambahkan dan disimpan permanen!")

def main():
    """Fungsi utama program dengan interactive while loop."""
    while True:
        print("\n=== SISTEM MANAJEMEN INVENTARIS BARANG ===")
        print("1. Lihat Seluruh Data Barang")
        print("2. Tambah Data Barang Baru")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ").strip()
        
        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan program inventaris barang!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()