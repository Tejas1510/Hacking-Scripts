from tkinter import * 
from database import BookData

main_window=Tk()
main_window.geometry('520x470')
main_window.title('Book Management System')

mydata=BookData()

def view():
    view_window=Toplevel()
    view_window.title('View all Books')
    view_window.geometry('520x470')
    heading=Label(view_window,text='Viewing All Books',justify='center',font='helvetica 24 bold underline',pady=20)
    view_table=Listbox(view_window,height=15,width=75)
    view_table.delete(0,END)
    for data in mydata.view_data():
        view_table.insert(END,data)
    close_btn=Button(view_window,text='Close',relief='groove',bd=3,width=10,height=1,font='helvetica 9',activeforeground='red',command=view_window.destroy)
    heading.place(x=125,y=0)
    close_btn.place(x=420,y=430)
    view_table.place(x=27,y=125)

def add():
    def add_cmd(): 
        mydata.insert_in_database(title_val.get(),author_val.get(),year_val.get(),isbn_val.get())
        view_table.delete(0,END)
        view_table.insert(END,(title_val.get(),author_val.get(),year_val.get(),isbn_val.get())) 
    add_window=Toplevel()
    add_window.geometry('520x470')
    add_window.title('Add new Book')
    view_table=Listbox(add_window,height=4,width=75)
    heading=Label(add_window,text='Add Book',justify='center',font='helvetica 24 bold underline',pady=20)
    title_val=StringVar()
    label1=Label(add_window,text='Title : ')
    label2=Label(add_window,text='Author : ')
    label3=Label(add_window,text='Year : ')
    label4=Label(add_window,text='ISBN : ')
    entry1=Entry(add_window,textvariable=title_val)
    author_val=StringVar()
    entry2=Entry(add_window,textvariable=author_val)
    year_val=StringVar()
    entry3=Entry(add_window,textvariable=year_val)
    isbn_val=StringVar()
    entry4=Entry(add_window,textvariable=isbn_val)
    close_btn=Button(add_window,text='Close',relief='groove',bd=3,width=10,height=1,font='helvetica 9',activeforeground='red',command=add_window.destroy)
    add_btn=Button(add_window,text='Add',relief='groove',bd=3,width=10,height=1,font='helvetica 9',command=add_cmd)
    heading.place(x=190,y=0)
    close_btn.place(x=420,y=430)
    label1.place(x=60,y=125)
    entry1.place(x=100,y=125)

    label2.place(x=275,y=125)
    entry2.place(x=325,y=125)

    label3.place(x=60,y=210)
    entry3.place(x=100,y=210)

    label4.place(x=285,y=210)
    entry4.place(x=325,y=210)
    view_table.place(x=27,y=280)
    add_btn.place(x=215,y=380)

def update():
    def get_selected_row1(event):
        try:
            global select
            index=view_table.curselection()[0]
            select=view_table.get(index)
            entry1.delete(0,END)
            entry1.insert(END,select[1])
            entry2.delete(0,END)
            entry2.insert(END,select[2])
            entry3.delete(0,END)
            entry3.insert(END,select[3])
            entry4.delete(0,END)
            entry4.insert(END,select[4])
            view_table.bind('<<ListboxSelect>>',get_selected_row1)
        except IndexError:
            pass

    def update_cmd():
        mydata.update_record(select[0],title_val.get(),author_val.get(),year_val.get(),isbn_val.get())

    update_window=Toplevel()
    update_window.geometry('520x470')
    update_window.title('Update Book')
    heading=Label(update_window,text='Update Book',justify='center',font='helvetica 24 bold underline',pady=20)
    close_btn=Button(update_window,text='Close',relief='groove',bd=3,width=10,height=1,font='helvetica 9',activeforeground='red',command=update_window.destroy)
    view_table=Listbox(update_window,height=4,width=75)
    view_table.delete(0,END)
    for data in mydata.view_data():
        view_table.insert(END,data)   
    label1=Label(update_window,text='Title : ')
    label2=Label(update_window,text='Author : ')
    label3=Label(update_window,text='Year : ')
    label4=Label(update_window,text='ISBN : ')
    title_val=StringVar()
    entry1=Entry(update_window,textvariable=title_val)
    author_val=StringVar()
    entry2=Entry(update_window,textvariable=author_val)
    year_val=StringVar()
    entry3=Entry(update_window,textvariable=year_val)
    isbn_val=StringVar()
    entry4=Entry(update_window,textvariable=isbn_val)
    update_btn=Button(update_window,text='Update',relief='groove',bd=3,width=10,height=1,font='helvetica 9',command=update_cmd)

    label1.place(x=60,y=125)
    entry1.place(x=100,y=125)

    label2.place(x=275,y=125)
    entry2.place(x=325,y=125)

    label3.place(x=60,y=210)
    entry3.place(x=100,y=210)

    label4.place(x=285,y=210)
    entry4.place(x=325,y=210)
    view_table.place(x=27,y=280)
    update_btn.place(x=215,y=380)
    heading.place(x=175,y=0)
    close_btn.place(x=420,y=430)

