
import tkinter as tk
def add_choice ():
  text = entry.get()
  listbox.insert(tk.END, text)
  
root = tk.Tk()
root.title("Magic 8 Ball +")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Pievienot")
button.pack()

listbox = tk.Listbox(root)
listbox.pack()

import random

def pick_choice():
    if listbox.size() == 0:
        result_label.config(text="Saraksts ir tukšs")
    else:
        random_choice = random.choice(listbox.get(0, tk.END))
        result_label.config(text=random_choice)
root.mainloop()

