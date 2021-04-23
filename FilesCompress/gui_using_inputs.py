from tkinter import *
import tkinter as tk
from compressmodule import compress, decompress


def compression(input_file, output_file):
    compress(input_file, output_file)


def decompression(input_file, output_file):
    decompress(input_file, output_file)


root = Tk()

root.title("Compression Engine")


canvas = Canvas(root, width=800, height=180)
canvas.pack()

frame = Frame()
frame.place(relx=0.2, rely=0.15, relwidth=0.8, relheight=0.8)

label = Label(frame, text=" Compress ")
label.grid(row=0, column=1)

input_label = tk.Label(frame, text="File to compress: ")
input_entry = tk.Entry(frame)
input_label.grid(row=1, column=0)
input_entry.grid(row=1, column=1)

output_label = tk.Label(frame, text="Compressed File: ")
output_entry = tk.Entry(frame)
output_label.grid(row=2, column=0)
output_entry.grid(row=2, column=1)

compress_button = tk.Button(frame, text="Compress", command=lambda: compression(
    input_entry.get(), output_entry.get()))
compress_button.grid(row=3, column=1)

label = Label(frame, text=" Decompress ")
label.grid(row=0, column=4)

input_label = tk.Label(frame, text="File to decompress: ")
input_entry = tk.Entry(frame)
input_label.grid(row=1, column=3)
input_entry.grid(row=1, column=4)

output_label = tk.Label(frame, text="Decompressed File: ")
output_entry = tk.Entry(frame)
output_label.grid(row=2, column=3)
output_entry.grid(row=2, column=4)

decompress_button = tk.Button(frame, text="Decompress", command=lambda: decompression(
    input_entry.get(), output_entry.get()))
decompress_button.grid(row=3, column=4)


root.mainloop()
