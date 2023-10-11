from tkinter import *
def close ():
    #window.destroy()
    window.quit()
def start ():
    import time
    time.sleep(3)
    window.quit
    import cypclock
window=Tk()
lbl=Label(window, text="Cypclock brough to you by cypress", font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.title('Welcome to Cypclock')
window.geometry("500x500+10+10")
my_button = Button(window,
                   text="start program",
                   command=start,
                   font=("calibri", 24),
                   fg="blue")
my_button.pack(pady=100)
window.mainloop()
