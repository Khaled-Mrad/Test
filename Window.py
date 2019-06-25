from tkinter import *
window=Tk()
window.title("Good Morning")
window.geometry("500x500")
window.minsize(200,200)
window.config(background="#2F97ED")
label_title=Label(window,text="my name is khaled mrad",font=("Oxygen",40),
                  bg="red",fg="blue")
label_title.pack(expand=YES)
window.mainloop()
