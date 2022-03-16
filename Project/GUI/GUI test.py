from tkinter import *

root = Tk()

root.title('exercise 5')
root.minsize(600,400)

Label(root, text='Red', bg='red', fg='white').pack(side=LEFT, fill=Y)
Label(root, text='Lime', bg='lime', fg='black').pack(side=BOTTOM, fill=X)
Label(root, text='Blue', bg='blue', fg='white').pack(side=RIGHT, fill=BOTH, expand=YES)

root.mainloop()

