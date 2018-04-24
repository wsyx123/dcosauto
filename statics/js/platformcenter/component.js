$(document).ready(function(){
	var settime = setInterval(function(){
		$.ajax({
			type: 'GET',
			url: '/platform/manage/status/',
			success: function(data,status,rhx){
				dataobj = eval('('+data+')');
				currentobj = $("#component-list table tbody tr");
				for(var i=0;i<currentobj.length;i++){
					name = $(currentobj[i]).children().eq(1).html();
					for(obj in dataobj){
						if(obj == name && dataobj[obj] == 'up'){
							$(currentobj[i]).children().eq(8).html('<span style="background-color:#006400;color:white;">up</span>');
						}
						if(obj == name && dataobj[obj] == 'down'){
							$(currentobj[i]).children().eq(8).html('<span style="background-color:#880000;color:white;">down</span>');
						}
					}
					
				}
			}
		})
	},50000);
	
})

function deploy_component(){
	$("#deploy-host").html($("select[name='host']").val());
	$("#deploy-name").html($("input[name='name']").val());
	$.ajax({
		type:'POST',
		url:'',
		data:$("#component-form").serialize(),
		success: function(data){
			var dataObj=eval("("+data+")");
			if( dataObj.status == 'success' ){
				$("#modal-body div").remove();
				$("#modal-body #deploying").remove();
				$("#modal-body #deploy-success").html('部署完成');
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

function delete_component_ask(obj){
	thisobj = $(obj);
	name = $(obj).siblings().eq(1).html();
	host = $(obj).siblings().eq(2).html();
	$("#delete-host").html(host);
	$("#delete-name").html(name);
}

function delete_component_ensure(obj){
	$.ajax({
		type:'POST',
		url:'delete/',
		data:{'name':name,'host':host},
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

function deploy_finish(){
	window.location.href='/platform/manage/';
}

function change_data_row(obj){
	var datarow = $(obj).find("option:selected").val();
	$.ajax({
		type:'GET',
		data:{'datarow':datarow},
		success:function(data){
			document.body.innerHTML = data;
			$("#component-footer").append('<script src="/static/js/base/base.js"></script>');
			if( datarow == 5 ){
				$("#component-footer select").html("<option>"+datarow+"</option><option>10</option><option>15</option>");
			}
			if( datarow == 10 ){
				$("#component-footer select").html("<option>"+datarow+"</option><option>5</option><option>15</option>");
			}
			if( datarow == 15 ){
				$("#component-footer select").html("<option>"+datarow+"</option><option>5</option><option>10</option>");
			}
		},
	})
}