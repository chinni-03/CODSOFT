import random
import string
import pyperclip
import tkinter as tk
from tkinter import ttk

DARK_GREY = '#3d3d3d'
WHITE = '#fff'
HEADER_FONT = ('Arial', 16)
DEFAULT_FONT = ('Arial', 12)

characters_to_use = string.ascii_letters + string.digits + string.punctuation

window = tk.Tk()
window.title('Password Generator')
window.geometry('400x150')
window.resizable(0,0)

def generate_password(entry: tk.Entry):
    length = int(entry.get())
    password = ''.join(random.choice(characters_to_use) for i in range(length))

    generated_password.delete(0, tk.END)
    generated_password.insert(0,password)

def copy(generated_password: tk.Entry):
    copy_password = generated_password.get()
    pyperclip.copy(copy_password)

header_frame = tk.Frame(window, height=20, bg=DARK_GREY)
header_frame.pack(fill='x')
style_header = ttk.Style()
style_header.configure('Custom.TLabel', padding=(5,5,5,5))
header_label = ttk.Label(header_frame, text='Password Generator', style='Custom.TLabel', background=DARK_GREY, foreground=WHITE, font=HEADER_FONT)
header_label.pack()

password_length_frame = tk.Frame(window, height=30)
password_length_frame.pack(fill='x', padx=10, pady=20)
input_label = tk.Label(password_length_frame, text='Enter the length of password:', font=DEFAULT_FONT)
input_label.grid(row=0, column=0, padx=(5,10))
input_style = ttk.Style()
input_style.configure('Custom.TEntry', padding=(5,5,5,5))
int_input = tk.IntVar()
input_space = ttk.Entry(password_length_frame, textvariable=int_input, width=8)
input_space.grid(row=0, column=1)
generate_button = ttk.Button(password_length_frame, text='generate',width=10, command=lambda: generate_password(input_space))
generate_button.grid(row=0, column=2, padx=(20,0))
copy_frame = tk.Frame(height=20)
copy_frame.pack()
generated_password = tk.Entry(copy_frame)
generated_password.grid(row=0, column=0)
copy_button = ttk.Button(copy_frame, text='copy', width=10, command=lambda: copy(generated_password))
copy_button.grid(row=0, column=1, padx=(20,0), sticky='e')

window.mainloop()