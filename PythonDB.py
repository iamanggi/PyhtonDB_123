import tkinter as tk
from tkinter import messagebox
import sqlite3

window = tk.Tk()
window.geometry("500x700")
window.title("Aplikasi Nilai Siswa")
window.resizable(False, False)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

entry_font = ("Helvetica", 12)
entry_width = 20

nama_label = tk.Label (frame, text="Nama Siswa")
nama_entry = tk.Entry(frame, font=entry_font, width=entry_width)

biologi_label = tk.Label (frame, text="Biologi")
biologi_entry = tk.Entry(frame, font=entry_font, width=entry_width)

fisika_label = tk.Label(frame, text= "Fisika")
fisika_entry = tk.Entry(frame, font=entry_font, width=entry_width)

inggris_label = tk.Label(frame, text="Inggris")
inggris_entry = tk.Entry(frame, font=entry_font, width= entry_width)

label_y = 0
entry_y = 1
for label, entry in zip([nama_label, biologi_label, fisika_label, inggris_label],
                        [nama_entry,biologi_entry, fisika_entry, inggris_entry]):
    label.grid(row=label_y, column=0, padx=5)
    entry.grid(row=label_y, column=1, padx=5)
    label_y += 2

def Submit_Nilai():
    nama_siswa = nama_entry.get()
    nilai_biologi = int(biologi_entry.get())
    nilai_fisika = int(fisika_entry.get())
    nilai_inggris = int(inggris_entry.get())

    if nilai_biologi >= nilai_fisika and nilai_biologi >= nilai_inggris:
            prediksi_fakultas = "Kedokteran"
    elif nilai_fisika >= nilai_biologi and nilai_fisika >= nilai_inggris:
            prediksi_fakultas = "Teknik"
    elif nilai_inggris >= nilai_biologi and nilai_inggris >= nilai_fisika:
            prediksi_fakultas = "Bahasa"


    messagebox.showinfo("Hasil Prediksi", f"Prediksi Fakultas: {prediksi_fakultas}")




    conn = sqlite3.connect("NilaiSiswa.db")

    cursor = conn.cursor()
    """
    cursor.execute('''
            create table nilai_siswa (
                id integer primary key autoincrement, 
                nama_siswa text,
                biologi integer,
                fisika integer,
                inggris integer,
                prediksi_fakultas text
            )
        ''')
"""
    cursor.execute('''
            INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas))


    conn.commit()
    conn.close()

submit_button = tk.Button(text="Submit", command=Submit_Nilai,
                          font=("Helvetica", 12), bg="silver", fg="white", bd=0, padx=10, pady=3,
                          relief=tk.GROOVE, cursor="hand2")
submit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

window.mainloop()