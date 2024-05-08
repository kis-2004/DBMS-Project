import tkinter as tk
import os

bg="#2C3E50"
textColor = "white"
btnColor = "#5bc0be"

def open_code_1():
    root.destroy()
    os.system("python policyregister.py")

def open_code_2():
    root.destroy()
    os.system("python policychange.py")
    
def open_code_3():
    root.destroy()
    os.system("python userinterface.py")
    
def open_code_4():
    root.destroy()
    os.system("python policyrenew.py")


root = tk.Tk()
root.title("User Interface")
root.geometry("470x500")
frame = tk.Frame(root, width=500, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana',30)
large_font1 = ('Verdana', 12)
large_font2 = ('Verdana', 15)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_3)
button1.place(x=10,y=10)

admin_label = tk.Label(frame, text="Policy",bg="#2C3E50",fg="Orange",font=large_font)
admin_label.place(x=175,y=45)

register_label = tk.Label(frame, text="Register Policy?",bg=bg,fg=textColor,font=large_font2)
register_label.place(x=30,y=160)

button1 = tk.Button(frame, text="Register", command=open_code_1,font=large_font1,bg="#5bc0be")
button1.place(x=40, y=220)

search_label = tk.Label(frame, text="Change Policy?",bg=bg,fg=textColor,font=large_font2)
search_label.place(x=285,y=160)

button2 = tk.Button(frame, text="Change", command=open_code_2,font=large_font1,bg="#5bc0be")
button2.place(x=285,y=220)

check_label = tk.Label(frame, text="Renew Policy?",bg=bg,fg=textColor,font=large_font2)
check_label.place(x=160,y=330)

button3 = tk.Button(frame, text="Renew", command=open_code_4,font=large_font1,bg="#5bc0be")
button3.place(x=180,y=390)


root.mainloop()
