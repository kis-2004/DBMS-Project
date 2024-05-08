import tkinter as tk
import os

bg="#2C3E50" #bg color of the window in this case blue similarly text and button color
textColor = "white"
btnColor = "#5bc0be"

def open_code_1():
    root.destroy()# close current window
    os.system("python userlogin.py") #run code userlogin.py which inturn opens another window
    
def open_code_4():
    root.destroy()
    os.system("python clientregisteration.py")

root = tk.Tk()
root.title("login")# title of the page
root.geometry("500x350") #size of the page
frame = tk.Frame(root, width=500, height=500, bg=bg)
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 40) #different types of fonts
large_font1 = ('Verdana', 12)
large_font2 = ('Verdana', 15)
large_font3 = ('Arial', 10,'italic')

motto_label = tk.Label(frame, text="unlimited tension free insurance for any vehicle",bg=bg,fg=textColor,font=large_font3)
motto_label.place(x=130,y=105)#creation of label along with its positioning text and font

login_label = tk.Label(frame, text="Insta Insurance",bg=bg,fg="orange",font=large_font)
login_label.place(x=50,y=35)

user_label = tk.Label(frame, text="Already a user?",bg=bg,fg=textColor,font=large_font2)
user_label.place(x=40,y=160)

button1 = tk.Button(frame, text="User Login",bg=btnColor,fg="black", command=open_code_1,font=large_font1)
button1.place(x=60,y=225)#creation of buttom along with its positioning text font and command to be executed when clicked

staff_label = tk.Label(frame, text="New User?",bg=bg,fg=textColor,font=large_font2)
staff_label.place(x=300,y=160)

button2 = tk.Button(frame, text="Register",bg=btnColor,fg="black", command=open_code_4,font=large_font1)
button2.place(x=315,y=225)


root.mainloop()

#client registration.py refer

