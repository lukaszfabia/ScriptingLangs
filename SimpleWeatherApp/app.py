from flask import Flask, render_template, request, redirect, url_for
from WeatherRequest import WeatherRequest
from LocationManager import get_location

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method != 'POST':
        return render_template('base.html')

    city = request.form.get('input')
    return redirect(url_for('search', city=city))


@app.route('/search/<city>', methods=['POST', 'GET'])
def search(city):
    location = get_location(city=city) 
    weather = WeatherRequest(coords=location).wrap_in_data_model()
    return render_template('search.html', data=weather, value=city)


if __name__ == '__main__':
    app.run(debug=True)
