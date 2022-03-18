import tkinter as tk
from tkinter import messagebox
import pyperclip
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    entry_password.delete(0, "end")
    entry_password.insert(0, password)
    print(f"Your password is: {password}")
    pyperclip.copy(password)
    # insert password into clibboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    pwebsite = entry_website.get()
    pusername = entry_username.get()
    ppassword = entry_password.get()
    new_data = {
        pwebsite: {
            "email": pusername,
            "password": ppassword,
        }
    }

    # check if  boxes full
    if len(pwebsite) == 0:
        messagebox.showinfo(title="Warning", message="Warning! No Website input!")
    elif len(ppassword) == 0:
        messagebox.showinfo(title="Warning", message="Warning! No password input!")
    else: #hier wurde geändert, dass man jetzt nur noch in json Format schreibt und nichtmehr .txt
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)  # read old data

        except FileNotFoundError:  # if file not found create new one
            with open("./data.json", "w") as datafile:
                json.dump(new_data, datafile, indent=4)

        else:
            data.update(new_data)  # update old data
            with open("data.json", "w") as datafile:
                json.dump(data, datafile, indent=4)  # write
        #mach so oder so:
        finally:
            entry_website.delete(0, "end")  # delete entry after adding data to file
            entry_password.delete(0, "end")
#-----------------------------Search for Password-----------------------#
def find_password():
    website= entry_website.get()
    try:
        with open("data.json", "r") as datafile:
            data = json.load(datafile)  # read old data

    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="No Data File Found")

    else:
        if website in data:
            messagebox.showinfo(title="Match", message=f"Website: {website}\nEmail: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Warning", message=f"Warning! No datais for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password-Manager")
window.config(padx=50, pady=50, bg="white")

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)  # highlightthickness=0 entfernt den Rahmen
logo_img = tk.PhotoImage(file="logo.png")  # wird benutzt um Bild bei tk besser zu verwenden
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# label website
lbl_website = tk.Label(text="Website:", bg="white")
lbl_website.grid(column=0, row=1)

# label EMAIL/Username
lbl_email_user_name = tk.Label(text="Email/Username:", bg="white")
lbl_email_user_name.grid(column=0, row=2)

# label Password
lbl_password = tk.Label(text="Password:", bg="white")
lbl_password.grid(column=0, row=3)

# Entry Website
entry_website = tk.Entry(width=34)
entry_website.focus()  # hier kann man den cuser schonmal setzen
entry_website.grid(column=1, row=1, columnspan=1, sticky="W")

# Entry Email/Username
entry_username = tk.Entry(width=53)
entry_username.insert(0, "michi.stober@gmail.com")  # mit insert kann man schonmal was rein schreiben
entry_username.grid(column=1, row=2, columnspan=2, sticky="W")

# Entry Password
entry_password = tk.Entry(width=34)
entry_password.grid(column=1, row=3, sticky="W")

# Button Generate Password
btn_generate_pswd = tk.Button(text="Generate Password", command=generate_password)  # command=
btn_generate_pswd.grid(column=2, row=3)

# Button Add
btn_add = tk.Button(text="Add", width=45, command=save)  # command=
btn_add.grid(column=1, row=4, columnspan=2, sticky="W")

# #button Search
btn_find_pswd = tk.Button(text="Search",width=14 ,command=find_password)  # command=
btn_find_pswd.grid(column=2, row=1, columnspan=1)


window.mainloop()
#TODO: Find website and delete entry