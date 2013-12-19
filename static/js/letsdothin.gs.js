$(document).ready(function() {

	$('.h3-event-title').live('click', function() {
		window.open("https://www.facebook.com/events/" + $(this).attr('eventid'));
	});

})

function not_implemented() {
	alert("Not implemented!");
}