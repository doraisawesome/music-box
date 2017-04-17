$(document).ready(function(){
	/*
	$('#logIn').on('click', function(){
		window.location.href = "../../musicbox/home.html";
	});
	$('#signUp').on('click', function(){
		window.location.href = "../../musicbox/templates/musicbox/createAccount.html";

	});*/

	$('.nav a:contains("page2")').parent().addClass('active');

 /*$("input:radio[name=rating]").click(function(){
        var value = $(this).val();
        alert(value);
});*/
$('.starRating').children().prop('disabled', true);
});

