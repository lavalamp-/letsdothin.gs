$(document).ready(function() {

	$('.h3-event-title').click(function() {
		window.open("https://www.facebook.com/events/" + $(this).attr('eventid'));
	});

	$('.span-event-location').click(function() {
		window.open("http://maps.google.com/maps?q=" + $(this).attr('maps-string'));
	});

	$('.event-upvote').click(function() {
		not_implemented();
	});

	$('.event-downvote').click(function() {
		not_implemented();
	});

	$('.event-promote').click(function() {
		not_implemented();
	});

})

function not_implemented() {
	alert("Not implemented!");
}