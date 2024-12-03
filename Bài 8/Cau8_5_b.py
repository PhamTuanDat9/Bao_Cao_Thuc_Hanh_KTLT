print("Pham Tuan Dat")
print("235752021610105")
import tkinter as tk
root = tk.Tk()
root.title("Indicator Example")
v = tk.IntVar()
v.set(1)  
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C#", 5)
]
def ShowChoice():
    print(f"Selected: {v.get()}")  
tk.Label(
    root,
    text="Choose your favourite programming language:",
    justify=tk.LEFT,
    padx=20
).pack()
for language, val in languages:
    tk.Radiobutton(
        root,
        text=language, 
        padx=20,
        variable=v, 
        command=ShowChoice, 
        value=val, 
        indicatoron=False,  
        width=20  
    ).pack(anchor=tk.W)
root.mainloop()
