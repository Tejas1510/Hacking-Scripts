import tkinter as tk
from tkinter import ttk
import datetime
import requests
import json
import webbrowser
# -----------------------------------------------------------------------------------------

API_KEY = 'YOUR_API_KEY'

def lineBreaker(text):
    """Break the line after every 80 letters"""
    breaker = ""
    for i in range(0, len(text)):
        breaker += text[i]
        if i % 80 == 0 and i != 0:
            breaker += "\n"
    return breaker


def main_data_window(url_link, tab):
    def live_time():
        time = datetime.datetime.now()
        time = time.strftime("%H:%M:%S")
        time_label.config(text=time)
        time_label.after(1000, live_time)

    # A canvas
    my_canvas = tk.Canvas(tab)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    # A scrollbar
    my_scrollbar = tk.Scrollbar(
        tab, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    # second frame
    second_frame = tk.Frame(my_canvas)

    # adding another window in canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor=tk.NW)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox('all')))
    # Create frame 0
    frame0 = tk.Frame(second_frame)
    frame0.pack(fill=tk.X, pady=(0, 50))

    # Date or Time
    date = datetime.datetime.now()
    date = date.strftime("%d %b. %Y")
    date_time_label = tk.Label(
        frame0, text=f"{date}", font='mssans 21 bold', pady=4)
    date_time_label.pack(side=tk.LEFT, anchor=tk.NE, padx=(19, 0), pady=(9, 9))

    # Heading / Name of the app
    heading_lable = tk.Label(frame0, text="The Daily News",
                             font='fixdays 36 bold italic', fg='red')
    heading_lable.pack(side=tk.LEFT, anchor=tk.NE, padx=(110), pady=(9, 9))

    # Time label
    time_label = tk.Label(frame0, font='mssans 21 bold', pady=4)
    time_label.pack(side=tk.RIGHT, anchor=tk.NW, padx=(9, 29), pady=(9, 9))
    live_time()
    # Container frame
    containter = tk.Frame(second_frame)
    containter.pack(side=tk.LEFT, fill=tk.X)

    # Get news with news API
    url = url_link

    r = requests.get(url)
    news = r.text

    json_news = json.loads(news)
    articless = json_news['articles']

    title_lst = []
    description_lst = []
    url_lst = []
    for article in articless:
        if article['title'] == None:
            title_lst.append('No Data.')
        if article['description'] == None:
            description_lst.append('No Data.')
        else:
            title_lst.append(article['title'])
            description_lst.append(article['description'])
            url_lst.append(article['url'])

    for i in range(len(title_lst)):
        # making variables
        title_lbl = 'title_lbl' + str(i)  # title_lbl0, title_lbl1, .......
        description_lbl = 'description_lbl' + str(i)
        url_lbl = 'url_lbl' + str(i)
        # seperator_lbl = 'seperator_lbl' + str(i)

        # title label
        title_lbl = tk.Label(containter, text=lineBreaker(
            title_lst[i]), justify=tk.LEFT, font='mssans 17 bold', fg='#14213d')
        title_lbl.pack(anchor=tk.W, padx=(10, 0), pady=(5, 0))

        # description lable
        description_lbl = tk.Label(containter, text=lineBreaker(
            description_lst[i]), justify=tk.LEFT, font='mssans 15', fg='#457b9d')
        description_lbl.pack(anchor=tk.W, padx=(10, 0), pady=(5, 0))

        # url label
        url_lbl = tk.Label(containter, text=lineBreaker(
            url_lst[i]), justify=tk.LEFT, font='mssans 13', fg='#d62828', cursor='hand2')
        url_lbl.pack(anchor=tk.W, padx=(10, 0), pady=(5, 0))
        # bind urls
        url_lbl.bind("<Button-1>", lambda e,
                     url=url_lst[i]: webbrowser.open_new(url))

        # seperator line
        seperator_lbl = tk.Label(
            containter, text=f"{'-'*180}", justify=tk.LEFT)
        seperator_lbl.pack(anchor=tk.W)
# ----------------------------------------------------------------------------------------


def fun_open_tab1():
    my_notebook.select(1)


def fun_open_tab2():
    my_notebook.select(2)


def fun_open_tab3():
    my_notebook.select(3)


def fun_open_tab4():
    my_notebook.select(4)


def fun_open_tab5():
    my_notebook.select(5)


def fun_open_tab6():
    my_notebook.select(6)


def fun_open_tab7():
    my_notebook.select(7)


# ------------------------------------------------------------------------------------------
root = tk.Tk()
root.geometry('1000x600')
root.title('The Daily News')
root.iconbitmap(r'D:\Python Projects\News App version 2\Images\nP.ico')

# notebook by ttk
my_notebook = ttk.Notebook(root)
my_notebook.pack(fill=tk.BOTH, expand=1)

# ------------------------------------------------------------------------------------------
# frame 1 or tab 1// Main Tab
frame1 = tk.Frame(my_notebook, bg='#d62828')
frame1.pack(fill=tk.BOTH, expand=1)
# title
title_lbl = tk.Label(frame1, text='The Daily News',
                     font='fixdays 36 bold italic', bg='#d62828', fg='black')
title_lbl.pack(pady=(5, 12))
# Heading
hdn_lbl = tk.Label(frame1, text='Catgories',
                   font='fixdays 31 bold', bg='#d62828', fg='black')
hdn_lbl.pack(pady=(5, 14))
# buttons
btn_texts = ['All', 'Businesss', 'Entertainment',
             'Health', 'Science', 'Sports', 'Technology']
btn_commands = [fun_open_tab1, fun_open_tab2, fun_open_tab3,
                fun_open_tab4, fun_open_tab5, fun_open_tab6, fun_open_tab7]

for i in range(len(btn_texts)):
    choice_btn = "btn" + str(i)
    choice_btn = tk.Button(
        frame1, text=btn_texts[i], command=btn_commands[i], font='massans 18 bold', pady=3, fg='#457b9d', width=13)
    choice_btn.pack(fill=tk.Y, expand=1, pady=(6, 0))
# ------------------------------------------------------------------------------------------
# frame2 or tab2 // child tab1
frame2 = tk.Frame(my_notebook)
frame2.pack()
main_data_window(
    f'http://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}', frame2)
# frame3 or tab3
frame3 = tk.Frame(my_notebook)
frame3.pack()
main_data_window(
    f'http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEY}', frame3)
# frame4 or tab4
frame4 = tk.Frame(my_notebook)
frame4.pack()
main_data_window(
    f'http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={API_KEY}', frame4)
# frame5 or tab5
frame5 = tk.Frame(my_notebook)
frame5.pack()
main_data_window(
    f'http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={API_KEY}', frame5)
# frame6 or tab6
frame6 = tk.Frame(my_notebook)
frame6.pack()
main_data_window(
    f'http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={API_KEY}', frame6)
# frame7 or tab7
frame7 = tk.Frame(my_notebook)
frame7.pack()
main_data_window(
    f'http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={API_KEY}', frame7)
# frame8 or tab8
frame8 = tk.Frame(my_notebook)
frame8.pack()
main_data_window(
    f'http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={API_KEY}', frame8)
# Add tabs to notebook
my_notebook.add(frame1, text='Category', state=tk.HIDDEN)
my_notebook.add(frame2, text='All', state=tk.HIDDEN)
my_notebook.add(frame3, text='Business', state=tk.HIDDEN)
my_notebook.add(frame4, text='Entertainment', state=tk.HIDDEN)
my_notebook.add(frame5, text='Health', state=tk.HIDDEN)
my_notebook.add(frame6, text='Science', state=tk.HIDDEN)
my_notebook.add(frame7, text='Sports', state=tk.HIDDEN)
my_notebook.add(frame8, text='Technology', state=tk.HIDDEN)

root.mainloop()
