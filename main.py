from tkinter import *
from tkinter import messagebox
from password_generator import random_passoword
def format_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Warning!", message="Dont leave blank fields!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail:{email} \nPassword:{password} \nIs it okay to save?")
        if is_ok:
            with open("data.txt" , "a") as file:
                file.write(f"Website: {website}, Email/Username: {email}, Password: {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def insert_random_password():
    password_entry.delete(0, END)
    random_password = random_passoword()
    if len(random_password) < 8 or len(random_password) > 32:
        random_password = random_passoword()
    password_entry.insert(END, string=random_password)

FONT_NAME = "Arial"
window = Tk()
window.title("Password Manager")
window.config(padx=100 , pady=100)
canvas = Canvas(width=512, height=512, highlightthickness=0)
img = PhotoImage(file="image.png")
canvas.create_image(256 , 256 , image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website",font=(FONT_NAME , 15 , "bold"))
website_label.grid(column=0, row=1)

email = Label(text="Email/Username",font=(FONT_NAME , 15 , "bold"))
email.grid(column=0, row=2)

password_label = Label(text="Password",font=(FONT_NAME , 15 , "bold"))
password_label.grid(column=0, row=3)

website_entry = Entry()
website_entry.config(width=80)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry()
email_entry.config(width=80)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry()
password_entry.config(width=50)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=insert_random_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=85, command=format_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()