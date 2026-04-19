import tkinter as tk
from tkinter import messagebox

# ---------------- CIRCULAR QUEUE ---------------- #

SIZE = 5
queue = [None] * SIZE

front = -1
rear = -1

# ---------------- FUNCTIONS ---------------- #

def enqueue():
    global front, rear

    cust_id = entry_id.get().strip()
    txn = entry_txn.get().strip()

    if cust_id == "" or txn == "":
        messagebox.showwarning("Warning", "Fill all fields")
        return

    # FULL condition
    if (rear + 1) % SIZE == front:
        status_label.config(text="Queue Full (Peak Load!)", fg="red")
        return

    if front == -1:
        front = rear = 0
    else:
        rear = (rear + 1) % SIZE

    queue[rear] = (cust_id, txn)

    entry_id.delete(0, tk.END)
    entry_txn.delete(0, tk.END)

    status_label.config(text=f"Customer {cust_id} added", fg="green")
    update_display()


def dequeue():
    global front, rear

    if front == -1:
        status_label.config(text="Queue Empty", fg="red")
        return

    removed = queue[front]
    queue[front] = None

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % SIZE

    status_label.config(text=f"Serving {removed[0]}", fg="blue")
    update_display()


def update_display():
    for i in range(SIZE):
        box = boxes[i]

        if queue[i] is None:
            box.config(text="Empty", bg="#2c2c2c")
        else:
            cust_id, txn = queue[i]
            box.config(text=f"{cust_id}\n{txn}", bg="#4caf50")

        # Reset border
        box.config(highlightbackground="gray", highlightthickness=1)

    # Highlight FRONT and REAR
    if front != -1:
        boxes[front].config(highlightbackground="yellow", highlightthickness=3)

    if rear != -1:
        boxes[rear].config(highlightbackground="cyan", highlightthickness=3)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("ATM Circular Queue")
root.geometry("650x400")
root.configure(bg="#1e1e1e")

# Title
tk.Label(root, text="ATM Queue Simulator",
         font=("Arial", 16, "bold"),
         bg="#1e1e1e", fg="white").pack(pady=10)

# Input Frame
frame_input = tk.Frame(root, bg="#1e1e1e")
frame_input.pack()

tk.Label(frame_input, text="Customer ID", bg="#1e1e1e", fg="white").grid(row=0, column=0)
entry_id = tk.Entry(frame_input)
entry_id.grid(row=1, column=0, padx=10)

tk.Label(frame_input, text="Transaction", bg="#1e1e1e", fg="white").grid(row=0, column=1)
entry_txn = tk.Entry(frame_input)
entry_txn.grid(row=1, column=1, padx=10)

# Buttons
frame_btn = tk.Frame(root, bg="#1e1e1e")
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Enqueue", width=12, command=enqueue, bg="#4caf50").grid(row=0, column=0, padx=10)
tk.Button(frame_btn, text="Dequeue", width=12, command=dequeue, bg="#f44336").grid(row=0, column=1, padx=10)

# Queue Display
frame_queue = tk.Frame(root, bg="#1e1e1e")
frame_queue.pack(pady=20)

boxes = []
for i in range(SIZE):
    lbl = tk.Label(frame_queue, text="Empty",
                   width=12, height=4,
                   bg="#2c2c2c", fg="white",
                   relief="flat")
    lbl.grid(row=0, column=i, padx=5)
    boxes.append(lbl)

# Status
status_label = tk.Label(root, text="Status: Ready",
                        bg="#1e1e1e", fg="white",
                        font=("Arial", 11))
status_label.pack(pady=10)

root.mainloop()