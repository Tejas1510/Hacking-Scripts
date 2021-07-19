import sqlite3
class BookData():
    def __init__(self):
        self.conn=sqlite3.connect('books.db')
        self.cur=self.conn.cursor()
        self.cur.execute('create table if not exists book (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)')
        self.conn.commit()

    def insert_in_database(self,title,author,year,isbn):
        self.cur.execute('insert into book values (null,?,?,?,?)',(title,author,year,isbn))
        self.conn.commit()


    def view_data(self):
        self.cur.execute('select * from book')
        view=self.cur.fetchall()
        return view

    def search_in_database(self,title='',author='',year='',isbn=''):

        self.cur.execute('select * from book where title=? or author=? or year=? or isbn=?',(title,author,year,isbn))
        search=self.cur.fetchall()
        return search  

    def update_record(self,id,title,author,year,isbn):
        self.cur.execute('update book set title=?,author=?,year=?,isbn=? where id=?',(title,author,year,isbn,id))
        self.conn.commit()

    def delete_record(self,id):
        self.cur.execute('delete from book where id=?',(id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()