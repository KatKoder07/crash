import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.withdraw()

answer = messagebox.askyesno(
    "normal question",
    "crash computer?\n\nthis action is 100% irreversible"
)

if not answer:
    root.destroy()
    raise SystemExit

crash = tk.Toplevel()
crash.attributes("-fullscreen", True)
crash.configure(bg="#0078D7")
crash.config(cursor="none")

frame = tk.Frame(crash, bg="#0078D7")
frame.place(relx=0.5, rely=0.5, anchor="center")

sad = tk.Label(
    frame,
    text=":(",
    font=("Segoe UI", 90),
    fg="white",
    bg="#0078D7"
)
sad.pack(anchor="w")

message = tk.Label(
    frame,
    text="Your PC ran into a problem and needs to restart.\n"
         "We're just collecting some error info...",
    font=("Segoe UI", 20),
    fg="white",
    bg="#0078D7",
    justify="left"
)
message.pack(anchor="w", pady=10)

percent = tk.Label(
    frame,
    text="0% complete",
    font=("Segoe UI", 18),
    fg="white",
    bg="#0078D7"
)
percent.pack(anchor="w")

status = tk.Label(
    frame,
    text="",
    font=("Segoe UI", 12),
    fg="white",
    bg="#0078D7"
)
status.pack(anchor="w", pady=20)

def update():
    value = int(percent.cget("text").split("%")[0])

    if value < 100:
        value += random.randint(1, 8)
        value = min(value, 100)

        percent.config(text=f"{value}% complete")

        if value >= 100:
            status.config(text="just kidding")
            crash.after(2000, crash.destroy)
        else:
            crash.after(random.randint(150, 500), update)


update()

crash.bind("<Escape>", lambda e: crash.destroy())

root.mainloop()