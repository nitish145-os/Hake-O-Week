import tkinter as tk
from tkinter import messagebox

# ---------------- QUEUE ---------------- #

queue = []  # each job = [job_id, pages]

# ---------------- FUNCTIONS ---------------- #

def enqueue_job():
    job_id = entry_id.get().strip()

    try:
        pages = int(entry_pages.get())
    except:
        messagebox.showerror("Error", "Pages must be a number")
        return

    if job_id == "":
        messagebox.showwarning("Warning", "Enter Job ID")
        return

    # prevent duplicate IDs (optional but good)
    for job in queue:
        if job[0] == job_id:
            messagebox.showerror("Error", "Job ID already exists")
            return

    queue.append([job_id, pages])  # enqueue

    status_label.config(text=f"Job {job_id} added to queue")
    clear_entries()
    display_queue()


def dequeue_job():
    if not queue:
        messagebox.showinfo("Info", "No jobs in queue")
        return

    job = queue.pop(0)  # FIFO dequeue
    status_label.config(text=f"Processing Job {job[0]} ({job[1]} pages)")

    display_queue()


def display_queue():
    listbox.delete(0, tk.END)

    if not queue:
        listbox.insert(tk.END, "Queue is empty")
        return

    for job in queue:
        listbox.insert(tk.END, f"Job ID: {job[0]} | Pages: {job[1]}")


def clear_entries():
    entry_id.delete(0, tk.END)
    entry_pages.delete(0, tk.END)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Printer Queue Simulator (FIFO)")
root.geometry("500x400")

# Input fields
tk.Label(root, text="Job ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Number of Pages").pack()
entry_pages = tk.Entry(root)
entry_pages.pack()

# Buttons
tk.Button(root, text="Add Job (Enqueue)", command=enqueue_job).pack(pady=5)
tk.Button(root, text="Process Job (Dequeue)", command=dequeue_job).pack(pady=5)
tk.Button(root, text="Display Queue", command=display_queue).pack(pady=5)

# Queue display
listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

# Status
status_label = tk.Label(root, text="Status: Idle", font=("Arial", 11))
status_label.pack()

root.mainloop()