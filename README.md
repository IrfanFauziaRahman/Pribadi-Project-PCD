Face Detection with YOLOv8 and OpenCV
📸 Repository ini berisi script Python untuk mendeteksi wajah dalam sebuah gambar menggunakan YOLOv8 dari library Ultralytics dan OpenCV. Proyek ini dirancang untuk memberikan bounding box pada setiap wajah yang terdeteksi dan menampilkan hasilnya menggunakan Matplotlib.

✨ Fitur Utama
✅ Deteksi wajah dalam gambar dengan akurasi tinggi menggunakan model YOLOv8.
✅ Penandaan wajah dengan bounding box menggunakan OpenCV.
✅ Visualisasi hasil deteksi dengan Matplotlib.

📥 Instalasi
Persyaratan
Pastikan Anda telah menginstal Python 3.8 atau versi yang lebih baru. Untuk library yang diperlukan, Anda bisa menginstalnya dengan perintah berikut:

bash
Salin kode
pip install ultralytics opencv-python matplotlib
🚀 Cara Penggunaan
1. Clone Repository
Clone repository ini ke komputer Anda:

bash
Salin kode
git clone https://github.com/username/repository-name.git
cd repository-name
2. Tambahkan Model YOLOv8
Letakkan file model YOLOv8 Anda (misalnya model.pt) di direktori proyek.

3. Ganti Path Gambar
Ganti nilai variabel image_path pada script dengan path gambar yang ingin Anda deteksi:

python
Salin kode
image_path = "dataset/IMG_1252.JPG"
4. Jalankan Script
Jalankan script Python:

bash
Salin kode
python detecttiion.py
5. Hasil Deteksi
Gambar hasil deteksi akan ditampilkan menggunakan Matplotlib.

📂 Struktur Direktori
plaintext
Salin kode
.
├── detecttiion.py         # Script utama untuk deteksi wajah
├── model.pt               # File model YOLOv8 (tidak termasuk, tambahkan manual)
├── dataset/               # Folder berisi gambar uji
└── README.md              # Dokumentasi proyek


📸 Contoh Hasil
Berikut adalah contoh hasil deteksi wajah menggunakan YOLOv8:

![Uploading Figure_1.png…]()

