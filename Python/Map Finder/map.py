#import Nominatim, folium and webbrowser packages
from geopy.geocoders import Nominatim
import folium
import webbrowser

locator = Nominatim(user_agent='http://open.mapquestapi.com/nominatim/v1/search.php')

#get the location and covert it into lowercase
loc = input('Enter the location : ')
#get the coordinates of your loction
loc = locator.geocode(loc)
#Map method of folium return Map object
#pass the coordinates of your location
mp=folium.Map(location= [loc.latitude,loc.longitude],zoom_start= 15)

#adds parachute style marker with pop-up text
folium.Marker([loc.latitude,loc.longitude],popup = loc).add_to(mp)

#save your map and open it using webbrowser
mp.save('map.html')
webbrowser.open('map.html')