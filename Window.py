from tkinter import *
window=Tk()
window.title("Good Morning")
window.geometry("500x500")
window.minsize(200,200)
window.config(background="yellow")
label_title=Label(window,text="Python is WWOOWW",font=("Oxygen",40),
                  bg="red",fg="blue")
label_title.pack(expand=YES)
window.mainloop()
