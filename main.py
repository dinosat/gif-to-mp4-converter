import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

def convert_gif_to_mp4():
    input_gif_path = input_entry.get()
    output_mp4_path = output_entry.get()

    try:
        clip = VideoFileClip(input_gif_path)
        clip.write_videofile(output_mp4_path, codec='libx264', preset='ultrafast')
        status_label.config(text="Conversion completed successfully.")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")
        print(e)

def browse_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def browse_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

# Create the main window
root = tk.Tk()
root.title("GIF to MP4 Converter")

# Input GIF file
input_label = tk.Label(root, text="Input GIF:")
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()
browse_input_button = tk.Button(root, text="Browse", command=browse_input_file)
browse_input_button.pack()

# Output MP4 file
output_label = tk.Label(root, text="Output MP4:")
output_label.pack()
output_entry = tk.Entry(root)
output_entry.pack()
browse_output_button = tk.Button(root, text="Browse", command=browse_output_file)
browse_output_button.pack()

# Conversion button
convert_button = tk.Button(root, text="Convert", command=convert_gif_to_mp4)
convert_button.pack()

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
