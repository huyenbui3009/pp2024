import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importing ttk for Combobox

window = tk.Tk()
window.title("GUI TEST")
window.geometry("1000x1000")

# Frame as a container for widgets
frame = tk.Frame(window, width=900, height=900)
frame.pack()

# Label widget
label = tk.Label(frame, text="Hello, this is text in GUI", font=("Arial", 24))
label.pack(padx=100, pady=20)

# Entry widget
# entry_var = tk.StringVar()
entry = tk.Entry(frame, text="Default text" )
entry.pack(pady=10)

# Checkbutton widget
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, text="checkbutton", variable=check_var)
checkbutton.pack(pady=10)

# Radiobutton widget
radio_var = tk.StringVar()
radio_var.set("Option 1")  # Setting a default value
radio1 = tk.Radiobutton(frame, text="Option 1", variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(frame, text="Option 2", variable=radio_var, value="Option 2")
radio1.pack()
radio2.pack(pady=10)

# Listbox widget
listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE)
icts = ["ICT", "I See Tea", "Icy Tea", "Ice City"]

for item in icts:
    listbox.insert(icts.index(item), item)
listbox.pack(pady=10)

# Combobox widget
combo_var = tk.StringVar()
combobox = ttk.Combobox(frame, textvariable=combo_var, values=["Option A", "Option B", "Option C"])
combobox.pack(pady=10)

def onClick():
    messagebox.showinfo(message="Button clicked")

# Button 1
button1 = tk.Button(frame, text="Button 1", command=onClick)
button1.pack(pady=10)

def button_click():
    label.config(text="Button Clicked!")

# Button 2
button2 = tk.Button(frame, text="Click Me!", command=button_click)
button2.pack()

window.mainloop()

# sub = tk.Toplevel(window)
# sub.title("Students")
# sub.geometry("600x400")
# sub.mainloop()