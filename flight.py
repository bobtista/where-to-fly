import csv


class airport():
    def __init__(self, code="", name="", city="", country=""):
        self.code = code  # technically this is IATA
        self.name = name
        self.city = city
        self.country = country
        self.destinations = []


class airline():
    def __init__(self, IATA="", ICAO="", name=""):
        self.IATA = IATA  # two letter code
        self.ICAO = ICAO  # three letter code
        self.name = name


def get_airports():
    all_airports = []

    with open('airport-codes.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_airports.append(airport(code=row['code'],
                                        name=unicode(row['name'], "utf8"),
                                        city=row['city'],
                                        country=row['country']))
    return all_airports


def get_airlines():
    all_airlines = []

    with open('airlines.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_airlines.append(airline(IATA=row['IATA'],
                                        ICAO=row['ICAO'],
                                        name=row['Name']))
    return all_airlines


def get_routes(airline, airport):
    codes = []
    destinations = []
    with open('routes.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if airline.IATA == row['Airline Code'] and \
                    airport.code == row['Origin']:
                codes.append(row['Destination'])
        codes = list(set(codes))
        for code in codes:
            destinations.append(get_airport_by_code(code))
    return destinations


def get_airport_by_code(code, airports=[]):
    if not airports:
        airports = get_airports()
    for airport in airports:
        if airport.code == code:
            return airport
    return None


def get_airline_by_code(ICAO, airlines=[]):
    if not airlines:
        airlines = get_airlines()
    for airline in airlines:
        if airline.ICAO == ICAO:
            return airline
    return None


def main():
    # airports = get_airports()
    my_airport = get_airport_by_code('BOS')  # San Francisco INTL
    # airlines = get_airlines()
    my_airline = get_airline_by_code('UAL')  # United
    my_airport.destinations = get_routes(my_airline, my_airport)
    for destination in my_airport.destinations:
        print "Code: %s, Name: %s" % (destination.code, destination.name)


if __name__ == '__main__':
    main()
