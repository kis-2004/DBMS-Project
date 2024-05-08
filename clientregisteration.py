import tkinter as tk
import os
import mysql.connector
from tempCodeRunnerFile import db

def get_last_customer_id(cursor):
    # Fetch the last customer ID from the database
    cursor.execute("SELECT cust_id FROM customer2 ORDER BY cust_id DESC LIMIT 1")
    last_id = cursor.fetchone()
    
    if last_id:
        last_id = int(last_id[0][4:])  # Extract numeric part and convert to int
    else:
        last_id = 0
    
    return last_id

def generate_customer_id(cursor):
    last_id = get_last_customer_id(cursor)
    
    # Increment the last ID by 1
    new_id = last_id + 1
    
    # Convert the new ID to the format 'CUSTxxx'
    return f'CUST{str(new_id).zfill(3)}'

def submit_data():
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
    login=0
    
    clientno = generate_customer_id(cursor)
    
    sql = "INSERT INTO customer2(cust_id,cust_fname,cust_lname,cust_DOB,cust_gender,cust_mob_number,cust_email,cust_passport_number,cust_martial_status,cust_ppS_number,cust_password,login) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (clientno, fname, lname, dob, gender, ph, email, passno, mstatus, ppsno, password,login)
    cursor.execute(sql, values)

    sql2 = "INSERT INTO customer(cust_id,cust_fname,cust_lname,cust_DOB,cust_gender,cust_mob_number,cust_email,cust_passport_number,cust_martial_status,cust_ppS_number) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values2 = (clientno, fname, lname, dob, gender, ph, email, passno, mstatus, ppsno)
    cursor.execute(sql2, values2)

    

    db.commit()
    
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

    success_label = tk.Label(root, text="Registration Successful!", bg="lightgreen")
    success_label.place(x=170, y=20)
    clientid_label = tk.Label(root, text="Your Client Id is :" + clientno)
    clientid_label.place(x=140, y=400)
 
def open_code_1():
    root.destroy()
    os.system("python loginpage.py")


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

submit_button = tk.Button(frame, text="Submit", bg="#1ABC9C", command=submit_data, font=large_font1)
submit_button.place(x=180, y=540)

root.mainloop()
