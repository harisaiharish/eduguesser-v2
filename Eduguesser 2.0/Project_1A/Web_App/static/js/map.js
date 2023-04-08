//Map Creation
var map = L.map('map').setView([30, 0], 2); //CHANGE params so that global map, minimum zoom

map.options.minZoom = 2;
map.options.maxZoom = 8;
map.setMaxBounds(  [[-90,-180],   [90,180]]  )

L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    maxZoom: 8,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
}).addTo(map);

//-------------------------------------------------------------------------------------------------

//e (Event) for Click
function onMapClick(e) {
    if(confirm("Confirm guess")){
//alert("You clicked the map at " + e.latlng); //This can be removed
        const s = JSON.stringify(e.latlng);

         $.ajax({ //Sends to Flask with POST
                url:"/jsonMapInput",
                type:"POST",
                contentType: "application/json",
                data: JSON.stringify(s), //Check with and without Stringify
                success: function (){
                    $.ajax({
                        url:"/ClickData",
                        type:"GET",
                        contentType: "application/json",
                        success: function(data){
                           if(data == 1){
                                window.location.href = window.location.origin + "/guessed"
                            }
                           if(data == 0){
                               alert("Don't guess water")
                           }
                        }
                    });
                }
         });
    }
}

map.on('click', onMapClick);
