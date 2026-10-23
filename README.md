# Pertemuan 10 - String dan Pengolahan Teks

Nama: Iqhsan Saleh  
NIM: 2225250021  
Kelas: 3A

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan

```bash
python3 tugas/normalisasi_data_mahasiswa.py
```

## Algoritma

1. Program membaca nama lengkap dan kode kelas dari pengguna.
2. Nama dibersihkan dari spasi di awal dan akhir menggunakan `.strip()`, lalu diformat menjadi title case dengan `.title()`.
3. Nama yang sudah bersih dipecah menjadi kata-kata menggunakan `.split()`. Inisial dibentuk dari karakter pertama setiap kata, diubah ke huruf kapital dengan `.upper()`, lalu digabungkan.
4. Jumlah kata dihitung dari banyaknya elemen dalam daftar kata nama.
5. Kode kelas dibersihkan dari spasi di awal dan akhir, diubah menjadi huruf kapital, dipecah berdasarkan spasi, lalu digabungkan kembali dengan tanda hubung (`-`).
6. Program mencetak nama, kode kelas, jumlah kata, dan inisial hasil normalisasi.

## Test Case

| Input Nama | Input Kode | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| `aan hendrayana` | `pmat a 2026` | `Aan Hendrayana` / `PMAT-A-2026` / `AH` | `Aan Hendrayana` / `PMAT-A-2026` / `AH` | Valid / Sesuai |
| `fATHIYYAH mUTHMAINNAH` | `kelas b` | `Fathiyyah Muthmainnah` / `KELAS-B` / `FM` | `Fathiyyah Muthmainnah` / `KELAS-B` / `FM` | Valid / Sesuai |
| `BUDI` | `pmtk 01` | `Budi` / `PMTK-01` / `B` | `Budi` / `PMTK-01` / `B` | Valid / Sesuai |
| `siti nur aisyah` | `kelas c` | `Siti Nur Aisyah` / `KELAS-C` / `SNA` | `Siti Nur Aisyah` / `KELAS-C` / `SNA` | Valid / Sesuai |
| `  dewi anggraeni  ` | `  pmat   a  2026  ` | `Dewi Anggraeni` / `PMAT-A-2026` / `DA` | `Dewi Anggraeni` / `PMAT-A-2026` / `DA` | Valid / Sesuai |
| `rudi hartono wijaya` | `informatika 03` | `Rudi Hartono Wijaya` / `INFORMATIKA-03` / `RHW` | `Rudi Hartono Wijaya` / `INFORMATIKA-03` / `RHW` | Valid / Sesuai |

## Refleksi

Masalah teks yang sering ditemukan pada input pengguna adalah inkonsistensi penggunaan huruf besar dan kecil, serta spasi berlebih di antara kata atau di awal dan akhir input. Masalah tersebut dapat ditangani dengan metode string bawaan Python seperti `.strip()` untuk merapikan tepi, `.title()` untuk menstandardisasi kapitalisasi nama, serta `.split()` dan `.join()` untuk merapikan spasi dan pemisah antar kata pada kode kelas.
