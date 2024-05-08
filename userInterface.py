import tkinter as tk
import os
from tempCodeRunnerFile import db
import mysql

bg="#2C3E50"
textColor = "white"
btnColor = "#5bc0be"

def open_code_1():
    root.destroy()
    os.system("python myinfo.py")

def open_code_2():
    root.destroy()
    os.system("python policies.py")
    
def open_code_3():
    cursor=db.cursor()
    cursor.execute("UPDATE customer2 SET login = '0'")
    db.commit()
    db.close()
    root.destroy()
    os.system("python loginpage.py")

        
    
def open_code_4():
    root.destroy()
    os.system("python claims.py")

def open_code_5():
    root.destroy()
    os.system("python vehicleinfo.py")

def open_code_6():
    cursor=db.cursor()
    def get_login_customer_id(cursor):
        cursor.execute("SELECT cust_id FROM customer2 where login='1'")
        last_id = cursor.fetchone()
        return last_id[0]
    
    cust_id = get_login_customer_id(cursor)

    sql=("""delete from customer where cust_id=%s;""")
    values=(cust_id,)
    cursor.execute(sql,values)
    sql=("""delete from customer2 where cust_id=%s;""")
    cursor.execute(sql,values)
    
    sql=("""delete from vehicle where cust_id=%s;""")
    cursor.execute(sql,values)

    db.commit()

    root.destroy()
    os.system("python loginpage.py")



    

root = tk.Tk()
root.title("User Interface")
root.geometry("500x500")
frame = tk.Frame(root, width=500, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana',30)
large_font1 = ('Verdana', 12)
large_font2 = ('Verdana', 15)

logoutbutton1 = tk.Button(frame, text="Log Out",bg="light grey",fg="red", command=open_code_3)
logoutbutton1.place(x=10,y=10)

admin_label = tk.Label(frame, text="Welcome User!",bg="#2C3E50",fg="Orange",font=large_font)
admin_label.place(x=80,y=45)

register_label = tk.Label(frame, text="View and Update Info?",bg=bg,fg=textColor,font=large_font2)
register_label.place(x=30,y=160)

button1 = tk.Button(frame, text="My Info", command=open_code_1,font=large_font1,bg="#5bc0be")
button1.place(x=40, y=220)

policy_label = tk.Label(frame, text="Policy Selection?",bg=bg,fg=textColor,font=large_font2)
policy_label.place(x=285,y=160)

button2 = tk.Button(frame, text="Policies", command=open_code_2,font=large_font1,bg="#5bc0be")
button2.place(x=285,y=220)

calims_label = tk.Label(frame, text="Claim Insurance?",bg=bg,fg=textColor,font=large_font2)
calims_label.place(x=30,y=330)

button3 = tk.Button(frame, text="Claims", command=open_code_4,font=large_font1,bg="#5bc0be")
button3.place(x=45,y=390)

new_label = tk.Label(frame, text="Update Vehicle Info?",bg=bg,fg=textColor,font=large_font2)
new_label.place(x=285,y=330)

button4 = tk.Button(frame, text="Vehicle Info", command=open_code_5,font=large_font1,bg="#5bc0be")
button4.place(x=285,y=390)

button5 = tk.Button(frame, text="Delete and Logout", fg="red", command=open_code_6, bg="light grey")
button5.place(x=370, y=10)  # Position in the top right corner

root.mainloop()
