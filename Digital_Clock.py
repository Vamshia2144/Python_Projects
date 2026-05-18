# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:48:58 2026

@author: avams
"""

import tkinter as tk
from datetime import datetime

def update_clock():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    current_date = now.strftime("%A, %d-%m-%Y")
    current_time_label.config(text=current_time)
    current_date_label.config(text=current_date)
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")

current_time_label = tk.Label(root, font=("Arial", 22), fg="blue", justify="center")
current_date_label = tk.Label(root, font=("Arial", 25), fg="red", justify="center")

current_time_label.pack(pady=20)
current_date_label.pack()

update_clock()
root.mainloop()