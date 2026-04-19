import tkinter as tk
from tkinter import messagebox

# ---------------- DOUBLY LINKED LIST ---------------- #

class Node:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_begin(self, node):
        if self.head is None:
            self.head = self.tail = self.current = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def add_end(self, node):
        if self.tail is None:
            self.head = self.tail = self.current = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def delete_pos(self, pos):
        if self.head is None:
            return False

        temp = self.head
        count = 0

        while temp:
            if count == pos:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev

                return True
            temp = temp.next
            count += 1

        return False

    def traverse(self):
        songs = []
        temp = self.head
        while temp:
            songs.append(temp)
            temp = temp.next
        return songs

    def reverse(self):
        temp = self.head
        self.head, self.tail = self.tail, self.head

        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev


playlist = DoublyLinkedList()

# ---------------- FUNCTIONS ---------------- #

def add_begin():
    add_song("begin")

def add_end():
    add_song("end")

def add_song(mode):
    title = entry_title.get().strip()
    artist = entry_artist.get().strip()

    if title == "" or artist == "":
        messagebox.showwarning("Warning", "Fill all fields")
        return

    node = Node(title, artist)

    if mode == "begin":
        playlist.add_begin(node)
    else:
        playlist.add_end(node)

    clear_entries()
    update_display(f"Added: {title}")


def delete_song():
    try:
        pos = int(entry_pos.get())
    except:
        messagebox.showerror("Error", "Enter valid position")
        return

    if playlist.delete_pos(pos):
        update_display("Song deleted")
    else:
        messagebox.showerror("Error", "Invalid position")


def next_song():
    if playlist.current and playlist.current.next:
        playlist.current = playlist.current.next
        update_display("Next song")


def prev_song():
    if playlist.current and playlist.current.prev:
        playlist.current = playlist.current.prev
        update_display("Previous song")


def shuffle_playlist():
    playlist.reverse()
    update_display("Playlist shuffled")


def update_display(status=""):
    listbox.delete(0, tk.END)

    songs = playlist.traverse()

    if not songs:
        listbox.insert(tk.END, "No songs")
        current_label.config(text="Now Playing: None")
        return

    for i, s in enumerate(songs):
        listbox.insert(tk.END, f"{i}. {s.title} - {s.artist}")

    if playlist.current:
        current_label.config(
            text=f"Now Playing: {playlist.current.title} - {playlist.current.artist}"
        )

    status_label.config(text=f"Status: {status}")


def clear_entries():
    entry_title.delete(0, tk.END)
    entry_artist.delete(0, tk.END)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Playlist Manager")
root.geometry("700x500")
root.configure(bg="#e5e5e5")

# Title
tk.Label(root, text="🎵 Playlist Manager",
         font=("Segoe UI", 16, "bold"),
         bg="#e5e5e5").pack(pady=10)

# Input
frame_input = tk.Frame(root, bg="#e5e5e5")
frame_input.pack()

entry_title = tk.Entry(frame_input, width=25)
entry_title.grid(row=0, column=0, padx=10)
entry_title.insert(0, "Song Title")

entry_artist = tk.Entry(frame_input, width=25)
entry_artist.grid(row=0, column=1, padx=10)
entry_artist.insert(0, "Artist")

# Buttons
frame_btn = tk.Frame(root, bg="#e5e5e5")
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Add Start", bg="#d1d5db", width=12, command=add_begin).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Add End", bg="#d1d5db", width=12, command=add_end).grid(row=0, column=1, padx=5)

entry_pos = tk.Entry(frame_btn, width=5)
entry_pos.grid(row=0, column=2, padx=5)

tk.Button(frame_btn, text="Delete Pos", bg="#fca5a5", command=delete_song).grid(row=0, column=3, padx=5)

# Playlist Display
listbox = tk.Listbox(root, width=70, height=12, bg="#f3f4f6")
listbox.pack(pady=10)

# Player Controls
frame_player = tk.Frame(root, bg="#e5e5e5")
frame_player.pack()

tk.Button(frame_player, text="⏮", width=5, command=prev_song).grid(row=0, column=0, padx=10)
tk.Button(frame_player, text="⏭", width=5, command=next_song).grid(row=0, column=1, padx=10)
tk.Button(frame_player, text="🔀 Shuffle", command=shuffle_playlist).grid(row=0, column=2, padx=10)

# Now Playing
current_label = tk.Label(root, text="Now Playing: None",
                         font=("Segoe UI", 11),
                         bg="#e5e5e5")
current_label.pack(pady=10)

# Status
status_label = tk.Label(root, text="Status: Ready",
                        bg="#e5e5e5")
status_label.pack()

root.mainloop()