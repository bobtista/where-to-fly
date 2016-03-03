import flight
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<airline>/<airport>')
def hello(airline, airport):
    my_airline = flight.get_airline_by_code(airline)
    my_airport = flight.get_airport_by_code(airport)
    my_airport.destinations = flight.get_routes(my_airline, my_airport)

    return render_template('destinations.html',
                           airline=my_airline.name,
                           airport=my_airport,
                           destinations=my_airport.destinations)

if __name__ == '__main__':
    app.run(debug=True)
