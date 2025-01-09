Face Detection with YOLOv8 and OpenCV
Repository ini berisi script Python untuk mendeteksi wajah dalam sebuah gambar menggunakan YOLOv8 dari library Ultralytics dan OpenCV. Proyek ini dirancang untuk memberikan bounding box pada setiap wajah yang terdeteksi dan menampilkan hasilnya menggunakan Matplotlib.

Fitur Utama
Deteksi wajah dalam gambar dengan akurasi tinggi menggunakan model YOLOv8.
Penandaan wajah dengan bounding box menggunakan OpenCV.
Visualisasi hasil deteksi dengan Matplotlib.
Instalasi
Persyaratan
Pastikan Anda telah menginstal Python 3.8 atau versi yang lebih baru. Untuk library yang diperlukan, Anda bisa menginstalnya dengan perintah berikut:

bash
Salin kode
pip install ultralytics opencv-python matplotlib
Cara Penggunaan
Clone Repository
Clone repository ini ke komputer Anda:

bash
Salin kode
git clone https://github.com/username/repository-name.git
cd repository-name
Tambahkan Model YOLOv8
Letakkan file model YOLOv8 Anda (misalnya model.pt) di direktori proyek.

Ganti Path Gambar
Ganti nilai variabel image_path pada script dengan path gambar yang ingin Anda deteksi:

python
Salin kode
image_path = "dataset/IMG_1252.JPG"
Jalankan Script
Jalankan script Python:

bash
Salin kode
python script_name.py
Hasil Deteksi
Gambar hasil deteksi akan ditampilkan menggunakan Matplotlib.

Struktur Direktori
Berikut adalah struktur direktori proyek:

bash
Salin kode
.
├── detecttiion.py         # Script utama untuk deteksi wajah
├── model.pt               # File model YOLOv8 (tidak termasuk, tambahkan manual)
├── dataset/               # Folder berisi gambar uji
└── README.md              # Dokumentasi proyek

Contoh Hasil
Berikut adalah contoh hasil deteksi wajah menggunakan YOLOv8:
![Figure_1](https://github.com/user-attachments/assets/0c3b1e2b-3b16-4845-a954-2ebda09de508)



Lisensi
Proyek ini dilisensikan di bawah MIT License. Anda bebas untuk menggunakan, memodifikasi, dan mendistribusikan proyek ini sesuai ketentuan lisensi.
