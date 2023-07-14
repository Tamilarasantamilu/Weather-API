from flask import Flask, request, render_template
import requests

app = Flask(__name__)
  
@app.route('/', methods =["GET", "POST"])
def index(): 
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST":       
        cityName = request.form.get("cityName")  
        if cityName:
            url = "https://api.weatherapi.com/v1/current.json?key=48063437325b48b78aa105516222411"
            weatherData = requests.get(url).json()
        else:
            error = 1    
    return render_template('base.html', data = weatherData, cityName = cityName, error = error)
if __name__ == "__main__":
    app.run()