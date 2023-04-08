import json
import random
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
import requests
from werkzeug.exceptions import abort
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from playsound import playsound

clue = []
RoundNum = 0
scores = []
usedIDs = []
distances = []

gCountryObjs = []
cCountryObjs = []

isOnLand = 0

api_endpoint = "http://127.0.0.1:8010/Locations"

app = Flask(__name__)
app.config["SECRET_KEY"] = "Randomfbsduifgeiufdwi"

geolocator = Nominatim(user_agent="geoapiExercises")  # Decode Coordinates

NUM_OF_ROUNDS = 5


# Non Routing Functions---------------------------------------------------------------------

# Update Score based on Distance
def score():
    cCountry = cCountryObjs[RoundNum - 1]
    gCountry = gCountryObjs[RoundNum - 1]

    gCountryName = str(gCountry.address)
    cCountryName = str(cCountry.address)

    global scores
    global distances

    if gCountryName == cCountryName:
        scores.append(1000)
        distances.append(0)
        playsound("static/sounds/yes.mp3")
    else:
        distance = getDistanceBetween((cCountry.latitude, cCountry.longitude), (gCountry.latitude, gCountry.longitude))
        distances.append(distance)
        # Shrink 1 - 18000 km possible range to a score between 1 and 1000
        OldRange = 20000
        NewRange = 900
        scores.append((int(900 - ((distance * NewRange) / OldRange))))

    if clue[RoundNum - 1] == 1:
        scores[RoundNum - 1] = scores[RoundNum - 1] * 0.75


# Convert a Dictionary Pair of Coordinates to the Country Object
def LatLong_to_Country(coords):  # Function to get Location from Coordinates
    location = geolocator.reverse(coords, zoom=3, language="en")  # zoom sets it to country only
    return location


# Find the Distance in km between two Pairs of Coordinates
def getDistanceBetween(c1, c2):
    return geodesic(c1, c2).km


# END---------------------------------------------------------------


# Home Page, Only renders the HTML
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


# Functions which do I/O in JSON with the javascript----------------------------------------------------
@app.route('/ClickData')
def WaterLand():
    return jsonify(isOnLand)


# Sets Clue to 1 if hint is used
@app.route('/clue', methods=['POST'])
def clueUsed():
    global clue
    clue[RoundNum - 1] = 1
    return "filler return statement"


# Receives Coordinates from click on map
@app.route('/jsonMapInput', methods=['POST'])
def test():
    global isOnLand

    if request.method == 'POST':
        output = eval(request.get_json())

        coordTuple = (output['lat'], output['lng'])
        if LatLong_to_Country(coordTuple) is None:
            isOnLand = 0
            return json.dumps({'success': True})

        isOnLand = 1
        gCountryObjs.append(LatLong_to_Country(coordTuple))

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


# END ----------------------------------------------------------------------------------------------
# Functions for displaying new locations

# Called at start of every game, resets all Variables
@app.route('/play')
def play():
    global usedIDs
    global clue
    global RoundNum
    global scores
    global distances

    global gCountryObjs
    global cCountryObjs

    cCountryObjs = []
    gCountryObjs = []

    distances = []
    usedIDs = []
    clue = []
    RoundNum = 0
    scores = []

    return redirect(url_for('newrandom'))


# Called every round to choose new random ID, reset some variables
@app.route('/new')
def newrandom():
    global clue
    global RoundNum
    clue.append(0)  # This will be changed to 1 IF clue is used
    RoundNum += 1

    global usedIDs

    if RoundNum <= NUM_OF_ROUNDS:
        LocationIDs = requests.get(f"{api_endpoint}/ids").json()
        IDs = [i[0] for i in LocationIDs]

        randomID = random.choice(IDs)  # Choose a random ID not already used
        while randomID in usedIDs:
            randomID = random.choice(IDs)

        usedIDs.append(randomID)

        return redirect(url_for('displayLocation', id=randomID))

    else:
        return redirect(url_for('GameEnd'))


# Displays Location of ID with relevant information
@app.route('/<int:id>')
def displayLocation(id):
    LocationData = requests.get(f"{api_endpoint}/{id}").json()
    cCountryObjs.append(LatLong_to_Country((LocationData[8], LocationData[9])))

    if LocationData is None:
        abort(404)

    return render_template('displayLocation.html', LocationData=LocationData)


# END---------------------------------------------------------------------------------------------------
# Functions for Displaying Map, Guessing, EndScreen
@app.route('/map')
def map():
    return render_template('map.html')


# Displays Relevant Information about Guess
@app.route('/guessed')
def guessed():

    score()  # Updates Score

    cCountry = cCountryObjs[RoundNum - 1]
    gCountry = gCountryObjs[RoundNum - 1]

    return render_template('guessedpage.html',
                           distance=distances[RoundNum - 1],
                           cCountry=cCountry.address,
                           gCountry=gCountry.address,
                           Correct=(gCountry.address == cCountry.address),
                           Score=scores[RoundNum - 1],
                           glatlng=(gCountry.latitude, gCountry.longitude),
                           clatlng=(cCountry.latitude, cCountry.longitude)
                           )


# Game End Screen
@app.route('/congratulations')
def GameEnd():
    totalScore = sum(scores)
    return render_template('gameover.html', score=totalScore)  # Still need to make End Screen html


# END------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8007, debug=False)
