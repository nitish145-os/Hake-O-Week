import tkinter as tk
from tkinter import messagebox

# Fixed size array
MAX_BOOKS = 5
books = []  # each book = [id, title, author]

# ---------------- FUNCTIONS ---------------- #

def add_book():
    if len(books) >= MAX_BOOKS:
        messagebox.showerror("Error", "Catalogue is full!")
        return

    book_id = entry_id.get()
    title = entry_title.get()
    author = entry_author.get()

    if book_id == "" or title == "" or author == "":
        messagebox.showwarning("Warning", "All fields are required!")
        return

    # Check duplicate ID
    for b in books:
        if b[0] == book_id:
            messagebox.showerror("Error", "Book ID already exists!")
            return

    books.append([book_id, title, author])
    messagebox.showinfo("Success", "Book added successfully!")

    clear_entries()
    display_books()


def search_book():
    title = entry_title.get()

    if title == "":
        messagebox.showwarning("Warning", "Enter title to search!")
        return

    found = []
    for b in books:  # Linear Search
        if title.lower() in b[1].lower():
            found.append(b)

    listbox.delete(0, tk.END)

    if found:
        for b in found:
            listbox.insert(tk.END, f"ID: {b[0]} | {b[1]} | {b[2]}")
    else:
        messagebox.showinfo("Result", "No book found!")


def delete_book():
    book_id = entry_id.get()

    if book_id == "":
        messagebox.showwarning("Warning", "Enter ID to delete!")
        return

    for b in books:
        if b[0] == book_id:
            books.remove(b)
            messagebox.showinfo("Success", "Book deleted!")
            display_books()
            clear_entries()
            return

    messagebox.showerror("Error", "Book not found!")


def display_books():
    listbox.delete(0, tk.END)

    if len(books) == 0:
        listbox.insert(tk.END, "No books in catalogue")
        return

    for b in books:
        listbox.insert(tk.END, f"ID: {b[0]} | {b[1]} | {b[2]}")


def clear_entries():
    entry_id.delete(0, tk.END)
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Library Book Catalogue")
root.geometry("500x400")

# Labels & Entries
tk.Label(root, text="Book ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Title").pack()
entry_title = tk.Entry(root)
entry_title.pack()

tk.Label(root, text="Author").pack()
entry_author = tk.Entry(root)
entry_author.pack()

# Buttons
tk.Button(root, text="Add Book", command=add_book).pack(pady=5)
tk.Button(root, text="Search by Title", command=search_book).pack(pady=5)
tk.Button(root, text="Delete by ID", command=delete_book).pack(pady=5)
tk.Button(root, text="Display All", command=display_books).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

root.mainloop()