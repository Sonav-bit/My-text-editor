from tkinter import *
from tkinter.filedialog import askopenfiles,asksaveasfilename
root=Tk()
root.title('My text editor')
root.geometry('600x500')
root.rowconfigure(0,minsize=800,weight=1)
root.columnconfigure(0,minsize=800,weight=1)

def open_file():
    filepath=askopenfiles(filetypes=[('Textfiles','.*txt'),('Allfiles','*.*')])
    if not filepath:
        return
    t1.delete(1.0,END)
    with open(filepath,'r') as i:
        text=i.read()
        t1.insert(END,text)
        i.close()
    root.title( f'Codingal file -{filepath}')

def save_file():
    filepath=asksaveasfilename(filetypes=[('Textfiles','.*txt'),('Allfiles','*.*')])
    if not filepath:
        return
    with open(filepath,'w') as i:
        text=t1.pygame.event.get(1.0,END)
        i.write(text)
        
    root.title( f'Codingal file -{filepath}')
t1=Text(root)
f1=Frame(root,relief=RAISED,bd=2)
b1=Button(f1,text='Open',command=open_file)
b2=Button(f1,text='Save',command=save_file)

b1.grid(row=0,column=0,sticky='ew',padx=5,pady=5)
b2.grid(row=1,column=0,sticky='ew',padx=5,pady=5)
f1.grid(row=0,column=0,sticky='ns')
t1.grid(row=0,column=1,sticky='nsew')




root.mainloop()