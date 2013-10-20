(function($){
	var methods = {
		init: function(options){
			var settings = $.extend({
				center: new google.maps.LatLng(39.8106460, -98.5569760),
				zoom: 3,
				mapTypeId: google.maps.MapTypeId.ROADMAP,
				scaleControl: true
			}, options);
			return this.each(function(){
				var that=$(this),
					data=that.data('google_maps'),
					gmap=new google.maps.Map(that[0],settings);
				gmap.setCenter(settings.center);
				if(!data){
					that.data('google_maps', {
						'gmap': gmap,
						'marker':null,
						'geocoder':null
					});
				}
			});
		},
		
		center: function(centerpoint, zoom_level){
			var zoom_level = typeof zoom_level !== 'undefined' ? zoom_level : 11,
				that=$(this),
				data=that.data('google_maps');
			data.gmap.setCenter(centerpoint);
			data.gmap.setZoom(zoom_level);
			that.google_map('set_marker', centerpoint);
			return that.data('google_maps', data);
		},
		
		click: function(handler){
			if(typeof handler === "function"){
				var data=$(this).data('google_maps');
				google.maps.event.addListener(data.gmap, 'click', handler);
			}
		},
		
		set_marker: function(location){
			var that=$(this),data=that.data('google_maps'),marker=null;
			if(data.marker===null){
				marker=new google.maps.Marker({
					position:location,
					map:data.gmap
				});
			}
			else{
				marker=data.marker;
				marker.setPosition(location);
			}
			data.marker = marker;
			return that.data('google_maps', data);
		},
		
		geocode: function(address, callback){
			var that=$(this),data=that.data('google_maps'),
				geocoder = data.geocoder === null ? new google.maps.Geocoder() : data.geocoder;
			geocoder.geocode({address:address}, callback);
		}
	};
	
	$.fn.google_map = function(method){
		if(methods[method]){
			return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
		}
		else if(typeof method === 'object' || ! method){
			return methods.init.apply(this, arguments);
		}
		else {
			$.error('Method '+method+' does not exist on jQuery.google_map');
		}
	}
})(jQuery);