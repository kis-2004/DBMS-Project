import tkinter as tk
import os
from tempCodeRunnerFile import db

root = tk.Tk()
root.title("Registration Form")
root.geometry("450x300")
root.configure(bg="#2C3E50")

# Function to go back
def open_code_1():
    root.destroy()
    os.system("python policies.py")

def open_code_2():
    cursor=db.cursor()
    cursor.execute('update customer2 set mem_type="gold" where login="1";')
    db.commit()
    success_label = tk.Label(root, text="Policy Selected", bg="gold")
    success_label.place(x=175, y=7)


def open_code_3():
    cursor=db.cursor()
    cursor.execute('update customer2 set mem_type="silver" where login="1";')
    db.commit()
    success_label = tk.Label(root, text="Policy Selected", bg="light grey")
    success_label.place(x=175, y=7)

    
def open_code_4():
    cursor=db.cursor()
    cursor.execute('update customer2 set mem_type="bronze" where login="1";')
    db.commit()
    success_label = tk.Label(root, text="Policy Selected", bg="brown")
    success_label.place(x=175, y=7)    

# Create a label with big text "Register"
register_label = tk.Label(root, text="Change Policy", font=("Verdana", 28), bg="#2C3E50", fg="#FFA500")
register_label.pack(pady=20)

# Back button
back_button = tk.Button(root, text="Back", command=open_code_1, bg="light grey", fg="red")
back_button.place(x=10, y=10)

# Frame to hold gold, silver, and bronze sections
frame = tk.Frame(root, bg="#2C3E50")
frame.pack()

# Gold section
gold_frame = tk.Frame(frame, bd=3, relief=tk.GROOVE, bg="#2C3E50")
gold_frame.pack(side=tk.LEFT, padx=10, fill=tk.Y)

gold_label = tk.Label(gold_frame, text="Gold Plan", font=("Verdana", 12), bg="#2C3E50", fg="white")
gold_label.pack()
gold_description = tk.Label(gold_frame, text="THEFT\nNATURAL CALAMITY\nACCIDENTS\nVANDALISM\nWEAR AND TEAR", font=("Verdana", 10), bg="#2C3E50", fg="white")
gold_description.pack()

gold_button = tk.Button(gold_frame, text="Select", font=("Verdana", 10), bg="#1ABC9C", fg="black",command=open_code_2)
gold_button.pack(side=tk.BOTTOM)

# Silver section
silver_frame = tk.Frame(frame, bd=3, relief=tk.GROOVE, bg="#2C3E50")
silver_frame.pack(side=tk.LEFT, padx=10, fill=tk.Y)

silver_label = tk.Label(silver_frame, text="Silver Plan", font=("Verdana", 12), bg="#2C3E50", fg="white")
silver_label.pack()
silver_description = tk.Label(silver_frame, text="ACCIDENTS\n VANDALISM\n WEAR AND TEAR", font=("Verdana", 10), bg="#2C3E50", fg="white")
silver_description.pack()

silver_button = tk.Button(silver_frame, text="Select", font=("Verdana", 10), bg="#1ABC9C", fg="black",command=open_code_3)
silver_button.pack(side=tk.BOTTOM)

# Bronze section
bronze_frame = tk.Frame(frame, bd=3, relief=tk.GROOVE, bg="#2C3E50")
bronze_frame.pack(side=tk.LEFT, padx=10, fill=tk.Y)

bronze_label = tk.Label(bronze_frame, text="Bronze Plan", font=("Verdana", 12), bg="#2C3E50", fg="white")
bronze_label.pack()

bronze_text = "ACCIDENTS\nVANDALISM"
bronze_description = tk.Label(bronze_frame, text=bronze_text, font=("Verdana", 10), bg="#2C3E50", fg="white")
bronze_description.pack(expand=True, fill="both")

bronze_button = tk.Button(bronze_frame, text="Select", font=("Verdana", 10), bg="#1ABC9C", fg="black",command=open_code_4)
bronze_button.pack(side=tk.BOTTOM)

root.mainloop()





