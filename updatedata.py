import tkinter as tk
import os
import mysql.connector
from tempCodeRunnerFile import db

def get_login_customer_id(cursor):
    # Fetch the last customer ID from the database
    cursor.execute("SELECT cust_id FROM customer2 where login='1'")
    last_id = cursor.fetchone()
    return last_id[0]



def update_data():
    cursor = db.cursor()

    fname = fname_entry.get()
    lname = lname_entry.get()
    dob = dob_entry.get()
    gender = gender_entry.get()
    ph = ph_entry.get()
    email = email_entry.get()
    passno = passno_entry.get()
    mstatus = mstatus_entry.get()
    ppsno = ppsno_entry.get()
    password = password_entry.get()
    login = 0
    
    clientno = get_login_customer_id(cursor)
    
    cursor.execute("""
    UPDATE customer2
    SET 
        cust_fname = %s,
        cust_lname = %s,
        cust_DOB = %s,
        cust_gender = %s,
        cust_mob_number = %s,
        cust_email = %s,
        cust_passport_number = %s,
        cust_martial_status = %s,
        cust_ppS_number = %s,
        cust_password = %s
    WHERE 
        cust_id = %s;
    """, (fname, lname, dob, gender, ph, email, passno, mstatus, ppsno, password, clientno))

    cursor.execute("""
    UPDATE customer
    SET 
        cust_fname = %s,
        cust_lname = %s,
        cust_DOB = %s,
        cust_gender = %s,
        cust_mob_number = %s,
        cust_email = %s,
        cust_passport_number = %s,
        cust_martial_status = %s,
        cust_ppS_number = %s
    WHERE 
        cust_id = %s;
    """, (fname, lname, dob, gender, ph, email, passno, mstatus, ppsno, clientno))

    db.commit()
    db.close()
    
    # Clear the entry fields after update
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    ph_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    passno_entry.delete(0, tk.END)
    mstatus_entry.delete(0, tk.END)
    ppsno_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    # Show success message
    success_label = tk.Label(root, text="Data updated successfully!", bg="lightgreen")
    success_label.place(x=150, y=150)

 
def open_code_1():
    root.destroy()
    os.system("python userinterface.py")


cursor = db.cursor()

root = tk.Tk()
root.title("User Registration")
root.geometry("500x600")
frame = tk.Frame(root, width=500, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 30)
large_font1 = ('Verdana', 13)

user_label = tk.Label(frame, text="User Registration", bg="#2C3E50", fg="Orange", font=large_font)
user_label.place(x=80, y=35)

button1 = tk.Button(frame, text="Back", fg="red", command=open_code_1)
button1.place(x=10, y=10)

fname_label = tk.Label(frame, text="First Name:", bg="silver", font=large_font1)
fname_label.place(x=80, y=140)
fname_entry = tk.Entry(frame)
fname_entry.place(x=290, y=140)

lname_label = tk.Label(frame, text="Last Name:", bg="silver", font=large_font1)
lname_label.place(x=80, y=180)
lname_entry = tk.Entry(frame)
lname_entry.place(x=290, y=180)

dob_label = tk.Label(frame, text="DOB:", bg="silver", font=large_font1)
dob_label.place(x=80, y=220)
dob_entry = tk.Entry(frame)
dob_entry.place(x=290, y=220)

gender_label = tk.Label(frame, text="Gender:", bg="silver", font=large_font1)
gender_label.place(x=80, y=260)
gender_entry = tk.Entry(frame)
gender_entry.place(x=290, y=260)

ph_label = tk.Label(frame, text="Phone Number:", bg="silver", font=large_font1)
ph_label.place(x=80, y=300)
ph_entry = tk.Entry(frame)
ph_entry.place(x=290, y=300)

email_label = tk.Label(frame, text="Email Address:", bg="silver", font=large_font1)
email_label.place(x=80, y=340)
email_entry = tk.Entry(frame)
email_entry.place(x=290, y=340)

passno_label = tk.Label(frame, text="PassportNumber:", bg="silver", font=large_font1)
passno_label.place(x=80, y=380)
passno_entry = tk.Entry(frame)
passno_entry.place(x=290, y=380)

mstatus_label = tk.Label(frame, text="Marital Status:", bg="silver", font=large_font1)
mstatus_label.place(x=80, y=420)
mstatus_entry = tk.Entry(frame)
mstatus_entry.place(x=290, y=420)

ppsno_label = tk.Label(frame, text="Pps Number:", bg="silver", font=large_font1)
ppsno_label.place(x=80, y=460)
ppsno_entry = tk.Entry(frame)
ppsno_entry.place(x=290, y=460)

password_label = tk.Label(frame, text="Password:", bg="silver", font=large_font1)
password_label.place(x=80, y=500)
password_entry = tk.Entry(frame)
password_entry.place(x=290, y=500)

submit_button = tk.Button(frame, text="Update", bg="#1ABC9C", command=update_data, font=large_font1)
submit_button.place(x=180, y=540)

root.mainloop()
