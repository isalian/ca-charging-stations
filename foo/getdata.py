from os.path import join
import csv

DATA_DIR = join('static', 'data')
DATA_FILENAME = join(DATA_DIR, 'altfuelslim.csv')


def get_stations():
    with open(DATA_FILENAME) as f:
        data = list(csv.DictReader(f))
    return data


def get_stations_by_zipcode(zipcode):
    zipstations = []
    for s in get_stations():
        if s['zipcode'] == zipcode:
            zipstations.append(s)
    return zipstations


def count_station_ownership(stations):
    thecount = {'Private': 0, 'Public': 0}

    for s in stations:
        ox = s['groups_with_access_code'].upper()
        if 'PUBLIC' in ox:
           thecount['Public'] += 1
        elif 'PRIVATE' in ox:
            thecount['Private'] += 1

    return thecount


