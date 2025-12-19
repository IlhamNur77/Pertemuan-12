# Sistem Validasi Registrasi Mahasiswa (SOLID)

## Deskripsi Proyek

Proyek ini merupakan bagian dari **Praktikum Pemrograman Berorientasi Objek (PBO)** pada **Pertemuan 12**. Tujuan utama proyek adalah menerapkan prinsip **SOLID** pada studi kasus **Sistem Validasi Registrasi Mahasiswa**, serta melengkapi proyek dengan **dokumentasi (Docstring)**, **logging**, dan **version control menggunakan GitHub**.

---

## Tujuan Pembelajaran

1. Menerapkan prinsip **Single Responsibility Principle (SRP)**
2. Menerapkan prinsip **Open Closed Principle (OCP)**
3. Menerapkan prinsip **Dependency Inversion Principle (DIP)**
4. Mengimplementasikan **Docstring Google Style**
5. Mengganti `print()` dengan **logging**
6. Menggunakan **Git & GitHub** sebagai version control

---

## Struktur Proyek

```
PBO_Praktikum/
└── Pertemuan_12/
    ├── pertemuan_12.py
    ├── README.md
```

---

## Desain Sistem (SOLID)

### 1. Single Responsibility Principle (SRP)

Setiap class memiliki satu tanggung jawab utama:

* `Student` → menyimpan data mahasiswa
* `SksLimitRule` & `PrerequisiteRule` → validasi aturan
* `RegistrationService` → mengoordinasikan proses registrasi

### 2. Open Closed Principle (OCP)

Sistem dapat diperluas dengan menambahkan aturan validasi baru tanpa mengubah kode pada `RegistrationService`.

### 3. Dependency Inversion Principle (DIP)

`RegistrationService` bergantung pada abstraksi `IValidationRule`, bukan pada implementasi konkret.

---

## Implementasi Logging

Sistem menggunakan modul `logging` Python untuk mencatat proses validasi:

* `logging.info()` → proses berhasil
* `logging.warning()` → validasi gagal

Logging digunakan untuk meningkatkan keterbacaan, debugging, dan profesionalitas kode.

---

## Cara Menjalankan Program

1. Pastikan Python telah terinstal
2. Masuk ke folder proyek:

   ```bash
   cd PBO_Praktikum/Pertemuan_12
   ```
3. Jalankan program:

   ```bash
   python pertemuan_12.py
   ```

---

## Version Control

Pengelolaan versi dilakukan menggunakan **Git** dan **GitHub** melalui **Visual Studio Code**.

### Contoh Commit Message:

```
Feat: Implementasi SOLID RegistrationService
Docs: Add Docstrings and Logging
```

---

## Kesimpulan

Melalui proyek ini, prinsip SOLID berhasil diterapkan untuk meningkatkan kualitas desain perangkat lunak. Penggunaan Docstring, logging, dan version control mendukung pengembangan kode yang lebih terstruktur, mudah dipelihara, dan sesuai dengan praktik profesional.

---

