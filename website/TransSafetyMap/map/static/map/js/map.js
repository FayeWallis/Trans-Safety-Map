window.onload= function(){

    map = L.map('map').setView([41.2273936,-81.6407933], 7.5);
    var osm = new L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png',{ 
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'})

	var dark = new L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}.png', {
		maxZoom: 20,
		attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
	});

	osm.addTo(map)
}