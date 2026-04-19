import tkinter as tk
from tkinter import messagebox

# ---------------- DATA ---------------- #

tasks = []

undo_stack = []
redo_stack = []

# ---------------- STACK OPERATIONS ---------------- #

def push_undo(action):
    undo_stack.append(action)

def push_redo(action):
    redo_stack.append(action)

# ---------------- CORE FUNCTIONS ---------------- #

def add_task():
    task = entry_task.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Enter a task")
        return

    tasks.append(task)
    push_undo(("add", task))
    redo_stack.clear()

    entry_task.delete(0, tk.END)
    update_display(status="Task Added")


def delete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task")
        return

    index = selected[0]
    task = tasks.pop(index)

    push_undo(("delete", task, index))
    redo_stack.clear()

    update_display(status="Task Deleted")


def edit_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task")
        return

    new_task = entry_task.get().strip()
    if new_task == "":
        messagebox.showwarning("Warning", "Enter new task")
        return

    index = selected[0]
    old_task = tasks[index]

    tasks[index] = new_task

    push_undo(("edit", old_task, new_task, index))
    redo_stack.clear()

    entry_task.delete(0, tk.END)
    update_display(status="Task Edited")


# ---------------- UNDO / REDO ---------------- #

def undo():
    if not undo_stack:
        messagebox.showinfo("Info", "Nothing to undo")
        return

    action = undo_stack.pop()

    if action[0] == "add":
        tasks.remove(action[1])
    elif action[0] == "delete":
        tasks.insert(action[2], action[1])
    elif action[0] == "edit":
        tasks[action[3]] = action[1]

    push_redo(action)
    update_display(status="Undo performed")


def redo():
    if not redo_stack:
        messagebox.showinfo("Info", "Nothing to redo")
        return

    action = redo_stack.pop()

    if action[0] == "add":
        tasks.append(action[1])
    elif action[0] == "delete":
        tasks.remove(action[1])
    elif action[0] == "edit":
        tasks[action[3]] = action[2]

    push_undo(action)
    update_display(status="Redo performed")


# ---------------- UI UPDATE ---------------- #

def update_display(status=""):
    listbox.delete(0, tk.END)

    if not tasks:
        listbox.insert(tk.END, "No tasks available")
    else:
        for t in tasks:
            listbox.insert(tk.END, t)

    status_label.config(text=f"Status: {status}")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Task Manager (Undo/Redo)")
root.geometry("550x450")

# Input
tk.Label(root, text="Task").pack()
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)

# Buttons
frame_btn = tk.Frame(root)
frame_btn.pack()

tk.Button(frame_btn, text="Add", width=10, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Edit", width=10, command=edit_task).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Delete", width=10, command=delete_task).grid(row=0, column=2, padx=5)

# Undo/Redo
frame_undo = tk.Frame(root)
frame_undo.pack(pady=10)

tk.Button(frame_undo, text="Undo", width=10, command=undo).grid(row=0, column=0, padx=10)
tk.Button(frame_undo, text="Redo", width=10, command=redo).grid(row=0, column=1, padx=10)

# Task List
listbox = tk.Listbox(root, width=60, height=12)
listbox.pack(pady=10)

# Status
status_label = tk.Label(root, text="Status: Ready", font=("Arial", 11))
status_label.pack()

root.mainloop()