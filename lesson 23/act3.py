Country_Code = {'India' : '0091',
'Australia' : '0025',
'Nepal' : '00977'}

#search dictionary for country code of India
print("Country Code for India -")
print(Country_Code.get('India', 'Not Found'))

#search dictionary for country code of Japan
print("Country Code for Japan -")
print(Country_Code.get('Japan', 'Not Found'))