import urllib.request
import json
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=8d91deb27dac403bc5363b959eae2f2f').read()
        json_data = json.loads(res)
        
        temp_in_kelvin = float(json_data['main']['temp'])
        temp_in_celsius = round(temp_in_kelvin - 273.15, 2)  
        # print(json_data)
        longitude=''
        latitude=''
      
        if (json_data['coord']['lon'])<0:
            x=0-(json_data['coord']['lon'])
           
            longitude=str(x) +' E'
        else:
            longitude=' '+str(json_data['coord']['lon'])+ ' W' 
        if (json_data['coord']['lat']) <0 :
            x=0-(json_data['coord']['lat'])
            latitude=str(x)+' S'
        else:
            latitude =str(json_data['coord']['lat'])+'N'
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinates': latitude + ' , ' + longitude,
            'temp': str(temp_in_celsius) + '°C',
            'pressure': (str(json_data['main']['pressure'])+'mb'),
            'humidity': str(json_data['main']['humidity'])+'%',
            'city': city
        }
    else:
        data = {}
        
    return render(request, 'index.html', data)
