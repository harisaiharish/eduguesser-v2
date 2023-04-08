from flask import Flask, request, jsonify
import CRUD
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="geoapiExercises")


@app.route('/Locations', methods=['GET'])
def get_Locations():
    Locations = CRUD.get_Locations()
    return jsonify(Locations)


@app.route('/Locations', methods=['POST'])
def insert_Location():
    Location_details = request.get_json()

    imagePath = Location_details["imagePath"]
    info1 = Location_details['info1']
    info2 = Location_details['info2']
    info3 = Location_details['info3']
    info4 = Location_details['info4']
    info5 = Location_details['info5']
    CountryName = Location_details['CountryName']

    CountryData = geolocator.geocode(CountryName)

    latitude = str(CountryData.latitude)
    longitude = str(CountryData.longitude)

    print(Location_details)
    result = CRUD.new_Location(imagePath, info1, info2, info3, info4, info5, CountryName, latitude, longitude)
    return jsonify(result)


@app.route('/Locations/<int:id>', methods=['PUT'])
def update_Location(id):
    Location_details = request.get_json()

    imagePath = Location_details["imagePath"]
    info1 = Location_details['info1']
    info2 = Location_details['info2']
    info3 = Location_details['info3']
    info4 = Location_details['info4']
    info5 = Location_details['info5']
    CountryName = Location_details['CountryName']

    CountryData = geolocator.geocode(CountryName)

    latitude = str(CountryData.latitude)
    longitude = str(CountryData.longitude)

    result = CRUD.update_Location(id, imagePath, info1, info2, info3, info4, info5, CountryName, latitude, longitude)
    return jsonify(result)


@app.route('/Locations/<int:id>', methods=['DELETE'])
def delete_Location(id):
    result = CRUD.delete_Location(id)
    return jsonify(result)


@app.route('/Locations/<int:id>', methods=['GET'])
def get_Location_by_id(id):
    Location = CRUD.get_by_id(id)
    return jsonify(Location)


@app.route('/Locations/ids', methods=['GET'])
def get_IDs():
    IDs = CRUD.get_IDs()
    print(IDs)
    return jsonify(IDs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8010, debug=True)
