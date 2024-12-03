print("Pham Tuan Dat")
print("235752021610105")
from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks App")
window.geometry("350x200")
lbl = Label(window, text="Hello", font=("Arial Bold", 14))
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", command=clicked, bg="blue", fg="white")
btn.grid(column=1, row=0)
window.mainloop()
