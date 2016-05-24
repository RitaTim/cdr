$(document).ready(function(){ 

	var get_article = function(id_article, url){
		$.ajax({
			url : url, 
			type : "GET",
			data : {},
			success : function(data) {
				$('.page-content').html(data);
			},
			error : function(err) {
				alert("Fail GET " + url);
			}
		})
	}

	$(".side-menu li").on('click', function(){
		$(".side-menu li.active").removeClass('active');
		$(this).addClass('active');
		var id_article = $(this).data('id-article');
		var url = "/encyclopedia/" + $('.side-menu').data('section') + "/" + id_article + "/";
		get_article(id_article, url);
	})

	$(".side-menu li:first").click();

})