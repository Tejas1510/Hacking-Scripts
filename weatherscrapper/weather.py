
from tkinter import *
from tkinter import messagebox


def tell_weather() :


    import requests, json


    api_key = "dd9f8a17ae0b73d205cbf9b3b6bcc39f"


    base_url = "http://api.openweathermap.org/data/2.5/weather?"



    city_name = city_field.get()


    complete_url = base_url + "appid =" + api_key + "&q =" + city_name


    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=25bb0be2a718d9cc2c9bf60994549146")


    x = response.json()

    if x["cod"] != "404" :


        y = x["main"]


        current_temperature = y["temp"]
        current_temperatureDegree=current_temperature-273.5
        finalTemp=round(current_temperatureDegree,2)

        current_pressure = y["pressure"]


        current_humidiy = y["humidity"]


        z = x["weather"]


        weather_description = z[0]["description"]
        min_temp=y["temp_min"]
        min1=min_temp-273.5
        min2=round(min1,2)
        max_temp=y["temp_max"]
        max1=max_temp-273.5
        max2=round(max1,2)

        temp_field.insert(15, str(finalTemp) + " degree")
        atm_field.insert(10, str(current_pressure) + " hPa")
        humid_field.insert(15, str(current_humidiy) + " %")
        desc_field.insert(10, str(weather_description) )
        min_field.insert(15, str(min2) + " degree")
        max_field.insert(15, str(max2) + " degree")



    else :


        messagebox.showerror("Error", "City Not Found \n"
                             "Please enter valid city name")


        city_field.delete(0, END)



def clear_all() :
    city_field.delete(0, END)
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)
    min_field.delete(0,END)
    max_field.delete(0,END)


    city_field.focus_set()



if __name__ == "__main__" :


    root = Tk()


    root.title("Weather Predicter")


    root.configure(background = "light grey")


    root.geometry("745x685")


    headlabel = Label(root, text = "Weather Predictor",
                      fg = 'red', bg = 'light pink',font="Times 24",padx="10",pady="10")


    label1 = Label(root, text = "City name : ",
                   fg = 'red', bg = 'light pink',font="Times 16")


    label2 = Label(root, text = "Temperature :",
                   fg = 'red', bg = 'light pink',font="Times 16")


    label3 = Label(root, text = "atm pressure :",
                   fg = 'red', bg = 'light pink',font="Times 16")


    label4 = Label(root, text = "humidity :",
                   fg = 'red', bg = 'light pink',font="Times 16")


    label5 = Label(root, text = "description  :",
                   fg = 'red', bg = 'light pink',font="Times 16")
    label6 = Label(root, text = "Minimun Temp",
                   fg = 'red', bg = 'light pink',font="Times 16")
    label7 = Label(root, text = "Maximum Temp",
                   fg = 'red', bg = 'light pink',font="Times 16")



    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 1, column = 0, sticky ="E")
    label2.grid(row = 3, column = 0, sticky ="E")
    label3.grid(row = 4, column = 0, sticky ="E")
    label4.grid(row = 5, column = 0, sticky ="E")
    label5.grid(row = 6, column = 0, sticky ="E")
    label6.grid(row = 7, column = 0, sticky ="E")
    label7.grid(row = 8, column = 0, sticky ="E")



    city_field = Entry(root,font = "Calibri 18")
    temp_field = Entry(root,font = "Calibri 18")
    atm_field = Entry(root,font = "Calibri 18")
    humid_field = Entry(root,font = "Calibri 18")
    desc_field = Entry(root,font = "Calibri 18")
    min_field=Entry(root,font = "Calibri 18")
    max_field=Entry(root,font = "Calibri 18")


    city_field.grid(row = 1, column = 1, ipadx ="150",ipady="7",padx="10",pady="10")
    temp_field.grid(row = 3, column = 1, ipadx ="150",ipady="7",padx="10",pady="10")
    atm_field.grid(row = 4, column = 1, ipadx ="150",ipady="7",padx="10",pady="10")
    humid_field.grid(row = 5, column = 1, ipadx ="150",ipady="7",padx="10",pady="10")
    desc_field.grid(row = 6, column = 1, ipadx ="150",ipady="7",padx="10",pady="10")
    min_field.grid(row = 7, column = 1, ipadx ="150",ipady="7",padx="10",pady="10")
    max_field.grid(row = 8, column = 1, ipadx ="150",ipady="7",padx="10",pady="10")


    button1 = Button(root, text = "Submit", bg = "red",
                     fg = "black", command = tell_weather,font="Times 18")


    button2 = Button(root, text = "Clear", bg = "red",
                     fg = "black", command = clear_all,font="Times 18")


    button1.grid(row = 2, column = 1)
    button2.grid(row = 10, column = 1)


    root.mainloop()
