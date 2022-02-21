from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# Save the form information to a file
def save():
    website_text = web_input.get()
    email_text = email_input.get()
    pw_text = pw_input.get()
    new_data = {
        website_text: {
        "email": email_text,
        "password": pw_text
    }}
    
    if len(website_text) == 0 or len(pw_text) == 0:
        messagebox.showinfo(title="Oops", message="Please fill in all fields")
    else:
        try:
            with open("data.json", "r") as f:
                # reading old data
                data = json.load(f)
                # Saving updated data
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
             # Updating old data with new
                data.update(new_data)
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
        finally:      
            web_input.delete(0, END)
            pw_input.delete(0, END)
        
            
# Generate password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letters_list = [random.choice(letters) for letter in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for number in range(random.randint(2, 4))]

    password_list = letters_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)

    pw_input.insert(0, password)
    pyperclip.copy(password)
    
# Search for item in json
def search():
    # Read json file and get the data
    try:
        with open("data.json", "r") as f:
            search_text = web_input.get().title()
            data = json.load(f)
            email_addy = data[search_text]["email"]
            password = data[search_text]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Please save some information first.")
    except KeyError:
        messagebox.showinfo(title="Error", message="This information does not exist, please add the website and password first.")
    else:
        messagebox.showinfo(title=f"{search_text}", message=f"Email: {email_addy}\nPassword: {password}")

# Configuring the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# Configuring the canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Configuring the labels
website_label = Label(font="bold",text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(font="bold",text="Email/Username:")
email_label.grid(column=0, row=2)

pw_label = Label(font="bold",text="Password:")
pw_label.grid(column=0, row=3)

# configuring the input boxes
web_input=Entry(width=33)
web_input.grid(column=1, row=1)
web_input.focus()  
 
email_input=Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "shelleygal78@gmail.com")

pw_input=Entry(width=33)
pw_input.grid(column=1, row=3)

# configuring the buttons
pw_btn=Button(text="Generate Password", command=generate_password)
pw_btn.grid(column=2, row=3)

add_btn=Button(text="Add", width=44, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", width=15, bg="blue", fg='white', command=search)
search_btn.grid(column=2, row=1)


window.mainloop()
