# Import library tkinter sebagai tk dan messagebox untuk menampilkan pesan kesalahan
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan hasil prediksi program studi
def prediksi_prodi():
    try:
        # Loop untuk mendapatkan nilai dari setiap entry input
        for entry in entries:
            # Mendapatkan nilai dari entry input dan mengonversinya menjadi integer
            nilai = int(entry.get())
            # Memeriksa apakah nilai berada di antara 0 dan 100
            if not(0 <= nilai <= 100):
                # Jika tidak, menghasilkan ValueError
                raise ValueError("nilai harus lebih dari sama dengan 0 dan kurang dari sama dengan 100")
        # Menampilkan prediksi jika tidak ada error
        hasil_label.config(text="Prediksi prodi : Teknologi Informasi")
    except ValueError as ve:
        # Menampilkan pesan kesalahan jika input tidak valid
        messagebox.showerror("input error", "pastikan sesuai dengan yang diminta")
        # Mengosongkan label hasil jika terjadi kesalahan
        hasil_label.config(text="")

# Inisialisasi jendela Tkinter
root = tk.Tk()
# Mengatur judul jendela
root.title("Aplikasi Prediksi Prodi Pilihan")
# Mengatur ukuran jendela
root.geometry("400x700")

# Label Judul Aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
judul_label.pack(pady=10)

# Membuat frame untuk input nilai mata pelajaran
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# List untuk menyimpan label dan entry input
labels = []
entries = []
# Loop untuk membuat label dan entry input nilai mata pelajaran sebanyak 10 kali
for i in range(10):
    # Membuat label untuk setiap mata pelajaran
    label = tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 12))
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    # Membuat entry input untuk setiap mata pelajaran
    entry = tk.Entry(input_frame, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    # Menambahkan label dan entry ke dalam list
    labels.append(label)
    entries.append(entry)

# Tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi, font=("Arial", 12))
prediksi_button.pack(pady=20)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14))
hasil_label.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
