# Login Form.

import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "1234":
        result_label.config(text="Login successfull")
    else:
        result_label.config(text="Invalid usernme or Password")

root = tk.Tk()
root.title("Login Form")
root.geometry("400x300")

tk.Label(root, text="Username").pack(pady=10)

username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack(pady=10) 

password_entry = tk.Entry(root, show="*")   
password_entry.pack()

tk.Button(root, text="login", command=login).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
