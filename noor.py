import requests
from datetime import datetime

filename = 'WeatherData.txt'
with open(filename,'a') as file_object:
  file_object.write(f"\t\t\t\t\t\t{'-' * 15}SEARCH HISTORY...{'-' * 15}\n\n\n")

for i in range(0,4):
  
  api_key='bb323062c1bac4981f485e655746dfad'
  location =  input("Enter your city/State name : \n")
  complete_api_link ="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
  api_link = requests.get(complete_api_link)
  api_data= api_link.json()

  temp_city = ((api_data['main']['temp']) -273.15)
  wether_desc = api_data['weather'][0]['description']
  hmdt = api_data['main']['humidity']
  wind_spd= api_data['wind']['speed']
  date_time= datetime.now().strftime( "%d %b %y | %I:%M:%S %p")




  print("/////////////////////////////////////////////////")
  print("weather  of  ={} || {} ".format(location.upper(), date_time))
  print("/////////////////////////////////////////////////\n\n\n")

  print("Current Temprature is :{:.2f} deg C". format(temp_city))
  print("Current wether desc :  ", wether_desc)
  print("Current humidity    :  " , hmdt,'%')
  print("Current wind speed  :  ",wind_spd ,'kmph\n')

  filename = 'WeatherData.txt'
  with open(filename,'a') as file_object:
    file_object.write(f"{location} {date_time}\nCurrent Temprature is : {temp_city}\nCurrent wether desc :{wether_desc}\n" 
                   f"Current humidity    : {hmdt}\nCurrent wind speed  : {wind_spd}\n\n\n")