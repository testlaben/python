"""
A program to store book information.
Title, Author
Year, ISBN

"""

from tkinter import *
from backend import Database


database = Database("books.db")

def get_selected_row(event):
    try:
        global selected_tuple
        index = list.curselection()[0]
        selected_tuple = list.get(index)
        l1_entry.delete(0, END)
        l1_entry.insert(END, selected_tuple[1])
        l2_entry.delete(0, END)
        l2_entry.insert(END, selected_tuple[2])
        l3_entry.delete(0, END)
        l3_entry.insert(END, selected_tuple[3])
        l4_entry.delete(0, END)
        l4_entry.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list.delete(0, END)
    for row in Database.view():
        list.insert(END, row)


def search_command():
    list.delete(0,END)
    for row in Database.search(text_input.get(), author_input.get(), year_input.get(), isbn_input.get()):
        list.insert(END, row)


def add_command():
    Database.insert(text_input.get(), author_input.get(), year_input.get(), isbn_input.get())
    list.delete(0, END)
    list.insert(END, (text_input.get(), author_input.get(), year_input.get(), isbn_input.get()))


def delete_command():
    Database.delete(selected_tuple[0])


def update_command():
    Database.update(selected_tuple[0], text_input.get(), author_input.get(), year_input.get(), isbn_input.get())


def exit_command():
    exit()


window = Tk()

# Title & input
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
text_input = StringVar()
l1_entry = Entry(window, textvariable=text_input)
l1_entry.grid(row=0, column=1)

# Author & input
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
author_input = StringVar()
l2_entry = Entry(window, textvariable=author_input)
l2_entry.grid(row=0, column=3)

# Year & input
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
year_input = StringVar()
l3_entry = Entry(window, textvariable=year_input)
l3_entry.grid(row=1, column=1)

# ISBN & input
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)
isbn_input = StringVar()
l4_entry = Entry(window, textvariable=isbn_input)
l4_entry.grid(row=1, column=3)

# Listbox & scroll
list = Listbox(window, height=6, width=35)
list.grid(row=2, column=0, rowspan=6, columnspan=2)
scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)
list.bind('<<ListboxSelect>>', get_selected_row)

list.configure(yscrollcommand=scroll.set)
scroll.configure(command=list.yview)

# Buttons
b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b1 = Button(window, text="Search Entry", width=12, command=search_command)
b1.grid(row=3, column=3)

b1 = Button(window, text="Add Entry", width=12, command=add_command)
b1.grid(row=4, column=3)

b1 = Button(window, text="Update", width=12, command=update_command)
b1.grid(row=5, column=3)

b1 = Button(window, text="Delete", width=12, command=delete_command)
b1.grid(row=6, column=3)

b1 = Button(window, text="Exit", width=12, command=exit_command)
b1.grid(row=7, column=3)


window.mainloop()
