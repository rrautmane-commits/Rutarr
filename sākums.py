import tkinter as tk
import random

def add_choice():

    text = entry.get()

    if text == "":
        result_label.config(text="Lūdzu ievadi izvēli")
    else:
        listbox.insert(tk.END, text)
        
        entry.delete(0, tk.END)

        result_label.config(text="")

def pick_choice():

    if listbox.size() == 0:
        result_label.config(text="Saraksts ir tukšs")

    else:
        random_choice = random.choice(listbox.get(0, tk.END))
        result_label.config(text=random_choice)

root = tk.Tk()
root.title("Magic 8 Ball +")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Pievienot", command=add_choice)
button.pack()

listbox = tk.Listbox(root)
listbox.pack()

pick_button = tk.Button(root, text="Izvēlēties", command=pick_choice)
pick_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
