import requests as requests
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

# Импортируем переменные из config.py
app.config.from_pyfile('config.py')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city')
        if city_name:
            # take a variable to show the json data
            r = requests.get(
                'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=40a1ac05de70230abfaa489d3c36c72b')

            # read the json object
            json_object = r.json()
            if json_object['cod'] =="404":
                return render_template('index.html')
                print(json_object)
            else:

            # take some attributes like temperature,humidity,pressure of this
                temperature = int(json_object['main']['temp'] - 273.15)  # this temparetuure in kelvin
                humidity = int(json_object['main']['humidity'])
                pressure = int(json_object['main']['pressure'])
                wind = int(json_object['wind']['speed'])

            # atlast just pass the variables
                condition = json_object['weather'][0]['main']
                desc = json_object['weather'][0]['description']

            return render_template('index.html', temperature=temperature, pressure=pressure, humidity=humidity,
                                   city_name=city_name, condition=condition, wind=wind, desc=desc)
        else:
            return render_template('index.html')

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
