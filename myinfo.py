import tkinter as tk
from tkinter import ttk
import mysql.connector
from tempCodeRunnerFile import db
import os

# Establishing connection to the database

cursor = db.cursor()





def go_back():
    root.destroy()
    os.system("python userinterface.py")
    # Add code to navigate back to the previous page

def update_data():
    root.destroy()
    os.system("python updatedata.py")
    

root = tk.Tk()
root.title("Customer Data")

frame = tk.Frame(root, padx=40, pady=40, bg='#2C3E50')

# Fetching data of the first customer from the database
cursor.execute("SELECT * FROM customer2 where login='1' LIMIT 1")
data = cursor.fetchone()

if data:
    # Transpose the data to show vertically
    data_vertical = [(col,) for col in data]

    # Get column names
    cursor.execute("DESCRIBE customer")
    columns = [col[0] for col in cursor.fetchall()]

    # Transpose the columns to show vertically
    columns_vertical = [(col,) for col in columns]

    # Create Treeview widget
    tree = ttk.Treeview(frame, columns=("Attribute", "Value"), show="headings")

    # Add column headings
    tree.heading("Attribute", text="Attribute")
    tree.heading("Value", text="Value")

    # Add data to the Treeview
    for col, val in zip(columns_vertical, data_vertical):
        tree.insert("", "end", values=(col[0], val[0]))

    # Pack the Treeview widget
    tree.pack(side="left", fill="y")

else:
    tk.Label(frame, text="No data found for customer with ID", bg="#2C3E50", fg="white").pack()

frame.pack()

# Back button
back_button = tk.Button(root, text="Back", bg="lightgrey", fg="red", command=go_back)
back_button.place(x=10, y=10)

# Submit button
updat_button = tk.Button(root, text="Update", bg="#1ABC9C", command=update_data)
updat_button.pack(side="bottom", pady=10)

# Style configuration
style = ttk.Style()
style.configure("Custom.Treeview", background="#2C3E50", foreground="white", font=('Verdana', 12))

root.mainloop()
