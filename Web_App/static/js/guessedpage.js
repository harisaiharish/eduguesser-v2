
var map = L.map('map').setView([30, 0], 4);

L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    maxZoom: 8,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
}).addTo(map);

var cmarker = new L.Marker(coord1);
var gmarker = new L.Marker(coord2);

cmarker.addTo(map)
gmarker.addTo(map)

var markers = new L.featureGroup([cmarker, gmarker]);
map.fitBounds(markers.getBounds().pad(0.25));

var pointList = [coord1, coord2];

var firstpolyline = new L.Polyline(pointList, {
    color: 'red',
    weight: 3,
    opacity: 0.5,
    smoothFactor: 1
});
firstpolyline.addTo(map);


function drawLine(){
}

