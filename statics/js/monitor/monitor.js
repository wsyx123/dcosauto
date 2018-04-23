function set_agent_status(agent,status,agent_info){
	$.ajax({
		type: 'PATCH',
		url: 'http://192.168.10.1:9000/master/api/hosts/'+agent+'/',
		data:{"name": agent,"status": status,},
		success: function(data,respons_status,xhr){
			if(xhr.status == 200){
				if(status == 'UP'){
					agent_status = 'enabled';
				}else{
					agent_status = 'disabled';
				}
				var host = agent_info.split(':')[0];
				var port = agent_info.split(':')[1];
				$.ajax({
					type: 'POST',
					url: 'editHost/'+agent,
					data:{"host":host,"port":port,"status":agent_status,},
				})
			}
		}
	})
}

function set_problem_status(id,status){
	$.ajax({
		type: 'PATCH',
		url: 'http://192.168.10.1:9000/master/api/problems/'+id+'/',
		data:{"id": id,"status": status,},
	})
	
}

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
		var name = $(this).siblings().eq(0).html();
		var agent_info = $(this).siblings().eq(1).html();
		var status = $(this).children().html();
		if( status == '已启用' ){
			var result = confirm('停用主机?');
			if( result == true ){
				set_agent_status(name,'DOWN',agent_info);
				$(this).html('<a style="cursor:pointer;color:red;">停用的</a>');
			}
		}
		if( status == '停用的' ){
			var result = confirm('启用主机?');
			if( result == true ){
				set_agent_status(name,'UP',agent_info);
				$(this).html('<a style="cursor:pointer;color:green;">已启用</a>');
			}
		}
		
	})
	
	$(".notify-status").bind('click',function(){
		var id = $(this).siblings().eq(0).html();
		var status = $(this).children().html();
		if( status == '已确认' ){
			var result = confirm('取消确认?');
			if( result == true ){
				set_problem_status(id,'UNCONFIRMED');
				$(this).html('<a class="notify-status-grey">未确认</a>');
			}
		}
		if( status == '未确认' ){
			var result = confirm('问题已确认?');
			if( result == true ){
				set_problem_status(id,'CONFIRMED');
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

function edit_agent(obj){
	var name = $(obj).parent().siblings().eq(0).html();
	window.location.href="/monitor/configure/editHost/"+name;
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

function get_template_id(name){
	$.ajax({
		type: 'GET',
		url: '/master/api/templates/'+name+'/',
		success: function(data){
			return data.id;
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

function edit_template(obj){
	var name = $(obj).parent().siblings().eq(0).html();
	window.location.href="/monitor/configure/editTemplate/"+name;
}

function server_api_edit_start(obj){
	var current = $("#server-api-show").html();
	$("input[name='server-api']").val(current);
}

function es_api_edit_start(obj){
	var current = $("#es-api-show").html();
	$("input[name='es-api']").val(current);
}

function server_api_edit_save(){
	var edit = $("input[name='server-api']").val();
	$("#server-api-show").html(edit);
}

function es_api_edit_save(){
	var edit = $("input[name='es-api']").val();
	$("#es-api-show").html(edit);
	$.ajax({
		type: 'PUT',
		url: 'http://192.168.10.1:9000/master/api/configs/ES%20API/',
		data:{"name": "ES API","value": edit,},
	})
}

function tdclick(tdobject){  
    var td=$(tdobject);
    var host = $(tdobject).siblings().eq(0).text();
    td.attr("onclick", "");  
    //1,取出当前td中的文本内容保存起来  
    var text=td.text();  
    //2,清空td里面的内容  
    td.html(""); //也可以用td.empty();  
    //3，建立一个文本框，也就是input的元素节点  
    var input=$("<input>");
    //4，设置文本框的值是保存起来的文本内容  
    input.attr("value",text);  
    input.bind("blur",function(){  
        var inputnode=$(this);  
        var inputtext=inputnode.val();  
        var tdNode=inputnode.parent(); 
        tdNode.html(inputtext);  
        //tdNode.click(tdclick);
        edit_agent(host,inputtext);
        td.attr("onclick", "tdclick(this)"); 
    });  
    input.keyup(function(event){  
        var myEvent =event||window.event;  
        var kcode=myEvent.keyCode;  
        if(kcode==13){  
            var inputnode=$(this);  
            var inputtext=inputnode.val();  
            var tdNode=inputnode.parent();  
            tdNode.html(inputtext);  
            tdNode.click(tdclick);  
        }  
    });  
  
    //5，将文本框加入到td中  
    td.append(input);  
    var t =input.val();  
    input.val("").focus().val(t);  
    input.focus(); 
  
    //6,清除点击事件  
    td.unbind("click");  
}

function del_item(obj){
	var name = $(obj).parent().siblings().eq(0).html();
	$.ajax({
		type: 'POST',
		url: 'delItem/',
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

function edit_item(obj){
	var name = $(obj).parent().siblings().eq(0).html();
	window.location.href="/monitor/configure/editItem/"+name;
}

function del_policy(obj){
	var name = $(obj).parent().siblings().eq(0).html();
	$.ajax({
		type: 'POST',
		url: 'delPolicy/',
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

function edit_policy(obj){
	var name = $(obj).parent().siblings().eq(0).html();
	window.location.href="/monitor/configure/editPolicy/"+name;
}

function str_convert_int(list){
	var temp_list = new Array();
	for(var i=0;i<list.length;i++){
		temp_list.push(parseInt(list[i]));
	}
	return temp_list;
}

function add_notify(){
	//data = $("#monitor-notify").serialize();
	var name = $("input[name='name']").val();
	var type = $("select[name='type']").val();
	var account = ($("select[name='account']").val()).join(",");
	var hosts = $("select[name='hosts']").val();
	var hosts = str_convert_int(hosts);
	var json = {"name":name,"type":type,"account":account,"hosts":hosts}
	$.ajax({
		beforeSend: function(request) {
            request.setRequestHeader("Content-Type", "application/json");
        },
		type: 'POST',
		url: 'http://192.168.10.1:9000/master/api/notifys/',
		data:JSON.stringify(json),
		success:function(){
			window.location.href="/monitor/notify/";
		}
	})
}

function edit_notify(obj){
	var name = $(obj).parent().siblings().eq(0).html();
	window.location.href="/monitor/configure/editHost/"+name;
}

function del_notify(obj){
	var name = $(obj).parent().siblings().eq(0).html();
	$.ajax({
		type: 'DELETE',
		url: 'http://192.168.10.1:9000/master/api/notifys/'+name,
		complete: function(data){
			//console.log(data.status,data.statusText);
			if(data.status == 204){
				$(obj).parent().parent().remove();
				$("#delete-name").html(name);
				$("#mySuccessAlert").css('display','block');
			}else{
				$("#delete-name").html(name);
				$("#delete-failure").html(data.statusText);
				$("#myFailureAlert").css('display','block');
			}
		}
	})
}