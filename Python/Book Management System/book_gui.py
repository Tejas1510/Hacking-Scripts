from tkinter import * 
main_window=Tk()
main_window.geometry('520x470')
main_window.title('Book Management System')

def view():
    view_window=Toplevel()
    view_window.title('View all Books')
    view_window.geometry('520x470')
    heading=Label(view_window,text='Viewing All Books',justify='center',font='helvetica 24 bold underline',pady=20)
    close_btn=Button(view_window,text='Close',relief='groove',bd=3,width=10,height=1,font='helvetica 9',activeforeground='red',command=view_window.destroy)
    heading.place(x=125,y=0)
    close_btn.place(x=420,y=430)


def add():
    add_window=Toplevel()
    add_window.geometry('520x470')
    add_window.title('Add new Book')
    heading=Label(add_window,text='Add Book',justify='center',font='helvetica 24 bold underline',pady=20)
    close_btn=Button(add_window,text='Close',relief='groove',bd=3,width=10,height=1,font='helvetica 9',activeforeground='red',command=add_window.destroy)
    heading.place(x=190,y=0)
    close_btn.place(x=420,y=430)

def update():
    update_window=Toplevel()
    update_window.geometry('520x470')
    update_window.title('Update Book')
    heading=Label(update_window,text='Update Book',justify='center',font='helvetica 24 bold underline',pady=20)
    close_btn=Button(update_window,text='Close',relief='groove',bd=3,width=10,height=1,font='helvetica 9',activeforeground='red',command=update_window.destroy)
    heading.place(x=175,y=0)
    close_btn.place(x=420,y=430)

def delete():
    delete_window=Toplevel()
    delete_window.geometry('520x470')
    delete_window.title('Delete Book')
    heading=Label(delete_window,text='Delete Book',justify='center',font='helvetica 24 bold underline',pady=20)
    close_btn=Button(delete_window,text='Close',relief='groove',bd=3,width=10,height=1,font='helvetica 9',activeforeground='red',command=delete_window.destroy)
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