from tkinter import *
import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a file to compress")
    return filename


def compression(input_file, output_file):
    compress(input_file, output_file)
    print("File compressed!")


def decompression(input_file, output_file):
    decompress(input_file, output_file)
    print("File decompressed!")


root = Tk()

root.title("Compression Engine")


canvas = Canvas(root, width=300, height=180)
canvas.pack()

frame = Frame()
frame.place(relx=0.2, rely=0.15, relwidth=0.8, relheight=0.8)

label = Label(frame, text=" Compress ")
label.grid(row=0, column=1)


compress_button = tk.Button(frame, text="Compress", command=lambda: compression(
    open_file(), "compressed_file.txt"))
compress_button.grid(row=3, column=1)

label = Label(frame, text=" Decompress ")
label.grid(row=0, column=4)

decompress_button = tk.Button(frame, text="Decompress", command=lambda: decompression(
    open_file(), "decompressed_file.txt"))
decompress_button.grid(row=3, column=4)


root.mainloop()
