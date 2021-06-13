# Import the required packages

from tkinter import *

# Creating the window

root = Tk()
root.geometry("530x350")
root.title("Get Covid-19 Data Country Wise")


def show_grouped_data():
    
    from matplotlib import pyplot as plt
    
    from covid import Covid
    
    import numpy as np

    covid = Covid()
    
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []
    
    try:
        
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",") 
        country_names = country_names.split(",")
        
        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
        print(cases)
        for y in cases:
            
            confirmed.append(y["confirmed"])
            
            active.append(y["active"])
            
            deaths.append(y["deaths"])
            
            recovered.append(y["recovered"])

        
        bar1 = np.arange(len(country_names))
        bar2 = [i+0.2 for i in bar1]
        bar3 = [i+0.2 for i in bar2]
        bar4 = [i+0.2 for i in bar3]

        plt.bar(bar1, confirmed, 0.2, color='red', label='Confirmed')
        plt.bar(bar2, recovered, 0.2, color='green',label='Recovered')
        plt.bar(bar3, active, 0.2, color='blue', label='Active')
        plt.bar(bar4, deaths, 0.2, color='black', label='Deaths')

        plt.legend()
        
        plt.title('Current Covid Cases (Grouped Bar Graphs)')
        plt.xlabel('Country Name')
        plt.ylabel('Cases(in millions)')
        plt.xticks(bar1+0.3,country_names)
        
        plt.show()

    except Exception as e:
        
        data.set("Enter correct details again (or) Check your internet connection")



Label(root, text="COVID-19 Tracker", font=("Times", "30", "bold italic"),bg='black',fg='white').pack(fill=X)
Label(root, text="Enter country names:",font=('ariel' ,15,'bold')).pack(pady=20)
data = StringVar()
data.set("Seperate country names using comma or space(not both)")
entry = Entry(root, textvariable=data, font=('ariel' ,10,'bold'), width=70,bd=5).pack()
Label(root).pack()
Button(root, text="Show Data in Grouped Bar Graphs",bg='green',fg='white',font=('ariel' ,10,'bold'), command=show_grouped_data).pack(pady=20)

root.mainloop()

        