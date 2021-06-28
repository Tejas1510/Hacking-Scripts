from matplotlib  import pyplot

x = []
y = []

a =int(input("Enter the number of values that you want to represent in Bar graph : "))
print("X-axis")
for i in range(a):
    p = int(input(f"Enter the {i+1} value on X axis : "))
    x.append(p)
print("Y-axis")
for j in range(a):
    q = int(input(f"Enter the {j+1} value on Y axis : "))
    y.append(q)

#To set the name of the window
fig = pyplot.gcf()
fig.canvas.set_window_title("BAR GRAPH")

#To set title of the window
pyplot.title("Bar Graph representation")

pyplot.bar(x,y)
pyplot.show()
