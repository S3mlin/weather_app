import requests
from flask import render_template, request, redirect, url_for
from app import app
from app.forms import SearchForm



def weather_for_city():
    form = SearchForm()
    weather_api = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=bad4ecf479fb84c8f2fa55f34cbaf6ee'.format(
                        form.city_name.data)
    response = requests.get(weather_api)
    return response.json()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    weather = []
        

    if request.method == 'POST' and form.validate_on_submit():
        data = weather_for_city()         
        weather_data = {
            'city' : form.city_name.data,
            'icon' : data['weather'][0]['icon'],
            'pressure' : data['main']['pressure'],
            'temp' : str(round(int(data['main']['temp']) - 273.15, 1)),
            'weather' : data['weather'][0]['main'],
            'description' : data['weather'][0]['description'],
            'humidity' : data['main']['humidity'],
            'feels_like': str(round(int(data['main']['feels_like']) - 273.15, 1))
        }
        weather.append(weather_data)
        return render_template('index.html', form=form, weather=weather, show=True)
    
    return render_template('index.html', form=form, weather=weather, show=False)