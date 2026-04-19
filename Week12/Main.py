import tkinter as tk
from tkinter import messagebox

# ---------------- LINKED LIST ---------------- #

class Node:
    def __init__(self, item_id, name, price, qty):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.qty = qty
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, node):
        node.next = self.head
        self.head = node

    def insert_at_end(self, node):
        if self.head is None:
            self.head = node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def delete_by_id(self, item_id):
        temp = self.head
        prev = None

        while temp:
            if temp.item_id == item_id:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return True
            prev = temp
            temp = temp.next

        return False

    def get_all_items(self):
        items = []
        temp = self.head
        while temp:
            items.append(temp)
            temp = temp.next
        return items


cart = LinkedList()

# ---------------- FUNCTIONS ---------------- #

def add_begin():
    add_item("begin")

def add_end():
    add_item("end")

def add_item(position):
    item_id = entry_id.get()
    name = entry_name.get()

    try:
        price = float(entry_price.get())
        qty = int(entry_qty.get())
    except:
        messagebox.showerror("Error", "Invalid price or quantity")
        return

    if item_id == "" or name == "":
        messagebox.showwarning("Warning", "Fill all fields")
        return

    new_node = Node(item_id, name, price, qty)

    if position == "begin":
        cart.insert_at_beginning(new_node)
    else:
        cart.insert_at_end(new_node)

    messagebox.showinfo("Success", "Item added")
    clear_entries()
    display_items()


def delete_item():
    item_id = entry_id.get()

    if item_id == "":
        messagebox.showwarning("Warning", "Enter ID")
        return

    if cart.delete_by_id(item_id):
        messagebox.showinfo("Success", "Item removed")
    else:
        messagebox.showerror("Error", "Item not found")

    display_items()
    clear_entries()


def display_items():
    listbox.delete(0, tk.END)

    items = cart.get_all_items()

    if not items:
        listbox.insert(tk.END, "Cart is empty")
        total_label.config(text="Total: 0")
        return

    total = 0
    for node in items:
        cost = node.price * node.qty
        total += cost
        listbox.insert(tk.END,
            f"ID:{node.item_id} | {node.name} | ₹{node.price} x {node.qty} = ₹{cost}"
        )

    total_label.config(text=f"Total: ₹{total}")


def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_qty.delete(0, tk.END)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Shopping Cart (Linked List)")
root.geometry("550x450")

tk.Label(root, text="Item ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Price").pack()
entry_price = tk.Entry(root)
entry_price.pack()

tk.Label(root, text="Quantity").pack()
entry_qty = tk.Entry(root)
entry_qty.pack()

tk.Button(root, text="Add at Beginning", command=add_begin).pack(pady=3)
tk.Button(root, text="Add at End", command=add_end).pack(pady=3)
tk.Button(root, text="Delete by ID", command=delete_item).pack(pady=3)
tk.Button(root, text="Display Cart", command=display_items).pack(pady=3)

listbox = tk.Listbox(root, width=65)
listbox.pack(pady=10)

total_label = tk.Label(root, text="Total: 0", font=("Arial", 12))
total_label.pack()

root.mainloop()