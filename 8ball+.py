import tkinter as tk
import random

choices = []
weights = []

def add_choice():
    text = entry_choice.get()
    weight = entry_weight.get()

    if text != "" and weight.isdigit():
        choices.append(text)
        weights.append(int(weight))

        listbox.insert(tk.END, f"{text} ({weight})")

        entry_choice.delete(0, tk.END)
        entry_weight.delete(0, tk.END)

def pick_choice():
    if len(choices) > 0:
        result = random.choices(choices, weights=weights)[0]
        result_label.config(text=result)

def save_choices():
    with open("choices.txt", "w") as file:
        for i in range(len(choices)):
            file.write(f"{choices[i]},{weights[i]}\n")

def load_choices():
    choices.clear()
    weights.clear()
    listbox.delete(0, tk.END)

    try:
        with open("choices.txt", "r") as file:
            for line in file:
                text, weight = line.strip().split(",")
                choices.append(text)
                weights.append(int(weight))
                listbox.insert(tk.END, f"{text} ({weight})")
    except:
        result_label.config(text="Nav faila")

root = tk.Tk()
root.title("Magic 8 Ball +")

tk.Label(root, text="Ievadi izvēli:").pack()

entry_choice = tk.Entry(root)
entry_choice.pack()

tk.Label(root, text="Svars (1-10):").pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Button(root, text="Pievienot", command=add_choice).pack()

listbox = tk.Listbox(root)
listbox.pack()

tk.Button(root, text="Izvēlēties", command=pick_choice).pack()

result_label = tk.Label(root, text="")
result_label.pack()

tk.Button(root, text="Saglabāt", command=save_choices).pack()

tk.Button(root, text="Ielādēt", command=load_choices).pack()

root.mainloop()