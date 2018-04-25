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

function save_asset(obj){
	var address = $("input[name='address']").val();
	var collection = $("input[name='collection']:checked").val();
	if( collection == 'yes' ){
		$("#deploy-host").html(address);
	}else{
		$(obj).removeAttr('data-target');
	}
	$.ajax({
		type:'POST',
		url:'',
		data:{'address':address,'collection':collection},
		success: function(data){
			if( collection == 'no' ){
				window.location.href='/asset/';
			}
			var dataObj=eval("("+data+")");
			if( dataObj.status == 'success' ){
				$("#modal-body div").remove();
				$("#modal-body #deploying").remove();
				$("#modal-body #deploy-success").html('收集完成');
				$(".modal-footer button").removeClass('disabled');
				$(".modal-footer button").attr('data-dismiss',"modal");
			}
			if( dataObj.status == 'failure' ){
				$("#modal-body div").remove();
				$("#modal-body #deploying").remove();
				$("#modal-body #deploy-failure").html(dataObj.msg);
				$(".modal-footer button").removeClass('disabled');
				$(".modal-footer button").attr('data-dismiss',"modal");
			}
		},
	})
}

function delete_asset_ask(obj){
	thisobj = $(obj);
	address = $(obj).siblings().eq(1).html();
	$("#delete-host").html(address);
}

function delete_asset_ensure(obj){
	$.ajax({
		type:'DELETE',
		data:{'address':address},
		success: function(data){
			var dataObj=eval("("+data+")");
			if( dataObj.status == 'success' ){
				$("#mySuccessAlert").css('display','block');
				$(thisobj).parent().remove();
			}
			if( dataObj.status == 'failure' ){
				$("#myFailureAlert").css('display','block');
				$("#delete-failure").html(dataObj.msg)
			}
		}
		
	})
}

function collection_finish(){
	window.location.href='/asset';
}
