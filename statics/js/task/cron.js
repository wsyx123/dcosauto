$(document).ready(function(){
	$("#image-menu div").bind("click",function(){
		var displayobj = $(".image-detail");
		$(displayobj).css('display','none');
		$("#image-menu div").removeAttr("style");
		$("#image-menu div").removeClass("add-underline");
		$(this).addClass("add-underline");
		$(displayobj[$(this).index()]).css('display','block');
	});
})









