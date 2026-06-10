# Terminal Finance v3.2

Aplikasi web keuangan ringan dengan tampilan terminal dan sinkronisasi ke JSONBin.

## Cara pakai

1. Buka `index.html` di browser Chrome.
2. Aplikasi akan mencoba memuat data dari JSONBin publik.
3. Jika tidak dapat terhubung, gunakan tombol `OFFLINE MODE` untuk menyimpan data di browser.
4. Tambah, sunting, dan hapus transaksi. Gunakan tab `LAPORAN` untuk ekspor.

## Fitur

- Dashboard ringkas dengan grafik
- Pencatatan transaksi masuk/keluar
- Filter riwayat berdasarkan teks, jenis, bulan, dan kategori
- Export data ke Excel, PDF, dan Word
- Sinkronisasi ke JSONBin untuk data bersama
- Offline fallback menggunakan LocalStorage

## Catatan

- Pastikan Chrome menggunakan akses internet saat `JSONBin` aktif.
- Jika ingin menggunakan sebagai file lokal, buka `index.html` langsung di browser.

## GitHub

Repo ini sudah tersedia di: https://github.com/kanza99/terminal-finance-v3

Untuk menghubungkan repo lokal dan mendorong perubahan:

```bash
cd /workspaces/codespaces-blank
git remote add origin https://github.com/kanza99/terminal-finance-v3.git
git branch -M main
git push -u origin main
```
