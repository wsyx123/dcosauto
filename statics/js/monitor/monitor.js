$(document).ready(function(){
	$("#zabbix-menu div").bind("click",function(){
		var displayobj = $(".zabbix-detail");
		$(displayobj).css('display','none');
		$("#zabbix-menu div").removeAttr("style");
		$("#zabbix-menu div").removeClass("add-underline");
		$(this).addClass("add-underline");
		$(displayobj[$(this).index()]).css('display','block');
	})
	
	$(".monitor-status").bind('click',function(){
		var status = $(this).children().html();
		if( status == '已启用' ){
			var result = confirm('停用主机?');
			if( result == true ){
				$(this).html('<a style="cursor:pointer;color:red;">停用的</a>');
			}
		}
		if( status == '停用的' ){
			var result = confirm('启用主机?');
			if( result == true ){
				$(this).html('<a style="cursor:pointer;color:green;">已启用</a>');
			}
		}
		
	})
	
	$(".notify-status").bind('click',function(){
		var status = $(this).children().html();
		if( status == '已确认' ){
			var result = confirm('取消确认?');
			if( result == true ){
				$(this).html('<a class="notify-status-grey">未确认</a>');
			}
		}
		if( status == '未确认' ){
			var result = confirm('问题已确认?');
			if( result == true ){
				$(this).html('<a class="notify-status-green">已确认</a>');
			}
		}
		
	})
})

function add_agent(){
	var hostinfo = {}
	hostinfo['name'] = $("input[name='name']").val();
	hostinfo['address'] = $("input[name='address']").val();
	hostinfo['port'] = $("input[name='port']").val();
	hostinfo['template'] = $("select[name='template']").val();
	hostinfo['status'] = $("input[name='status']").is(':checked');
	$.ajax({
		type: 'POST',
		data: {'host':JSON.stringify(hostinfo),},
		success: function(){
			window.location.href="/monitor/configure/";
		}
	})
}

function delete_agent(obj){
	var name = $(obj).parent().siblings().eq(0).html();
	$.ajax({
		type: 'POST',
		url: 'delHost/',
		data: {'name':name},
		success: function(data){
			var dataobj = eval('('+data+')');
			if(dataobj.status){
				$(obj).parent().parent().remove();
				$("#mySuccessAlert").css('display','block');
			}else{
				$("#myFailureAlert").css('display','block');
				$("#delete-failure").html(dataobj.msg);
			}
		}
	})
}

function del_template(obj){
	var name = $(obj).parent().siblings().eq(0).html();
	$.ajax({
		type: 'POST',
		url: 'delTemplate/',
		data: {'name':name},
		success: function(data){
			var dataobj = eval('('+data+')');
			if(dataobj.status){
				$(obj).parent().parent().remove();
				$("#mySuccessAlert").css('display','block');
			}else{
				$("#myFailureAlert").css('display','block');
				$("#delete-failure").html(dataobj.msg);
			}
		}
	})
}

function server_api_edit_start(){
	var current = $("#server-api-show").html();
	$("input[name='server-api']").val(current);
}
function server_api_edit_save(){
	var edit = $("input[name='server-api']").val();
	$("#server-api-show").html(edit);
}
