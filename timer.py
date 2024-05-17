import tkinter as tk
from tkinter import simpledialog
import time

def start_countdown(minutes):
    countdown_time = int(minutes) * 60  # Convert minutes to seconds

    def update_timer():
        nonlocal countdown_time
        minutes, seconds = divmod(abs(countdown_time), 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        label.config(text=time_str)

        if countdown_time < 0:
            label.config(fg='red')
        else:
            label.config(fg='black')

        countdown_time -= 1
        root.after(1000, update_timer)

    update_timer()

root = tk.Tk()
root.title("Countdown Timer")

# Ask the user to enter the number of minutes
minutes = simpledialog.askinteger("Input", "Enter the number of minutes:", minvalue=1, maxvalue=60)

label = tk.Label(root, font=('Helvetica', 48), text="00:00")
label.pack(padx=20, pady=20)

start_button = tk.Button(root, text="Start", command=lambda: start_countdown(minutes))
start_button.pack(pady=10)

root.mainloop()
