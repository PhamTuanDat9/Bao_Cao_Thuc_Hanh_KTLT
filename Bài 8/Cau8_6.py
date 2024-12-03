print("Pham Tuan Dat")
print("235752021610105")
from tkinter import *
from tkinter import messagebox
def new_file():
    print("New File selected")
    messagebox.showinfo("Action", "New File")
def open_file():
    print("Open File selected")
    messagebox.showinfo("Action", "Open File")
def exit_app():
    print("Exiting application")
    root.quit()
def insert_text():
    print("Insert Text selected")
    messagebox.showinfo("Action", "Text Inserted")
def insert_picture():
    print("Insert Picture selected")
    messagebox.showinfo("Action", "Picture Inserted")
def about():
    print("About selected")
    messagebox.showinfo("About", "This is a menu example using tkinter.")
root = Tk()
root.title("Menu Example")
root.geometry("300x200")
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
insert_menu = Menu(menu_bar, tearoff=0)
insert_menu.add_command(label="Text", command=insert_text)
insert_menu.add_command(label="Picture", command=insert_picture)
menu_bar.add_cascade(label="Insert", menu=insert_menu)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu_bar)
root.mainloop()
