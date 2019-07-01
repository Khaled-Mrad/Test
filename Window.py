from tkinter import *
import webbrowser

def khaled():
    webbrowser.open_new("http://youtube.com")

window=Tk()
window.title("my new app")
window.geometry("500x500")
window.minsize(200,200)
window.config(background="#00B8FF")

frame=Frame(window,bg="#59E959",bd=1,relief=SUNKEN)


label_title=Label(frame,text="Python is WWOOWW",font=("Oxygen",40),
                  bg="white",fg="blue")
label_title.pack()
#new text

label_text=Label(frame,text="my naem  is khaled maf",font=("Oxygen",25),
                  bg="white",fg="blue")
label_text.pack()

#new button
khaled=Button(frame,text="youtube",font=("Oxygen",25),
                  bg="white",fg="blue",command=khaled)
khaled.pack(pady=25,fill=X)
frame.pack(expand=YES)

window.mainloop()
