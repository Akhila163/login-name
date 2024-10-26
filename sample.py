import tkinter as tk
from tkinter import messagebox
def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    if username =="usename"and password == "password":
        messagebox.showinfo("Login success","Welcome!")
    else:
        messagebox.showerror("Login failed","invalid credentials.please try again.")
root = tk.Tk()
root.title(" Tkinter App")
root.geometry("300x200")
Label_username = tk.Label(root,text="Username:")
Label_username.pack(pady=10) 
entry_username = tk.Entry(root) 
entry_username.pack(pady=5)
Label_password = tk.Label(root,text="password:")
Label_password.pack(pady=10) 
entry_password = tk.Entry(root,show="*") 
entry_password.pack(pady=5)
button_login = tk.Button(root,text="Login",command=validate_login)
button_login.pack(pady=20)
root.mainloop()
                
