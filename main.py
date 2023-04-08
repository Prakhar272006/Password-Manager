import json
from tkinter import *
from tkinter import  messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letter = [random.choice(letters) for pas in range(nr_letters)]
    password_number = [random.choice(numbers) for pas in range(nr_numbers)]
    password_symbol = [random.choice(symbols) for pas in range(nr_symbols)]
    pass_list = password_letter + password_symbol + password_number
    random.shuffle(pass_list)
    final_pass = "".join(pass_list)
    password.insert(0, pass_list)
    pyperclip.copy(final_pass)
# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_name.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found.")
    else:
         if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email} \n Password : {password} ")
         else:
             messagebox.showinfo(title="Error",message=f"No details for {website} were found")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_detail():
    site = website_name.get()
    username = email.get()
    password_saved = password.get()
    new_data = {
        site: {
            "email" : username,
            "password": password_saved,
        }
    }
    if len(site)==0 and len(username)==0 and len(password_saved)==0:
        messagebox.showinfo(title="Oops", message="Please make sure that you dont have any fields empty")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
           data.update(new_data)

           with open("data.json","w") as data_file:
               json.dump(data,data_file,indent=4)
        finally:
               website_name.delete(0,END)
               password.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50,pady=50)
logo =PhotoImage(file="logo.png")
canvass = Canvas(width=200,height=200)
canvass.create_image(100,100,image=logo)
canvass.grid(row=0,column=1)

website_lable = Label(text="Website :")
website_lable.grid(row=1,column=0)

username_lable = Label(text="Email/Username :")
username_lable.grid(row=2,column=0)

password_lable = Label(text="Password :")
password_lable.grid(row=3,column=0)

generate_button = Button(text="Generate Password", command=generate_pass)
generate_button.grid(row=3,column=2)


add_button = Button(text="Add",width=30,command = save_detail)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",width=10,command=find_password)
search_button.grid(column=2,row=1)

website_name =Entry(width=34).lower()
website_name.grid(row=1,column=1)
website_name.focus()

email = Entry(width=50)
email.grid(row=2,column=1,columnspan=2)
email.insert(0,"prakhargurjar27@gmail.com")

password = Entry(width=34)
password.grid(row=3,column=1)
























screen.mainloop()
