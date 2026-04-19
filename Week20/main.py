import tkinter as tk
from tkinter import messagebox

# ---------------- DATA ---------------- #

scores = []

# ---------------- FUNCTIONS ---------------- #

def add_score():
    try:
        score = int(entry_score.get())
    except:
        messagebox.showerror("Error", "Enter valid number")
        return

    scores.append(score)
    entry_score.delete(0, tk.END)

    update_display("Score Added")


def display_scores():
    listbox.delete(0, tk.END)

    if not scores:
        listbox.insert(tk.END, "No scores yet")
        return

    for i, s in enumerate(scores):
        listbox.insert(tk.END, f"{i+1}. Score: {s}")


def calculate_stats():
    if not scores:
        messagebox.showinfo("Info", "No data")
        return

    # Linear traversal
    min_score = scores[0]
    max_score = scores[0]

    for s in scores:
        if s < min_score:
            min_score = s
        if s > max_score:
            max_score = s

    # Mode using frequency count
    freq = {}
    for s in scores:
        freq[s] = freq.get(s, 0) + 1

    mode = max(freq, key=freq.get)

    min_label.config(text=f"Min: {min_score}")
    max_label.config(text=f"Max: {max_score}")
    mode_label.config(text=f"Mode: {mode}")


def update_display(status=""):
    display_scores()
    calculate_stats()
    status_label.config(text=f"Status: {status}")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Exam Score Tracker")
root.geometry("700x450")
root.configure(bg="#f0f2f5")

# Title
tk.Label(root, text="📊 Score Analytics Dashboard",
         font=("Segoe UI", 16, "bold"),
         bg="#f0f2f5").pack(pady=10)

# Input
frame_input = tk.Frame(root, bg="#f0f2f5")
frame_input.pack()

entry_score = tk.Entry(frame_input, width=20)
entry_score.grid(row=0, column=0, padx=10)
entry_score.insert(0, "Enter Score")

tk.Button(frame_input, text="Add Score",
          bg="#d1d5db", width=12,
          command=add_score).grid(row=0, column=1, padx=5)

# Main Layout
frame_main = tk.Frame(root, bg="#f0f2f5")
frame_main.pack(pady=10)

# Left: Score List
frame_list = tk.Frame(frame_main, bg="#ffffff", bd=1, relief="solid")
frame_list.grid(row=0, column=0, padx=10)

tk.Label(frame_list, text="Scores",
         bg="#ffffff", font=("Segoe UI", 12, "bold")).pack()

listbox = tk.Listbox(frame_list, width=30, height=12, bg="#f9fafb")
listbox.pack(padx=10, pady=10)

# Right: Stats Panel
frame_stats = tk.Frame(frame_main, bg="#ffffff", bd=1, relief="solid")
frame_stats.grid(row=0, column=1, padx=10)

tk.Label(frame_stats, text="Statistics",
         bg="#ffffff", font=("Segoe UI", 12, "bold")).pack(pady=5)

min_label = tk.Label(frame_stats, text="Min: -", bg="#ffffff", font=("Segoe UI", 11))
min_label.pack(pady=5)

max_label = tk.Label(frame_stats, text="Max: -", bg="#ffffff", font=("Segoe UI", 11))
max_label.pack(pady=5)

mode_label = tk.Label(frame_stats, text="Mode: -", bg="#ffffff", font=("Segoe UI", 11))
mode_label.pack(pady=5)

tk.Button(frame_stats, text="Refresh Stats",
          bg="#60a5fa", command=calculate_stats).pack(pady=10)

# Status
status_label = tk.Label(root, text="Status: Ready",
                        bg="#f0f2f5")
status_label.pack(pady=10)

root.mainloop()