import tkinter as tk
from tkinter import messagebox

# ---------------- TREE STRUCTURE ---------------- #

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


root_node = None

# ---------------- FUNCTIONS ---------------- #

def create_root():
    global root_node
    name = entry_name.get().strip()

    if name == "":
        messagebox.showwarning("Warning", "Enter folder name")
        return

    if root_node is not None:
        messagebox.showerror("Error", "Root already exists")
        return

    root_node = Node(name)
    entry_name.delete(0, tk.END)
    update_tree_display()
    update_status("Root created")


def add_child(direction):
    global root_node

    parent = entry_parent.get().strip()
    child = entry_name.get().strip()

    if parent == "" or child == "":
        messagebox.showwarning("Warning", "Enter parent and child")
        return

    node = find_node(root_node, parent)

    if node is None:
        messagebox.showerror("Error", "Parent not found")
        return

    if direction == "left":
        if node.left is not None:
            messagebox.showerror("Error", "Left already exists")
            return
        node.left = Node(child)
    else:
        if node.right is not None:
            messagebox.showerror("Error", "Right already exists")
            return
        node.right = Node(child)

    entry_name.delete(0, tk.END)
    update_tree_display()
    update_status(f"{child} added to {parent}")


def find_node(node, name):
    if node is None:
        return None
    if node.name == name:
        return node

    left = find_node(node.left, name)
    if left:
        return left

    return find_node(node.right, name)


# ---------------- TRAVERSALS ---------------- #

def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(node.name)
        inorder(node.right, result)

def preorder(node, result):
    if node:
        result.append(node.name)
        preorder(node.left, result)
        preorder(node.right, result)

def postorder(node, result):
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.name)


def show_traversal(mode):
    result = []

    if root_node is None:
        messagebox.showinfo("Info", "Tree is empty")
        return

    if mode == "inorder":
        inorder(root_node, result)
    elif mode == "preorder":
        preorder(root_node, result)
    else:
        postorder(root_node, result)

    traversal_label.config(text=f"{mode.capitalize()}: {' → '.join(result)}")


# ---------------- DISPLAY TREE ---------------- #

def display_tree(node, indent=""):
    if node is None:
        return ""

    text = indent + "📁 " + node.name + "\n"
    text += display_tree(node.left, indent + "   ")
    text += display_tree(node.right, indent + "   ")

    return text


def update_tree_display():
    text_area.delete("1.0", tk.END)

    if root_node is None:
        text_area.insert(tk.END, "No directories yet")
    else:
        text_area.insert(tk.END, display_tree(root_node))


def update_status(msg):
    status_label.config(text=f"Status: {msg}")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("File System Directory (Binary Tree)")
root.geometry("750x500")
root.configure(bg="#1e1e1e")

# Title
tk.Label(root, text="File System Simulator",
         font=("Arial", 16, "bold"),
         bg="#1e1e1e", fg="white").pack(pady=10)

# Input Frame
frame_input = tk.Frame(root, bg="#1e1e1e")
frame_input.pack()

tk.Label(frame_input, text="Folder Name", bg="#1e1e1e", fg="white").grid(row=0, column=0)
entry_name = tk.Entry(frame_input)
entry_name.grid(row=1, column=0, padx=10)

tk.Label(frame_input, text="Parent Folder", bg="#1e1e1e", fg="white").grid(row=0, column=1)
entry_parent = tk.Entry(frame_input)
entry_parent.grid(row=1, column=1, padx=10)

# Buttons
frame_btn = tk.Frame(root, bg="#1e1e1e")
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Create Root", command=create_root, bg="#4caf50", width=12).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Add Left", command=lambda: add_child("left"), bg="#2196f3", width=12).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Add Right", command=lambda: add_child("right"), bg="#ff9800", width=12).grid(row=0, column=2, padx=5)

# Traversal Buttons
frame_trav = tk.Frame(root, bg="#1e1e1e")
frame_trav.pack(pady=10)

tk.Button(frame_trav, text="Inorder", command=lambda: show_traversal("inorder")).grid(row=0, column=0, padx=5)
tk.Button(frame_trav, text="Preorder", command=lambda: show_traversal("preorder")).grid(row=0, column=1, padx=5)
tk.Button(frame_trav, text="Postorder", command=lambda: show_traversal("postorder")).grid(row=0, column=2, padx=5)

traversal_label = tk.Label(root, text="", bg="#1e1e1e", fg="white")
traversal_label.pack()

# Tree Display
text_area = tk.Text(root, width=80, height=15, bg="#2c2c2c", fg="white")
text_area.pack(pady=10)

# Status
status_label = tk.Label(root, text="Status: Ready", bg="#1e1e1e", fg="white")
status_label.pack()

root.mainloop()