from tkinter import *

root=Tk()
root.title("User Data Management")
root.geometry("400x400")

my_menu= Menu(root)
root.config(menu=my_menu)



#click command


def add():
    add_data=Tk()
#create a menu item

file_menu =Menu(my_menu)
my_menu.add_cascade(label="Utilities", menu=file_menu)
my_menu.add_cascade(label="Master")
my_menu.add_cascade(label="Transaction")
my_menu.add_command(label="Exit", command=root.quit)



#CREATE A SUB MENUS
file_menu.add_command(label="Calculator")
file_menu.add_command(label="Add User")
file_menu.add_command(label="Change Password")






root.mainloop()


 