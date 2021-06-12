from countryinfo import CountryInfo


country_name="India"
a= CountryInfo(country_name)

info_1=a.alt_spellings()
print(info_1)

info_2= a.capital()
print(info_2)

info_3= a.languages()
print(info_3)

info_4=a.timezones()
print(info_4)

info_5=a.currencies()
print(info_5)

info_6=a.area()
print(info_6)

info_7=a.borders()
print(info_7)

info_8=a.calling_codes()
print(info_8)

info_9= a.wiki()
print(info_9)

info_10=a.info()
for p,q in info_10.items():
    print(f'{p}     {q}')