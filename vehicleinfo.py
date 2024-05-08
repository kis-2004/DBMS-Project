import tkinter as tk
import os
import mysql.connector
from tempCodeRunnerFile import db

def get_login_customer_id(cursor):
    cursor.execute("SELECT cust_id FROM customer2 where login='1'")
    last_id = cursor.fetchone()
    return last_id[0]

def get_last_vehicle_id(cursor):
    cursor.execute("SELECT vehicle_id FROM vehicle ORDER BY vehicle_id DESC LIMIT 1")
    last_id = cursor.fetchone()
    if last_id:
        last_id = int(last_id[0][3:])
    else:
        last_id = 0
    return last_id

def generate_vehicle_id(cursor):
    last_id = get_last_vehicle_id(cursor)
    new_id = last_id + 1
    return f'VEH{str(new_id).zfill(3)}'

def get_last_nok_id(cursor):
    cursor.execute("SELECT dependent_nok_id FROM vehicle ORDER BY dependent_nok_id DESC LIMIT 1")
    last_id = cursor.fetchone()
    if last_id:
        last_id = int(last_id[0][3:])
    else:
        last_id = 0
    return last_id

def generate_nok_id(cursor):
    last_id = get_last_nok_id(cursor)
    new_id = last_id + 1
    return f'NOK{str(new_id).zfill(3)}'

def get_last_policy_id(cursor):
    cursor.execute("SELECT policy_id FROM vehicle ORDER BY policy_id DESC LIMIT 1")
    last_id = cursor.fetchone()
    if last_id:
        last_id = int(last_id[0][3:])
    else:
        last_id = 0
    return last_id

def generate_policy_id(cursor):
    last_id = get_last_policy_id(cursor)
    new_id = last_id + 1
    return f'POL{str(new_id).zfill(3)}'

def submit_data():
    cursor = db.cursor()
    regno = regno_entry.get()
    vehval = vehval_entry.get()
    vehtyp = vehtyp_entry.get()
    vehsize = vehsize_entry.get()
    seats = seats_entry.get()
    manufact = manufact_entry.get()
    chasino = chasino_entry.get()
    vehno = vehno_entry.get()
    modno = modno_entry.get()
    
    cust_id = get_login_customer_id(cursor)
    policyno = generate_policy_id(cursor)
    nok = generate_nok_id(cursor)
    veh_id = generate_vehicle_id(cursor)
    
    sql = """INSERT INTO vehicle (vehicle_id, cust_id, policy_id, dependent_nok_id, vehicle_registration_number, 
             vehicle_value, vehicle_type, vehicle_size, vehicle_number_of_seat, vehicle_manufacturer, 
             vehicle_chasis_number, vehicle_number, vehicle_model_number) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    values = (veh_id, cust_id, policyno, nok, regno, vehval, vehtyp, vehsize, seats, manufact, chasino, vehno, modno)
    cursor.execute(sql, values)
    db.commit()
    
    regno_entry.delete(0, tk.END)
    vehval_entry.delete(0, tk.END)
    vehtyp_entry.delete(0, tk.END)
    vehsize_entry.delete(0, tk.END)
    seats_entry.delete(0, tk.END)
    manufact_entry.delete(0, tk.END)
    chasino_entry.delete(0, tk.END)
    vehno_entry.delete(0, tk.END)
    modno_entry.delete(0, tk.END)

    success_label = tk.Label(root, text="Registration Successful!", bg="lightgreen")
    success_label.place(x=170, y=20)
    clientid_label = tk.Label(root, text="Your vehicle Id is: " + veh_id)
    clientid_label.place(x=140, y=400)

def view_info():
    root.destroy()
    os.system("python viewvehicleinfo.py")

def open_code_1():
    root.destroy()
    os.system("python userinterface.py")

cursor = db.cursor()

root = tk.Tk()
root.title("Vehicle Info")
root.geometry("500x600")
frame = tk.Frame(root, width=500, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 30)
large_font1 = ('Verdana', 13)

user_label = tk.Label(frame, text="Vehicle Registration", bg="#2C3E50", fg="Orange", font=large_font)
user_label.place(x=80, y=35)

button1 = tk.Button(frame, text="Back", fg="red", command=open_code_1)
button1.place(x=10, y=10)

regno_label = tk.Label(frame, text="Registration No:", bg="silver", font=large_font1)
regno_label.place(x=80, y=140)
regno_entry = tk.Entry(frame)
regno_entry.place(x=290, y=140)

vehval_label = tk.Label(frame, text="Vehicle Value:", bg="silver", font=large_font1)
vehval_label.place(x=80, y=180)
vehval_entry = tk.Entry(frame)
vehval_entry.place(x=290, y=180)

vehtyp_label = tk.Label(frame, text="Vehicle Type:", bg="silver", font=large_font1)
vehtyp_label.place(x=80, y=220)
vehtyp_entry = tk.Entry(frame)
vehtyp_entry.place(x=290, y=220)

vehsize_label = tk.Label(frame, text="Vehicle Size:", bg="silver", font=large_font1)
vehsize_label.place(x=80, y=260)
vehsize_entry = tk.Entry(frame)
vehsize_entry.place(x=290, y=260)

seats_label = tk.Label(frame, text="No of Seats:", bg="silver", font=large_font1)
seats_label.place(x=80, y=300)
seats_entry = tk.Entry(frame)
seats_entry.place(x=290, y=300)

manufact_label = tk.Label(frame, text="Manufacturer:", bg="silver", font=large_font1)
manufact_label.place(x=80, y=340)
manufact_entry = tk.Entry(frame)
manufact_entry.place(x=290, y=340)

chasino_label = tk.Label(frame, text="Chasis No:", bg="silver", font=large_font1)
chasino_label.place(x=80, y=380)
chasino_entry = tk.Entry(frame)
chasino_entry.place(x=290, y=380)

vehno_label = tk.Label(frame, text="Vehicle No:", bg="silver", font=large_font1)
vehno_label.place(x=80, y=420)
vehno_entry = tk.Entry(frame)
vehno_entry.place(x=290, y=420)

modno_label = tk.Label(frame, text="Model No:", bg="silver", font=large_font1)
modno_label.place(x=80, y=460)
modno_entry = tk.Entry(frame)
modno_entry.place(x=290, y=460)

submit_button = tk.Button(frame, text="Submit", bg="#1ABC9C", command=submit_data, font=large_font1)
submit_button.place(x=80, y=520)

view_info_button = tk.Button(frame, text="View Info", bg="#3498DB", command=view_info, font=large_font1)
view_info_button.place(x=290, y=520)

root.mainloop()
