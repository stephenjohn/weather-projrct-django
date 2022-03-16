from email import message
from pyexpat.errors import messages
from time import timezone
from django.shortcuts import render
import json
import urllib.request
from django.contrib import messages 
from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    if request.method == 'POST':
        serch = request.POST['serch']
        res = urllib.request.urlopen ('https://api.openweathermap.org/data/2.5/weather?q='+serch+'&units=imperial&appid=c5a3791006ae7a1aecdd82126fff3719')
        json_data = json.load(res)
        data = {
            "country_code":str(json_data['sys']['country']),
            "temp":str(json_data['main']['temp']) + '°F' ,
            "pressure":str(json_data['main']['pressure']) + 'hpa',
            "humidity":str(json_data['main']['humidity']) +'%',
            "coordinate":str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']), 
            "temp_min":str(json_data['main']['temp_min']) + '°F',
            "temp_max":str(json_data['main']['temp_max']) + '°F',
            "timezone":str(json_data['timezone']) + ' unix',
            "sunrise":str(json_data['sys']['sunrise']) + ' unix',
            "description":str(json_data['weather'][0]['description']),
            "windspeed":str(json_data['wind']['speed']) + 'kph',
            "visibility":str(json_data['visibility']),
            
            
            

            
            

        }


  
    else:
        serch = ''
        data = {}
    return render(request,'/Users/sangeetha/Downloads/weatherproject/weather/templates/index.html',{'serch':serch, 'data':data})
    