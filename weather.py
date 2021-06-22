import requests
#import os
from datetime import datetime

api_key = '35b421c8e3a7a45fd2152de2a8d71a28'
location = input("Enter your city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

w_file = open("W_report.txt", "w")
#creating a file to redirect the values and the values change dynamically after repeated execution of program

#here only the current requested weather report is generated and saved in W_report.txt file 
print ("-------------------------------------------------------------",file=w_file)
print ("Weather Statistics for - {}  || {}".format(location.upper(), date_time),file=w_file)
print ("-------------------------------------------------------------",file=w_file)

print ("Current temperature is: {:.2f} deg C".format(temp_city),file=w_file)
print ("Current weather desc  :",weather_desc,file=w_file)
print ("Current Humidity      :",hmdt, '%',file=w_file)
print ("Current wind speed    :",wind_spd ,'kmph',file=w_file)

w_file. close()#closing the file after redirection is done