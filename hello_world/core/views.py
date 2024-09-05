from django.shortcuts import render
import requests

def fun_view(request):
    name = None
    city = None
    weather_data = None

    if request.method == 'POST':
        name = request.POST.get('name')  # Get the name from the form
        city = request.POST.get('city') # Get the city from the form'
        url = "https://wttr.in/"+city+"?format=%C+%t"  # Return only condition and temperature
        response = requests.get(url) # Get the current temperature in Sacramento
        weather_data = response.text  # Extract temperature as text
    return render(request, 'index.html', {'name': name, 'weather_data': weather_data})

