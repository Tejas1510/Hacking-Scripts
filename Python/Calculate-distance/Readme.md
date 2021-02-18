# Distance Calculating Django App
App that can show distance between user's location and searched location on map.

# Packages Used
1. Geopy
2. folium
3. crispy-form
4. Bootstrap

# How to run
**1.**  Fork [this](https://github.com/Tejas1510/Hacking-Scripts) repository.

**2.**  Clone your forked copy of the project.

```
git clone https://github.com/<your_user_name>/Hacking-Scripts.git
```
Navigate to the project directory.
```bash
cd Hacking-Scripts/python/Calculate-distance
```
```
create folder named 'geoip' in main project directory.
```
```
download city and country database
```
[For downloading city and country database ](https://www.maxmind.com/en/accounts/497315/people/84e6213c-91a4-4e02-ae2e-1d709084c544)
1. ![](https://imgur.com/6n7Fac9)
2. ![](https://imgur.com/xwQf6s1)

```
extract the zip files and copy paste 
1. GeoLite2-City.mmdb
2. GeoLite2-country.mmdb
to geoip folder
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py runserver
```
# And here you go
![](https://imgur.com/JKn92eb)
![](https://imgur.com/dJDQi0N)
![](https://imgur.com/N5E4fuF)

# Author
[Pritam Pawar](https://github.com/pritamp17)
