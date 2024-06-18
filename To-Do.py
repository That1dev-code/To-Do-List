import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext

# Create an instance of the Tk class to make the window
window = tk.Tk()
window.geometry("430x500")
window.title("To-Do")

# Setting the window icon
try:
    icon = tk.PhotoImage(file=r"Path goes here guys!")
    window.iconphoto(True, icon)
except Exception as e:
    print(f"Error loading icon: {e}")

window.config(background="#ACE1AF")

# Define the fonts
title_font = ("Helvetica", 18, "bold")
label_font = ("Helvetica", 12)
task_font = ("Helvetica", 10)
tasks_font = ("Helvetica", 10)

# Setting the window title label
title_label = ttk.Label(window, text="To-Do List", font=title_font, background="#E0FBE2", foreground="#2d2d2d")
title_label.pack(pady=20)

# Frame for checkboxes and labels
frame = ttk.Frame(window, padding="10 10 10 10", style="My.TFrame")
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Checkbox for Workout
Workout_check = ttk.Checkbutton(frame, text="Workout")
Workout_check.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

# Label for Workout details
Workout_label = ttk.Label(frame, text="Chest, Legs, Shoulders, and Cardio.", font=task_font, background="#E0FBE2", foreground="#2d2d2d")
Workout_label.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

# Checkbox for Work
Work_check = ttk.Checkbutton(frame, text="Work")
Work_check.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

# Label for Work details
Work_label = ttk.Label(frame, text="Work on projects.", font=task_font, background="#E0FBE2", foreground="#2d2d2d")
Work_label.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)

# Additional Tasks Section
additional_tasks_label = ttk.Label(frame, text="Additional Tasks:", font=label_font, background="#E0FBE2", foreground="#2d2d2d")
additional_tasks_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10, columnspan=2)

# Frame for listbox and scrollbar
listbox_frame = ttk.Frame(frame)
listbox_frame.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E, padx=10, pady=5)

# Listbox for additional tasks
tasks_listbox = tk.Listbox(listbox_frame, font=task_font, height=6, bg="#E0FBE2", fg="#2d2d2d", selectbackground="#E0FBE2", borderwidth=0, highlightthickness=0)
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for listbox
scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=tasks_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.config(yscrollcommand=scrollbar.set)

# Additional Section
tasks_label = ttk.Label(frame, text="© All rights reserved.", font=tasks_font, background="#E0FBE2", foreground="#2d2d2d")
tasks_label.grid(row=10, column=0, sticky=tk.W, padx=10, pady=10, columnspan=2)
tasks_label.place(x=-9, y=355)

# Entry widget to add new task
new_task_entry = ttk.Entry(frame, font=task_font)
new_task_entry.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W+tk.E)

# Function to add new task
def add_task():
    task = new_task_entry.get().strip()
    if task:
        tasks_listbox.insert(tk.END, task)
        new_task_entry.delete(0, tk.END)
        status_var.set(f"Task '{task}' added")
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Function to delete selected task
def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        status_var.set(f"Task '{task}' deleted")
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

# Button to add new task
add_task_button = ttk.Button(frame, text="Add Task", command=add_task)
add_task_button.grid(row=4, column=1, padx=10, pady=5)

# Button to delete selected task
delete_task_button = ttk.Button(frame, text="Delete Task", command=delete_task)
delete_task_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Status bar
status_var = tk.StringVar()
status_bar = ttk.Label(window, textvariable=status_var, font=task_font, background="#E0FBE2", foreground="#2d2d2d")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Styling
style = ttk.Style()
style.configure("TCheckbutton", background="#E0FBE2", foreground="black")
style.configure("TLabel", background="#B0EBB4", foreground="#black")
style.configure("TButton", background="#E0FBE2", foreground="#2d2d2d")
style.configure("TFrame", background="#BFF6C3")
style.map("TButton", background=[("active", "#E0FBE2")])

# Menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Clear All Tasks", command=lambda: tasks_listbox.delete(0, tk.END))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "To-Do List App\nVersion 1.0"))

window.mainloop()  # Places the window on the screen
