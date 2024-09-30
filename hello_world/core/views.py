from django.shortcuts import render
from ..models import RequestRecord
import requests

def fun_view(request):
    name = None
    city = None
    temperature = None

    if request.method == 'POST':
        name = request.POST.get('name')  # Get the name from the form
        city = request.POST.get('city') # Get the city from the form'
        url = "https://wttr.in/"+city+"?format=%C+%t"  # Return only condition and temperature
        response = requests.get(url) # Get the current temperature 
        temperature = response.text  # Extract temperature as text
        
        # After getting the request sorted out, store to the DB
        RequestRecord.objects.create(
            name = name,
            city = city,
            temperature = temperature
        )
        
    return render(request, 'index.html', {'name': name, 'weather_data': temperature})

def info_view(request):
    return render(request, 'info.html')

