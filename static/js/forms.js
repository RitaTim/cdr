$(document).ready(function(){ 

	var send_form_add_student = function(){
		$.ajax({
			url : "/new-student/add/", 
			type : "POST",
			data : {
				name: $('#id_name').val(),
				phone: $('#id_phone').val(),
				filial: $('#id_filial').val(),
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
			},
			success : function(data) {
				if (data['error']){
					var error_line = "<span class='error-text'>" + data['error']+ "</span>";
					$('.container-form .errors').html(error_line);
					$.each($('.contact-form input[type=text]'), function(){
						if ($(this).val() == ""){
							$(this).addClass('empty-field');
						};
					})
					$.each($('.empty-field'), function(){
						$(this).on('click', function(){
							$(this).removeClass('empty-field');
						})
					})
				} else {
					$('.modal-content').html(data);
				}
			},
			error : function(err) {
				alert("Fail GET /new-student/add/");
			}
		})
	}


	$('#form-register-class').on('submit', function(event){
		event.preventDefault();
		send_form_add_student();
	})

	$("#id_phone").mask("+7 (999) 999-99-99");
	
})