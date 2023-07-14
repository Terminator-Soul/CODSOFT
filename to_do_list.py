import tkinter as tk
from tkinter import messagebox, font

# Create a list to store tasks
tasks = []


# Function to add a new task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


# Function to delete a selected task
def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")


# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("1980x1080")
root.configure(bg="#1a1a1a")

# Create custom fonts
title_font = font.Font(family="Helvetica", size=30, weight="bold")
task_font = font.Font(family="Helvetica", size=26)

# Create the title label
title_label = tk.Label(
    root, text="To-Do List", font=title_font, bg="#1a1a1a", foreground="#ffffff"
)
title_label.pack(pady=10)

# Create the listbox to display tasks
listbox = tk.Listbox(root, font=task_font, bg="#1a1a1a", fg="#ffffff", width=1700)
listbox.pack(padx=20)


# Create an entry field for new tasks
entry = tk.Entry(
    root, font=task_font, width=70, background="#1a1a1a", foreground="#ffffff"
)
entry.pack(pady=10)

# Create buttons for adding and deleting tasks
add_button = tk.Button(
    root,
    text="Add Task",
    font=task_font,
    command=add_task,
    bg="#1a1a1a",
    fg="white",
    padx=30,
    pady=30,
)
add_button.pack(pady=10, padx=30)

delete_button = tk.Button(
    root,
    text="Delete Task",
    font=task_font,
    command=delete_task,
    bg="#1a1a1a",
    fg="white",
    pady=30,
    padx=30,
)
delete_button.pack(pady=30)

# Start the main event loop
root.mainloop()
