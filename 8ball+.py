import tkinter as tk
import random

choices = []
weights = []

def add_choice():

    text = entry_choice.get()
    weight = entry_weight.get()

    if text == "" or weight == "":
        result_label.config(text="Aizpildi abus laukus")
        return

    if not weight.isdigit():
        result_label.config(text="Svars jābūt skaitlim")
        return

    choices.append(text)
    weights.append(int(weight))

    listbox.insert(tk.END, f"{text} ({weight})")

    entry_choice.delete(0, tk.END)
    entry_weight.delete(0, tk.END)

    result_label.config(text="")


def pick_choice():

    if len(choices) == 0:
        result_label.config(text="Saraksts ir tukšs")

    else:
        result = random.choices(choices, weights=weights)[0]

        result_label.config(text="Rezultāts: " + result)


root = tk.Tk()
root.title("Magic 8 Ball +")
root.geometry("340x380")


title_label = tk.Label(
    root,
    text="Magic 8 Ball +",
    font=("Arial", 14, "bold")
)

title_label.pack(pady=8)


tk.Label(root, text="Izvēle:").pack()

entry_choice = tk.Entry(root, width=25)
entry_choice.pack(pady=3)


tk.Label(root, text="Svars (1-10):").pack()

entry_weight = tk.Entry(root, width=10)
entry_weight.pack(pady=3)


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
