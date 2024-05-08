import tkinter as tk
from tkinter import ttk
from tempCodeRunnerFile import db
import os

# Create the main window
root = tk.Tk()
root.title("Claims Tracker")
root.geometry("400x350")  # Set the initial size of the window

# Change background color
root.configure(bg="#2C3E50")

# Function to handle back button click
def go_back():
    root.destroy()
    os.system("python userinterface.py")  # Runs userinterface.py

# Function to handle button click
def submit():
    # Retrieve data from entries
    amount = amount_entry.get()
    accident_type = accident_var.get()
    
    # dect to the database
    
    cursor = db.cursor()
    
    # Execute a query to check the mem_type column where login is 1
    cursor.execute("SELECT mem_type FROM customer2 WHERE login=1;")
    mem_type = cursor.fetchone()[0]
    
    # Check the coverage based on mem_type
    if mem_type == "gold":
        claim_approved_label.config(text="Claim Approved")
    elif mem_type == "silver":
        if accident_type in ["Theft", "Natural Calamity"]:
            claim_approved_label.config(text="Please Upgrade for this Coverage")
        else:
            claim_approved_label.config(text="Claim Approved")
    elif mem_type == "bronze":
        if accident_type in ["Theft", "Natural Calamity","Wear and Tear"]:
            claim_approved_label.config(text="Please Upgrade for this Coverage")
        else:
            claim_approved_label.config(text="Claim Approved")
    
    # Clear the amount entry box
    amount_entry.delete(0, tk.END)
    
    # Commit changes and close dection
    db.commit()


# Create and place the widgets
claim_label = tk.Label(root, text="Claims", font=("Verdana", 20), bg="#2C3E50", fg="orange")
claim_label.pack(fill=tk.X, pady=10)

back_button = tk.Button(root, text="Back", fg="red", bg="light grey", command=go_back)
back_button.place(x=10, y=10)

amount_frame = tk.Frame(root, bg="#2C3E50")
amount_frame.pack(pady=10)

amount_text = tk.Label(amount_frame, text="Amount:", font=("Verdana", 12), bg="#2C3E50", fg="white")
amount_text.grid(row=0, column=0)

amount_entry = tk.Entry(amount_frame, font=("Verdana", 12), width=10)
amount_entry.grid(row=0, column=1)

accident_frame = tk.Frame(root, bg="#2C3E50")
accident_frame.pack(pady=10)

accident_text = tk.Label(accident_frame, text="Accident Type:", font=("Verdana", 12), bg="#2C3E50", fg="white")
accident_text.grid(row=0, column=0)

accident_options = ["Theft", "Natural Calamity", "Accidents", "Wear and Tear", "Vandalism"]
accident_var = tk.StringVar(root)
accident_var.set(accident_options[0])
accident_menu = ttk.Combobox(accident_frame, textvariable=accident_var, values=accident_options, font=("Verdana", 12), width=20)
accident_menu.grid(row=0, column=1)

submit_button = tk.Button(root, text="Submit", command=submit, bg="light grey")
submit_button.pack(pady=10)

claim_approved_label = tk.Label(root, text="", font=("Verdana", 12), bg="#2C3E50", fg="green")
claim_approved_label.pack(pady=10)

# Start the application
root.mainloop()