def delete():
    def get_selected_row2(event):
        try:
            global selection
            index=view_table.curselection()[0]
            selection=view_table.get(index)
            entry1.delete(0,END)
            entry1.insert(END,selection[1])
            entry2.delete(0,END)
            entry2.insert(END,selection[2])
            entry3.delete(0,END)
            entry3.insert(END,selection[3])
            entry4.delete(0,END)
            entry4.insert(END,selection[4])
            view_table.bind('<<ListboxSelect>>',get_selected_row2)
        except IndexError:
            pass

    def delete_cmd():
        mydata.delete_record(selection[0])

    delete_window=Toplevel()
    delete_window.geometry('520x470')
    delete_window.title('Delete Book')
    heading=Label(delete_window,text='Delete Book',justify='center',font='helvetica 24 bold underline',pady=20)
    close_btn=Button(delete_window,text='Close',relief='groove',bd=3,width=10,height=1,font='helvetica 9',activeforeground='red',command=delete_window.destroy)
    view_table=Listbox(delete_window,height=4,width=75)
    view_table.delete(0,END)
    for data in mydata.view_data():
        view_table.insert(END,data)
    label1=Label(delete_window,text='Title : ')
    label2=Label(delete_window,text='Author : ')
    label3=Label(delete_window,text='Year : ')
    label4=Label(delete_window,text='ISBN : ')
    title_val=StringVar()
    entry1=Entry(delete_window,textvariable=title_val)
    author_val=StringVar()
    entry2=Entry(delete_window,textvariable=author_val)
    year_val=StringVar()
    entry3=Entry(delete_window,textvariable=year_val)
    isbn_val=StringVar()
    entry4=Entry(delete_window,textvariable=isbn_val)
    update_btn=Button(delete_window,text='Delete',relief='groove',bd=3,width=10,height=1,font='helvetica 9',command=delete_cmd)

    label1.place(x=60,y=125)
    entry1.place(x=100,y=125)

    label2.place(x=275,y=125)
    entry2.place(x=325,y=125)

    label3.place(x=60,y=210)
    entry3.place(x=100,y=210)

    label4.place(x=285,y=210)
    entry4.place(x=325,y=210)
    view_table.place(x=27,y=280)
    update_btn.place(x=215,y=380)
    heading.place(x=175,y=0)
    close_btn.place(x=420,y=430)


title=Label(main_window,text='Book Management System',justify='center',font='helvetica 21 bold underline',pady=20,width=30)
view_button=Button(main_window,text='View All Books',relief='groove',bd=4,width=17,height=3,font='helvetica 9 bold',anchor=CENTER,command=view)
add_button=Button(main_window,text='Add Book',relief='groove',bd=4,width=17,height=3,font='helvetica 9 bold',anchor=CENTER,command=add)
update_button=Button(main_window,text='Update Book',relief='groove',bd=4,width=17,height=3,font='helvetica 9 bold',anchor=CENTER,command=update)
delete_button=Button(main_window,text='Delete Book',relief='groove',bd=4,width=17,height=3,font='helvetica 9 bold',anchor=CENTER,command=delete)
close_button=Button(main_window,text='Close',relief='groove',bd=3,width=10,height=1,font='helvetica 9',activeforeground='red',command=main_window.destroy)

title.place(x=0,y=0)
view_button.place(x=100,y=150)
add_button.place(x=300,y=150)
update_button.place(x=100,y=300)
delete_button.place(x=300,y=300)
close_button.place(x=420,y=425)

main_window.mainloop()