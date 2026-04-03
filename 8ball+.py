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

    weight = int(weight)

    if weight < 1 or weight > 10:
        result_label.config(text="Svars jābūt no 1 līdz 10")
        return

    choices.append(text)
    weights.append(weight)

    listbox.insert(tk.END, f"{text} ({weight})")

    entry_choice.delete(0, tk.END)
    entry_weight.delete(0, tk.END)

    result_label.config(text="")


def pick_choice():

    if len(choices) == 0:
        result_label.config(text="Nav izvēļu")
    else:
        result = random.choices(choices, weights=weights)[0]
        result_label.config(text="Rezultāts: " + result)


root = tk.Tk()
root.title("Magic 8 Ball +")
root.geometry("360x400")


title_label = tk.Label(
    root,
    text="Magic 8 Ball +",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)


input_frame = tk.Frame(root)
input_frame.pack()


tk.Label(input_frame, text="Izvēle").grid(row=0, column=0)
tk.Label(input_frame, text="Svars (1-10)").grid(row=0, column=1)


entry_choice = tk.Entry(input_frame, width=18)
entry_choice.grid(row=1, column=0, padx=5)


entry_weight = tk.Entry(input_frame, width=8)
entry_weight.grid(row=1, column=1, padx=5)


add_button = tk.Button(
    input_frame,
    text="Pievienot",
    command=add_choice
)
add_button.grid(row=1, column=2, padx=5)


listbox = tk.Listbox(
    root,
    width=35,
    height=7
)
listbox.pack(pady=15)


pick_button = tk.Button(
    root,
    text="Izvēlēties",
    command=pick_choice,
    width=18,
    height=2
)
pick_button.pack()


result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=10)


root.mainloop()
