from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List') #title of the page
        self.root.geometry('650x410+300+150') #setting up the size and the positioning of the window
        self.root.resizable(False,False)

        #icon
        Image_icon = PhotoImage(file='Image/task.png')
        self.root.iconphoto(False, Image_icon)

        self.label = Label(self.root, text='To-Do List Application', 
             font='ariel, 25 bold', width=10, borderwidth=5, background='light blue', foreground='black') #creating the header label 
        self.label.pack(side='top', fill = BOTH)

        self.label2 = Label(self.root, text='Add Task', 
             font='ariel, 18 bold', width=10, borderwidth=5, background='light blue', foreground='black') #creating the add task label and placing it 
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks', 
             font='ariel, 18 bold', width=10, borderwidth=5, background='light blue', foreground='black') #creating the tasks label and placing it 
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, borderwidth=5, width= 23, font='ariel, 20 italic bold') #creating a list box where the users tasks can be displayed
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold') #creating a text box where the users put in their tasks to be displayed PS: bd is borderwidth
        self.text.place(x=20, y=120)

        #--------------- ADD TASK ----------------#

        def add():
            content = self.text.get(1.0, END) #getting the content in the text box from the begining(index one) to the end 
            self.main_text.insert(END, content) #inserting the content from the text box to the list box
            with open('data.txt', 'a') as file: #writing the content to the text file
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END) #deleting everything in the text box after its been added

        def delete():
            delete_ = self.main_text.curselection() #when a particular task its selected it identifies which one is to be deleted
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f: #reading each line in the txt file
                #deleting the item from the text file
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look) #changing the look item to a string
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_) #deletes the item selected on the list box

        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split() #each task will be on a separate line in the list box
                self.main_text.insert(END, ready)
            file.close()

        self.button = Button(self.root, text='Add', font='sarif, 20 bold italic', 
                width=10, bd=5, background='light blue', foreground='black', command=add)
        self.button.place(x=30, y=180) #placing it on the screen

        self.button2 = Button(self.root, text='Delete', font='sarif, 20 bold italic', 
                width=10, bd=5, background='light blue', foreground='black', command=delete)
        self.button2.place(x=30, y=280) #placing it on the window

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()