from tkinter import * 
main_window=Tk()
main_window.geometry('520x470')

title=Label(main_window,text='Book Management System',justify='center',font='helvetica 21 bold underline',pady=20,width=30)
view_button=Button(main_window,text='View All Books',relief='groove',bd=4,width=17,height=3,font='helvetica 9 bold',anchor=CENTER)
add_button=Button(main_window,text='Add Book',relief='groove',bd=4,width=17,height=3,font='helvetica 9 bold',anchor=CENTER)
update_button=Button(main_window,text='Update Book',relief='groove',bd=4,width=17,height=3,font='helvetica 9 bold',anchor=CENTER)
delete_button=Button(main_window,text='Delete Book',relief='groove',bd=4,width=17,height=3,font='helvetica 9 bold',anchor=CENTER)
close_button=Button(main_window,text='Close',relief='groove',bd=3,width=10,height=1,font='helvetica 9',activeforeground='red',command=main_window.destroy)

title.place(x=0,y=0)
view_button.place(x=100,y=150)
add_button.place(x=300,y=150)
update_button.place(x=100,y=300)
delete_button.place(x=300,y=300)
close_button.place(x=420,y=425)

main_window.mainloop()