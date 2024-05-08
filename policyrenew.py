import tkinter as tk
import os
from tempCodeRunnerFile import db
def renew_policy():
    success_label = tk.Label(root, text="Policy Renewed", bg="light green")
    success_label.place(x=158, y=130)

def open_code_1():
    root.destroy()
    os.system("python policies.py")

cursor=db.cursor()
cursor.execute("SELECT mem_type FROM customer2 where login='1' LIMIT 1")
data = cursor.fetchone()
policy=data[0]

root = tk.Tk()
root.title("Policy Renewal")
root.geometry("400x200")
root.configure(bg="#2C3E50")

# Back button
back_button = tk.Button(root, text="Back", bg="lightgrey", fg="red", command=open_code_1)
back_button.place(x=10, y=10)

# Create a label with the text "Your current policy is _______ do you wish to renew?"
policy_text = "Your current policy is"
policy_label = tk.Label(root, text=policy_text, font=("Verdana", 12), bg="#2C3E50", fg="white")
policy_label.pack(pady=10)

# Separate label for policy type
policy_type_label = tk.Label(root, text=policy, font=("Verdana", 12, "bold"), bg="#2C3E50", fg="white")
policy_type_label.pack()

# Label for "do you wish to renew?"
renew_label = tk.Label(root, text="do you wish to renew?", font=("Verdana", 12), bg="#2C3E50", fg="white")
renew_label.pack()

# Button for renewing policy
renew_button = tk.Button(root, text="Renew", command=renew_policy, bg="#1ABC9C", fg="black")
renew_button.pack(pady=10)

root.mainloop()
