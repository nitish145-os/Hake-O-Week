import tkinter as tk
from tkinter import messagebox

# ---------------- DATA ---------------- #

contacts = []  # each contact = [name, phone]

# ---------------- FUNCTIONS ---------------- #

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Fill all fields")
        return

    # prevent duplicate names (simple rule)
    for c in contacts:
        if c[0].lower() == name.lower():
            messagebox.showerror("Error", "Contact already exists")
            return

    contacts.append([name, phone])
    messagebox.showinfo("Success", "Contact added")
    clear_entries()
    display_contacts()


def display_contacts():
    listbox.delete(0, tk.END)

    if not contacts:
        listbox.insert(tk.END, "No contacts available")
        return

    for c in contacts:
        listbox.insert(tk.END, f"{c[0]} : {c[1]}")


# ----------- BUBBLE SORT ----------- #

def sort_contacts():
    n = len(contacts)

    for i in range(n):
        for j in range(0, n - i - 1):
            if contacts[j][0].lower() > contacts[j + 1][0].lower():
                contacts[j], contacts[j + 1] = contacts[j + 1], contacts[j]

    messagebox.showinfo("Sorted", "Contacts sorted alphabetically")
    display_contacts()


# ----------- BINARY SEARCH ----------- #

def binary_search(name):
    low = 0
    high = len(contacts) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_name = contacts[mid][0].lower()

        if mid_name == name:
            return mid
        elif mid_name < name:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def search_contact():
    name = entry_name.get().strip().lower()

    if name == "":
        messagebox.showwarning("Warning", "Enter name to search")
        return

    # IMPORTANT: must sort before binary search
    sort_contacts()

    index = binary_search(name)

    listbox.delete(0, tk.END)

    if index != -1:
        c = contacts[index]
        listbox.insert(tk.END, f"Found: {c[0]} : {c[1]}")
    else:
        listbox.insert(tk.END, "Contact not found")


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Contact Book (Sorting + Binary Search)")
root.geometry("500x400")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Display Contacts", command=display_contacts).pack(pady=5)
tk.Button(root, text="Sort Contacts", command=sort_contacts).pack(pady=5)
tk.Button(root, text="Search (Binary)", command=search_contact).pack(pady=5)

listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

root.mainloop()