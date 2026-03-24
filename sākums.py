import tkinter as tk
def add_choice ():
  text = entry.get()
  listbox.insert(tk.END, text)
  
root = tk.Tk()
root.title("Magic 8 Ball")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Pievienot")
button.pack()

listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()

