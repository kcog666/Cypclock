from tkinter import *
from time import strftime
import webbrowser

root = Tk()
root.geometry("420x420")
root.resizable(0,0)
root.title('Cypclock 0.1')

new = 1
url = "https://www.youtube.com/watch?v=Q44DA9-TH2o&list=PLLGIaswzK8nerfBww5vX312Bt2B5A24om"


def openweb():
    webbrowser.open(url,new=new)
def expand ():
    pass


# button code
my_button = Button(root,
                   text="Korn AMVs",
                   command=openweb,
                   font=("calibri", 24),
                   fg="blue")
my_button.pack(pady=100)
# clock code
Label(root,text = 'test by Cyp', font = 'arial 20 bold').pack(side=BOTTOM)

def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)

mark = Label(root,
    font = ('calibri', 40, 'bold'),
    pady=150,
    foreground = 'black')

mark.pack(anchor = 'center')
time()

mainloop()