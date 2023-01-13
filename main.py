import customtkinter
import pyperclip
from password_generator import RandomPassword

rand_password = RandomPassword()
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.title('Random Password Generator By Tahmid Newaz')
app.geometry("420x240")


def button_function():
    copy_button.configure(text='Copy to Clipboard', state='normal')
    password_display.configure(text=rand_password.generate())

def copy_to_clipboard():
    pyperclip.copy(password_display.text)


button = customtkinter.CTkButton(master=app, text="Generate Password", command=button_function)
button.pack(pady=(50, 0))
password_display = customtkinter.CTkLabel(master=app, text="Click The Button to generate a random Password")
password_display.pack(pady = (10, 0))
copy_button = customtkinter.CTkButton(master=app, text='',hover_color= 'green',
                                      fg_color= 'transparent', command=copy_to_clipboard, state='disabled')
copy_button.pack(pady = (10, 0))

app.mainloop()