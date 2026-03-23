import tkinter as tk

root = tk.Tk()
root.title("Magic 8 Ball")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Pievienot")
button.pack()

root.mainloop()