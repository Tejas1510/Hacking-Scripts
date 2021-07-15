from tkinter import * 
main_window=Tk()
main_window.geometry('500x500')

title=Label(main_window,text='Book Management System',justify='center',font='helvetica 21 bold')
view_button=Button(main_window,text='View All Books',relief='groove',bd=5)
add_button=Button(main_window,text='Add Book',relief='groove',bd=5)
update_button=Button(main_window,text='Update Book',relief='groove',bd=5)
delete_button=Button(main_window,text='Delete Book',relief='groove',bd=5)

title.grid(row=0,column=0)
view_button.grid(row=1,column=0)
add_button.grid(row=1,column=1)
update_button.grid(row=2,column=0)
delete_button.grid(row=2,column=1)

main_window.mainloop()