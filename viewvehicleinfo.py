import tkinter as tk
from tkinter import ttk
import mysql.connector
import os
from tempCodeRunnerFile import db

c = db.cursor()

def go_back():
    root.destroy()
    os.system("python userinterface.py")

root = tk.Tk()
root.title("Vehicle Data")

frame = tk.Frame(root, padx=40, pady=40, bg='#2C3E50')

# Fetching data of the first customer from the database
c.execute(
"""SELECT vehicle_id,vehicle_registration_number,vehicle_value,vehicle_type,vehicle_size,vehicle_number_of_seat,vehicle_manufacturer,vehicle_chasis_number,vehicle_number,vehicle_model_number 
FROM vehicle WHERE cust_id IN (SELECT cust_id FROM customer2 WHERE login='1')""")
data = c.fetchone()

if data:
    print("Fetched data:", data)

    # Get column names
    c.execute("DESCRIBE vehicle")
    columns = ['vehicle_id','vehicle_registration_number','vehicle_value','vehicle_type','vehicle_size','vehicle_number_of_seat','vehicle_manufacturer','vehicle_chasis_number','vehicle_number','vehicle_model_number']
    

    # Create Treeview widget
    tree = ttk.Treeview(frame, columns=("Attribute", "Value"), show="headings")

    # Add column headings
    tree.heading("Attribute", text="Attribute")
    tree.heading("Value", text="Value")

    # Add data to the Treeview
    for col, val in zip(columns, data):
        # Handle None values
        if val is not None:
            tree.insert("", "end", values=(col, val))
        else:
            tree.insert("", "end", values=(col, "None"))

    # Pack the Treeview widget
    tree.pack(side="left", fill="y")

else:
    tk.Label(frame, text="No data found for customer with ID", bg="#2C3E50", fg="white").pack()

frame.pack()

# Back button
back_button = tk.Button(root, text="Back", bg="lightgrey", fg="red", command=go_back)
back_button.place(x=10, y=10)

# Style configuration
style = ttk.Style()
style.configure("Custom.Treeview", background="#2C3E50", foreground="white", font=('Verdana', 12))

root.mainloop()
