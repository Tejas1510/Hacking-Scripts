#reading the currency file first
with open('currency') as f:
    lines=f.readlines()
print(lines)
currencyDict= {}
# fetching all data
for line in lines:
    parsed=line.split("\t")
    currencyDict[parsed[0]]=parsed[1]
print(currencyDict)
amount=int(input("enter the amount: \n"))
print("Enter the name of the country of which you want to convert currency")
print("Available options for conversion is: \n")
[print(item)for item in currencyDict.keys() ]
currency=input("Please enter the currency you want to convert")
print(f"{amount} INR is equal to  {amount*float(currencyDict[currency])}"  f"{currency}")