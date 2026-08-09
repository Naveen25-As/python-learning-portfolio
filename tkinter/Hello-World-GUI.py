# Hello World GUI.

import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Hello World GUI")
root.geometry("300x200")

# create a label widget
label = tk.Label(root, text="Hello, World!", font=("Arial", 24))
label.pack(pady=50)

# Run the application
root.mainloop()