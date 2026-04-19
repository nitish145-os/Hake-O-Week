import tkinter as tk
from tkinter import messagebox

# ---------------- STACKS ---------------- #

back_stack = []
forward_stack = []
current_page = None

# ---------------- FUNCTIONS ---------------- #

def visit_page():
    global current_page

    url = entry_url.get().strip()

    if url == "":
        messagebox.showwarning("Warning", "Enter a URL")
        return

    if current_page is not None:
        back_stack.append(current_page)

    current_page = url
    forward_stack.clear()  # clear forward history

    update_display()
    entry_url.delete(0, tk.END)


def go_back():
    global current_page

    if not back_stack:
        messagebox.showinfo("Info", "No back history")
        return

    forward_stack.append(current_page)
    current_page = back_stack.pop()

    update_display()


def go_forward():
    global current_page

    if not forward_stack:
        messagebox.showinfo("Info", "No forward history")
        return

    back_stack.append(current_page)
    current_page = forward_stack.pop()

    update_display()


def update_display():
    # Current page
    current_label.config(text=f"Current Page: {current_page}")

    # Back stack display
    back_list.delete(0, tk.END)
    for page in reversed(back_stack):
        back_list.insert(tk.END, page)

    # Forward stack display
    forward_list.delete(0, tk.END)
    for page in reversed(forward_stack):
        forward_list.insert(tk.END, page)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Browser History Simulator (Stack)")
root.geometry("600x400")

# URL Entry
tk.Label(root, text="Enter URL").pack()
entry_url = tk.Entry(root, width=50)
entry_url.pack()

tk.Button(root, text="Visit", command=visit_page).pack(pady=5)

# Navigation Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack()

tk.Button(frame_buttons, text="Back", command=go_back, width=10).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Forward", command=go_forward, width=10).grid(row=0, column=1, padx=5)

# Current Page
current_label = tk.Label(root, text="Current Page: None", font=("Arial", 12))
current_label.pack(pady=10)

# Stacks Display
frame_lists = tk.Frame(root)
frame_lists.pack()

# Back Stack
tk.Label(frame_lists, text="Back Stack").grid(row=0, column=0)
back_list = tk.Listbox(frame_lists, width=30, height=10)
back_list.grid(row=1, column=0, padx=10)

# Forward Stack
tk.Label(frame_lists, text="Forward Stack").grid(row=0, column=1)
forward_list = tk.Listbox(frame_lists, width=30, height=10)
forward_list.grid(row=1, column=1, padx=10)

root.mainloop()