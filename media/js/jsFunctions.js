jQuery(document).on('ready', function(){

	jQuery('nav a').mouseup('click', function(){
		var id = jQuery(this).attr('id');

		var act = jQuery('nav').find('.current').attr('id');
		if(id === act){
			return false;
		}else if(jQuery('#' + id).parent().parent().attr('id') == 'list-service'){
			var service = jQuery(this).attr('id');
			jQuery('.serviciosPage').find('.actived').attr('class' , 'unactived');
			jQuery('div#' + service).attr('class' , 'actived');
			return false;
		}

		listService();
		jQuery.ajax({
			url : '/' + id,
			success : function(html){
				jQuery( "#main" ).find('.' + act + 'Page').remove();
				//jQuery( "#main" ).find('.' + act + 'Page').effect( 'blind', 'fast');
				jQuery( "#main" ).append(html).effect('slide', 'slow');
				changeClass(id);
				if(id == "contacto"){
					setTimeout(function(){
      				initialize();
					},1000);
				}else if(id == "proyectos"){
					scaleImage();
					hoverImage();
				}else if(id == "servicios"){
					jQuery('ul#list-service').show();
					jQuery('header').css('padding-bottom', '50px');
				}
			}
		});

	});

	jQuery('.social_media').find('a').hover(function(){
		var src = jQuery(this).find('img').attr('title');
		var img = '/media/img/' + src + '_hover.png'
		jQuery(this).find('img').attr('src', img);
	}, function(){
		var src = jQuery(this).find('img').attr('title');
		var img = '/media/img/' + src + '.png'
		jQuery(this).find('img').attr('src', img);
	});
	
	jQuery('body').delegate('#btnContact', 'click',function(){
		jQuery('#form_contact').submit(function(){
			var data = jQuery('#form_contact').serialize();

			jQuery.ajax({
				url : '/contact',
				type: 'post',
				data: data,
				dataType: 'json',
				success: function(data){
					// jQuery.parseJSON(data);
					// jQuery('.contactoPage').remove();
					// jQuery('#main').html(data);					
				},
				complete: function(data, dato){
					if(data.readyState == 4){
						if(typeof data.responseJSON == 'undefined'){
							jQuery('.contactoPage').remove();
							jQuery('#main').html(data.responseText);
							initialize();
						}else{
							jQuery('.errorlist').remove();
							jQuery('input[type=text]').val('');
							jQuery('input[type=tel]').val('');
							jQuery('input[type=email]').val('');
							jQuery('textarea').val('');
							jQuery.fancybox(
								'<p>Mensaje enviado exitosamente, gracias por el contacto.</p><br /><p> Me comunicare con Ud. según corresponda.</p>',
								{
									'width' : 350,
									'height': 100
								}
							);
							
						}
						
					}else{
						alert('Ha ocurrido un problema');
					}					
					
				}
			});
			return false;
		});
	});

	jQuery('body').delegate('a#more', 'click', function(){
		var id = jQuery(this).attr('data-id');
		var act = jQuery('nav').find('.current').attr('id');
		if (act == 'servicios') {
			return false;
		}

		jQuery.ajax({
			url : '/servicios',
			success : function(html){
				jQuery( "#main" ).find('.' + act + 'Page').remove();
				jQuery( "#main" ).append(html).effect('slide', 'slow');
				changeClass('servicios');
				jQuery('ul#list-service').show();
				jQuery('header').css('padding-bottom', '50px');

				jQuery('.serviciosPage').find('.actived').attr('class', 'unactived');
				jQuery('.serviciosPage').find('#' + id).attr('class', 'actived');
				
			}
		});

		return false;	
	});

});

function hoverImage(){
	var id = jQuery('img#proyectImage').attr('id');
	jQuery('img#proyectImage').hover(scaleImageOpacity, scaleGrey);
}

function scaleGrey(){
	jQuery(this).animate({"opacity": "0.3"}, 100);
	jQuery(this).parent().next().css('color', '#393535'); //principal
	jQuery(this).css('border-bottom' , '1px solid #f5f5f5');
}

function scaleImage(){
	jQuery("img#proyectImage").animate({"opacity": "0.3"});
}

function scaleImageOpacity(){
	jQuery(this).animate({"opacity": "1"}, 100);
	jQuery(this).parent().next().css('color', '#ea8469'); //secundario
	jQuery(this).css('border-bottom' , '1px solid #ea8469');
}

function changeClass(id){
	jQuery('.current').attr('class', 'link');
	jQuery('#'+ id).attr('class', 'current');

}

function listService(){
	jQuery('ul#list-service').hide();
	jQuery('header').css('padding-bottom', '10px');
}

function initialize () {
	var mapOptions = {
		zoom: 11,
		center: new google.maps.LatLng(-33.5237864105204, -70.78244524999997),
		disableDefaultUI: true,
		zoomControl: false,
		scaleControl: false,
		scrollwheel: false,
		disableDoubleClickZoom: true,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}
 
	var map = new google.maps.Map(document.getElementById('mapa'), mapOptions);

    var icono = new google.maps.Marker({
     	   	position: new google.maps.LatLng(-33.5237864105204, -70.78244524999997),
        	icon: '/media/img/map_marker.png',
        	map: map               
    });
}