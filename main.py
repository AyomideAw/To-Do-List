from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('800x500+300+150')  # Wider and taller for better layout
        self.root.resizable(False, False)

        # App Icon
        img = Image.open('Image/task.png')
        Image_icon = ImageTk.PhotoImage(img)
        self.root.iconphoto(False, Image_icon)

        # App Title
        self.label = Label(self.root, text='To-Do List Application',
                           font='Arial 24 bold', bg='light blue', fg='black', padx=20, pady=10)
        self.label.pack(fill=BOTH)

        # Add Task Section
        self.label2 = Label(self.root, text='Add Task',
                            font='Arial 16 bold', bg='light blue', fg='black')
        self.label2.place(x=40, y=80)

        self.text = Text(self.root, bd=3, height=2, width=40, font='Arial 12')
        self.text.place(x=40, y=120)

        self.button = Button(self.root, text='Add', font='Arial 14 bold',
                             width=10, bg='light blue', fg='black', command=self.add)
        self.button.place(x=60, y=180)

        self.button2 = Button(self.root, text='Delete', font='Arial 14 bold',
                              width=10, bg='light blue', fg='black', command=self.delete)
        self.button2.place(x=200, y=180)

        # Task List Section
        self.label3 = Label(self.root, text='Tasks',
                            font='Arial 16 bold', bg='light blue', fg='black')
        self.label3.place(x=450, y=80)

        self.main_text = Listbox(self.root, height=13, width=40,
                                 bd=3, font='Arial 12')
        self.main_text.place(x=400, y=120)

        # Load tasks if file exists
        if not os.path.exists('tasklist.txt'):
            with open('tasklist.txt', 'w') as f:
                pass

        with open('tasklist.txt', 'r') as file:
            read = file.readlines()
            for line in read:
                self.main_text.insert(END, line.strip())

    def add(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content + '\n')
            with open('tasklist.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)

    def delete(self):
        try:
            selected = self.main_text.curselection()
            task = self.main_text.get(selected)
            self.main_text.delete(selected)

            with open('tasklist.txt', 'r') as file:
                lines = file.readlines()
            with open('tasklist.txt', 'w') as file:
                for line in lines:
                    if line.strip() != task.strip():
                        file.write(line)
        except IndexError:
            pass  # No item selected

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
