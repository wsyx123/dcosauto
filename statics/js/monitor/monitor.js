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

function get_template_id(name){
	$.ajax({
		type: 'GET',
		url: '/master/api/templates/'+name+'/',
		success: function(data){
			return data.id;
		}
	})
}

function edit_agent(name,template_name){
	template_id = get_template_id(template_name);
	$.ajax({
		type: 'GET',
		url: '/master/api/hosts/'+name+'/',
		data: {'template':template_id,'name':name},
		success: function(data){
			//var dataobj = eval('('+data+')');
			console.log(data.template);
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