import tkinter as tk
from tkinter import ttk

# colors used in the program
DARK_BG = '#3d3d3d'
WHITE = '#fff'
HEADER_FONT = ('Arial', 16)
DEFAULT_FONT = ('Arial', 10)

# create main window
window = tk.Tk()
window.title('Todo List')
window.geometry('400x500')
window.resizable(0,0)

# create header
header_frame = tk.Frame(window, height=20)
header_frame.pack(fill='x')

style = ttk.Style()
style.configure('Custom.TLabel', padding=(5,5,5,5))
label = ttk.Label(header_frame, text='Todo List', anchor='center', style='Custom.TLabel', background=DARK_BG, foreground=WHITE, font=HEADER_FONT)
label.pack(fill='x')

# create a frame containing label, an input and an add task button
label_frame = tk.Frame(window, height=35)
label_frame.pack(fill='x', padx=20)
# label
label = tk.Label(label_frame, text='Enter task:', anchor='e', font=DEFAULT_FONT)
label.grid(row=0, column=0, pady=(10,0))
# input
text_variable_entry = tk.StringVar()
style = ttk.Style()
style.configure('Custom.TEntry', padding=(5,5,5,5))
entry = ttk.Entry(label_frame, textvariable=text_variable_entry, width=25, style='Custom.TEntry', font=DEFAULT_FONT)
entry.grid(row=0, column=1, pady=(10,0), padx=(10,0))
# add task button
style_button = ttk.Style()
style_button.configure('Custom.TButton', padding=(5,5,5,5), font=DEFAULT_FONT)
add_task = ttk.Button(label_frame, text='add task', width=8, style='Custom.TButton', command=lambda: add_task_to_list(entry, task_list))
add_task.grid(row=0, column=2, pady=(10,0), padx=(10,0))

# create a frame, a listbox to display the tasks, and a scrollbar
scrollbar_frame = tk.Frame(window, width=100, height=20)
scrollbar_frame.pack(pady=20)
# listbox
task_list = tk.Listbox(scrollbar_frame, width=55, height=20, borderwidth=0)
task_list.grid(row=0, column=0)
# scrollbar
scrollbar = tk.Scrollbar(scrollbar_frame, orient='vertical', command=task_list.yview, width=15)
scrollbar.grid(row=0, column=1, sticky='NS')
# configure listbox
task_list.config(yscrollcommand=scrollbar.set)
# configure scrollbar
scrollbar.config(command=task_list.yview)
scrollbar.set(20, 200)

# create a frame, and a delete button
delete_frame = tk.Frame(window)
delete_frame.pack(fill='x', padx=20)
# delete button
style_button = ttk.Style()
style_button.configure('Custom.TButton', padding=(5,5,5,5), font=DEFAULT_FONT)
delete = ttk.Button(delete_frame, text='delete task', style='Custom.TButton', command=lambda: delete_task(task_list))
delete.pack(padx=5, fill='x')

# read the tasks from the todo.txt file and display on loading the window
with open('todo.txt', 'r') as read_file:
    lines = read_file.readlines()
    for line in lines:
        task_list.insert(tk.END, line)

# adding tasks to the list from the Entry widget
def add_task_to_list(task: tk.Entry, task_list: tk.Listbox):
    new_task = task.get()
    if new_task not in task_list.get(0, tk.END):
        task_list.insert(tk.END, new_task)
        with open('todo.txt', 'a') as task_list_file:
            task_list_file.write(f'{new_task}\n')

# deleting the selected task from the Entry widget
def delete_task(task_list: tk.Listbox):
    selected_task = task_list.get(tk.ACTIVE)
    task_list.delete(tk.ACTIVE)

    with open('todo.txt', 'r+') as tasks_list_file:
        lines = tasks_list_file.readlines()

        for line in lines:
            if selected_task in line:
                lines.remove(line)

        tasks_list_file.truncate(0)
        with open('todo.txt', 'w') as re_write:
            for line in lines:
                re_write.write(line)

window.mainloop()