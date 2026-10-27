import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("nilai_siswa.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS nilai_siswa (
    nama_siswa TEXT,
    biologi REAL,
    fisika REAL,
    inggris REAL,
    prediksi_fakultas TEXT
)
""")

conn.commit()

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x350")

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
)
judul.pack(pady=15)

tk.Label(root, text="Nama Siswa").pack()
entry_nama = tk.Entry(root, width=30)
entry_nama.pack(pady=5)

tk.Label(root, text="Nilai Biologi").pack()
entry_biologi = tk.Entry(root, width=30)
entry_biologi.pack(pady=5)

tk.Label(root, text="Nilai Fisika").pack()
entry_fisika = tk.Entry(root, width=30)
entry_fisika.pack(pady=5)

tk.Label(root, text="Nilai Inggris").pack()
entry_inggris = tk.Entry(root, width=30)
entry_inggris.pack(pady=5)


def hasil_prediksi():
    nama = entry_nama.get().strip()
    nilai_biologi = entry_biologi.get()
    nilai_fisika = entry_fisika.get()
    nilai_inggris = entry_inggris.get()

    if not nama:
            messagebox.showerror("gabisa", "nama wajib diisi")
            return
    if not nilai_biologi:
            messagebox.showerror("gabisa", "nilai biologi wajib diisi")
            return
    if not nilai_fisika:
            messagebox.showerror("gabisa", "nilai fisika wajib diisi")
            return
    if not nilai_inggris:
            messagebox.showerror("gabisa", "nilai inggris wajib diisi")
            return

    nilai_tertinggi = max(nilai_biologi, nilai_fisika, nilai_inggris)

    if nilai_biologi == nilai_tertinggi:
        prediksi = "Kedokteran"
    elif nilai_fisika == nilai_tertinggi:
        prediksi = "Teknik"
    else:
        prediksi = "Bahasa"

    cursor.execute("""
        INSERT INTO nilai_siswa
        (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    """, (nama, nilai_biologi, nilai_fisika, nilai_inggris, prediksi))

    conn.commit()

    hasil.config(
        text=f"Hasil Prediksi: {prediksi}"
    )

    messagebox.showinfo(
        "Berhasil",
        f"Data sudah disimpan\nPrediksi: {prediksi}"
    )

button = tk.Button(
    root,
    text="Submit Nilai",
    command=hasil_prediksi
)
button.pack(pady=15)

hasil = tk.Label(
    root,
    text="",
)
hasil.pack(pady=5)

def tutup_aplikasi():
    conn.close()
    root.destroy()

root.mainloop()