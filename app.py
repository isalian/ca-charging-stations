# http://flask.pocoo.org/
# https://dashboard.heroku.com/apps/dandan1111/deploy/heroku-git
# https://github.com/datademofun/heroku-basic-flask


from flask import Flask
from flask import render_template
from getdata import get_stations, get_stations_by_zipcode, count_station_ownership, get_station_by_id, get_zipcodes


app = Flask(__name__)

@app.route("/")
def homepage():
    stations = get_stations()
    return render_template('index.html', stations=stations, zipcodes=get_zipcodes())

@app.route("/zip/<zipcode>")
def zippage(zipcode):
    stations = get_stations_by_zipcode(zipcode)
    return render_template('zip.html',
        stations=stations, zipcode=zipcode, ownership_count=count_station_ownership(stations))

@app.route("/station/<idval>")
def stationpage(idval):
	station = get_station_by_id(idval)
	return render_template('station.html', station=station)
 

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
