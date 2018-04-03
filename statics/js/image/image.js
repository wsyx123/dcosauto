$(document).ready(function(){
	$("#image-menu div").bind("click",function(){
		var displayobj = $(".image-detail");
		$(displayobj).css('display','none');
		$("#image-menu div").removeAttr("style");
		$("#image-menu div").removeClass("add-underline");
		$(this).addClass("add-underline");
		$(displayobj[$(this).index()]).css('display','block');
	})
	
})

function save_repository(){
	$.ajax({
		type:'POST',
		data:$("#image-form").serialize(),
		success:function(){
			window.location.href="/image/";
		}
	})
}

function refresh_repository(obj){
	var address = $($($(obj).parent()).siblings()[0]).html();
	$.ajax({
		type:'UPDATE',
		data:{'address':address},
		success:function(data){
			var dataObj=eval("("+data+")");
			$($($(obj).parent()).siblings()[3]).html(dataObj.count);
		}
	})
}

function delete_repository(obj){
	var address = $($($(obj).parent()).siblings()[0]).html();
	$.ajax({
		type:'DELETE',
		data:{'address':address},
		success:function(){
			window.location.href="/image/";
		}
	})
}

function download_image(obj){
	var imgobj = $(obj).parent().siblings();
	var host = $(imgobj[3]).html();
	var imginfo = $(imgobj[0]).html();
	var cmds = host+"/"+imginfo
	var imgversion = imginfo.split(':')[1]
	$("#imgversion").html(imgversion);
	$("#cmds").html(cmds);
}