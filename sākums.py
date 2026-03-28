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

        result_label.config(text="Rezultāts: " + random_choice)


root = tk.Tk()
root.title("Magic 8 Ball +")
root.geometry("320x350")


title_label = tk.Label(
    root,
    text="Magic 8 Ball +",
    font=("Arial", 14, "bold")
)

title_label.pack(pady=8)


entry_label = tk.Label(
    root,
    text="Ievadi izvēli:"
)

entry_label.pack()


entry = tk.Entry(root, width=25)

entry.pack(pady=5)


button = tk.Button(
    root,
    text="Pievienot",
    command=add_choice
)

button.pack(pady=5)


listbox = tk.Listbox(
    root,
    width=30,
    height=6
)

listbox.pack(pady=10)


pick_button = tk.Button(
    root,
    text="Izvēlēties",
    command=pick_choice,
    width=15
)

pick_button.pack(pady=5)


result_label = tk.Label(
    root,
    text="",
    font=("Arial", 11)
)

result_label.pack(pady=10)


root.mainloop()
