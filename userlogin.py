import tkinter as tk
from tempCodeRunnerFile import db
import os
import mysql

def open_code_1():
    root.destroy()
    os.system("python userInterface.py")

def open_code_2():
    root.destroy()
    os.system("python loginpage.py")

def check_credentials():
    clientno = id_box.get()
    email = email_box.get()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM customer2 WHERE cust_id = %s AND cust_password = %s", (clientno, email))
    
    row = cursor.fetchone()
    
    if row:
        success_label = tk.Label(root, text="Login successful!")
        success_label.place(x=150, y=150)
        print("Client ID:", clientno)
        sql = "UPDATE customer2 SET login = '1' WHERE cust_id = %s"
        values = (clientno,)  # Tuple with one element
        try:
            cursor.execute(sql, values)
            db.commit()
            db.close() 
            open_code_1()
            root.destroy()
        except mysql.connector.Error as err:
            print("Error:", err)
    else:
        error_label = tk.Label(root, text="Invalid username or password.", bg="red")
        error_label.place(x=150, y=150)



root = tk.Tk()
root.title("User Login")
root.geometry("400x250")
frame = tk.Frame(root, width=350, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 15)
large_font1 = ('Verdana', 10)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_2)
button1.place(x=10,y=10)

user_label = tk.Label(frame, text="User Login",bg="#2C3E50",fg="Orange",font=large_font)
user_label.place(x=125,y=15)

id_label = tk.Label(frame, text="Enter Client Id :",bg="#2C3E50",fg="white",font=large_font1)
id_label.place(x=50, y=80)
id_box = tk.Entry(frame)
id_box.place(x=180, y=80)
email_label = tk.Label(frame, text="Enter password :",bg="#2C3E50",fg="white",font=large_font1)
email_label.place(x=50, y=120)
email_box = tk.Entry(frame)
email_box.place(x=180, y=120)

button = tk.Button(frame, text="Login", command=check_credentials,bg="#1ABC9C")
button.place(x=180, y=180)

message = tk.Label(frame, text="")


root.mainloop()
