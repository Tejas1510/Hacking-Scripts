import psutil

# Not for windows user 
data = psutil.sensors_temperatures()
print("Current Temperature of CPU (celcius): ",data['coretemp'][0][1])