## A python script to get a map of any specified location using geopy, folium, and webbrowser packages.



## Requirements :

1) Install geopy and folium packages<br>
```
      pip install geopy
      pip install folium \\ it is used to return map object
```
2) Run the code
```
python map.py
```
## Implementation Example -
![](https://raw.githubusercontent.com/Paras0-7/Hacking-Scripts/main/Python/Map%20Finder/Screenshot.png)<br>

## Methodology :

1) Import Nominatim, folium, webbrowser

2) Create a Nominatim object and provide it a user agent to find your location. 

3) Get the location for which you want to get the map.

4) Use geocode method of Nominatim to get the coordinates of your location.

5) Pass the latitude and longitude of your location to the map function of the folium package.

6) Use the Marker method of the folium package to get a parachute style marker over your location

7) Save your map and open it using the webbrowser package to view it.

Scroll through your map to see your nearby locations.




Check out my GitHub profile [Paras0-7](https://github.com/Paras0-7)


