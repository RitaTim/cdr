$(document).ready(function(){
	var load_map = function(map_id){
		var posLatitude = parseFloat($('#' + map_id).data('position-latitude'));
		var posLongitude = parseFloat($('#' + map_id).data('position-longitude'));
		var metka_url = $('#' + map_id).data('marker-img');
		var metka_title = $('#' + map_id).data('marker-title');

		var options = {
			center: {lat: posLatitude, lng: posLongitude},
			zoom: 15,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			mapTypeControl: false,
			scaleControl: false,
			streetViewControl: false,
			panControl: true,
			disableDefaultUI: true,
			zoomControlOptions: {
				style: google.maps.ZoomControlStyle.DEFAULT
			},
			overviewMapControl: true,
		};

		window[map_id] = new google.maps.Map(document.getElementById(map_id), options);

		google.maps.event.trigger(window[map_id], 'resize');

		var icon = {
			url: metka_url,
			origin: new google.maps.Point(0, 0)
		};

		var marker = new google.maps.Marker({
			position: {lat: posLatitude, lng: posLongitude},
			map: window[map_id],
			title: metka_title,
			icon: icon,
			draggable: false
		});

	} //end load_map


	$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
		map_id = 'map-' + $(e.target).data('map-id');
		load_map(map_id);
	});

	map_id = 'map-' + $('.nav-tabs li :first').data('map-id');
	load_map(map_id);
});