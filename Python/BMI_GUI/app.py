# BMI Application
# Script to create a GUI App that calculates BMI of a person
# Author - Sandip Dutta

# Funtion to calculate the BMI, given height and weight
# We have added height in cms and weight in Kgs (?)
import tkinter as tk


def getBMI(height: float, weight: float) -> float:
    # Returns calculated BMI
    # height is in cms, convert to metres
    cm_to_m = 0.01
    height_in_metres = cm_to_m * height
    return round(weight / (height_in_metres * height_in_metres), 3)


# main app setup
root = tk.Tk(className=" Calculate BMI")

# Setup of main layout
main_canvas = tk.Canvas(root, width=400, height=300)
main_canvas.pack()

# App heading mentioning what type of app it is
app_heading = tk.Label(root, text='Calculate BMI')
app_heading.config(font=('monospace', 20, 'bold'))
main_canvas.create_window(200, 20, window=app_heading)

# widget to Get the value of height
height_box = tk.Entry(root)
main_canvas.create_window(100, 100, window=height_box)

# Height Label
height_label = tk.Label(root, text='Enter Height (cms)')
app_heading.config(font=('arial', 15, 'bold'))
main_canvas.create_window(100, 85, window=height_label)

# widget to get the value of weight
weight_box = tk.Entry(root)
main_canvas.create_window(300, 100, window=weight_box)

# Weight Label
weight_label = tk.Label(root, text='Enter Weight (kgs)')
app_heading.config(font=('arial', 15, 'bold'))
main_canvas.create_window(300, 85, window=weight_label)

# Function to get and display BMI from widgets


def show_bmi_from_entries() -> None:
    # Calcultes BMI,
    height = height_box.get()
    weight = weight_box.get()
    #
    bmi = getBMI(height=float(height), weight=float(weight))

    bmi_info_label = tk.Label(root, text='Your BMI is')
    main_canvas.create_window(200, 210, window=bmi_info_label)

    bmi_value = tk.Label(root, text=bmi, font=('helvetica', 10, 'bold'))
    main_canvas.create_window(200, 230, window=bmi_value)


# Button to calculate the BMI of person
get_bmi_button = tk.Button(text='Calculate BMI', command=show_bmi_from_entries)
main_canvas.create_window(200, 180, window=get_bmi_button)

# MAIN _LOOP
root.mainloop()
