$(document).ready(function(){
	$("#image-menu div").bind("click",function(){
		var displayobj = $(".image-detail");
		$(displayobj).css('display','none');
		$("#image-menu div").removeAttr("style");
		$("#image-menu div").removeClass("add-underline");
		$(this).addClass("add-underline");
		$(displayobj[$(this).index()]).css('display','block');
	});
	$(".add_var").bind("click",add_var);
	$(".add_task").bind("click",add_task);
	$(".add_handler").bind("click",add_handler);
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
				window.location.href='/asset/host/';
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
	address = $(obj).parent().siblings().eq(1).html();
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

function terminal_connect(obj){
	var addr = $(obj).parent().siblings().eq(1).html();
	window.location.href='/asset/host/'+addr;
}

function collection_finish(){
	window.location.href='/asset';
}

function choice_execute_model(obj){
	var model = $(obj).val();
	if(model == 'ansible'){
		$(".ansible-playbook-input").css("display",'block');
		$(".shell-input").css("display",'none');
		$("#execute-result-area").css("height","190px")
	}else{
		$(".ansible-playbook-input").css("display",'none');
		$(".shell-input").css("display",'block');
		$("#execute-result-area").css("height","255px")
	}
}

function add_var(){
	$(this).next().children().append('<tr>\
	<td class="name"><input name="var_name"></td>\
	<td><input name="var_value"></td>\
	<td onclick="del_element(this)"><i class="glyphicon glyphicon-minus"></i></td>\
</tr>');
}
function del_element(obj){
	$(obj).parent().remove();
}

function add_task(){
	$(this).next().children().append('<tr>\
			<td class="name"><input name="task_name"></td>\
    		<td class="model"><input name="task_module"></td>\
    		<td class="args"><input name="task_arg"></td>\
    		<td><input name="task_notify"></td>\
			<td onclick="del_element(this)"><i class="glyphicon glyphicon-minus"></i></td>\
    	</tr>');
}

function add_handler(){
	$(this).next().children().append('<tr>\
			<td class="name"><input name="handler_name"></td>\
    		<td class="model"><input name="handler_module"></td>\
    		<td class="args"><input name="handler_arg"></td>\
			<td onclick="del_element(this)"><i class="glyphicon glyphicon-minus"></i></td>\
    	</tr>');
}

function execute_command(){
	var execute_data = {};
	var model = $(".execute-model select").find("option:selected").val();
	if(model == 'shell'){
		execute_data['model'] = 'shell';
		execute_data['command'] = $("textarea[name='shell_command']").val();
	}else{
		/*  传递给后台数据格式
		{
			'model':'ansible',
			'vars':{'http_in':80,'http_out':81},
			'tasks':[
			         {'name':'task1','module':'shell','arg':'df','notify':'handler1'},
			         {'name':'task2','module':'shell','arg':'ls','notify':'handler2},
			         ],
			'handler':[
			           {'name':'handler1','module':'shell','arg':'df'},
			           {'name':'handler2','module':'shell','arg':'df'},
			           ]
			} */
		execute_data['model'] = 'ansible';
		var var_name_obj=$("input[name='var_name']");
		var var_value_obj=$("input[name='var_value']");
		
		var task_name_obj=$("input[name='task_name']");
		var task_module_obj=$("input[name='task_module']");
		var task_arg_obj=$("input[name='task_arg']");
		var task_notify_obj=$("input[name='task_notify']");
		
		var handler_name_obj=$("input[name='handler_name']");
		var handler_module_obj=$("input[name='handler_module']");
		var handler_arg_obj=$("input[name='handler_arg']");
		
		execute_data['vars']=foreach_var(var_name_obj,var_value_obj);
		execute_data['tasks']=foreach_task(task_name_obj,task_module_obj,task_arg_obj,task_notify_obj)
		execute_data['handlers']=foreach_handler(task_name_obj,task_module_obj,task_arg_obj)
	}
	console.log(execute_data);
	$.ajax({
		type: 'POST',
		data: {'execute_data':JSON.stringify(execute_data),},
	})
}

function foreach_var(name_obj,value_obj){
	var var_dict = {};
	for(var i=0;i<name_obj.length;i++){
		var_dict[$(name_obj[i]).val()]=$(value_obj[i]).val();
	}
	return var_dict;
}

function foreach_task(name_obj,module_obj,arg_obj,notify_obj){
	var task_list = [];
	for(var i=0;i<name_obj.length;i++){
		var task_dict = {};
		task_dict['name'] = $(name_obj[i]).val();
		task_dict['module'] = $(module_obj[i]).val();
		task_dict['arg'] = $(arg_obj[i]).val();
		task_dict['notify'] = $(notify_obj[i]).val();
		task_list.push(task_dict);
	}
	return task_list;
}

function foreach_handler(name_obj,module_obj,arg_obj){
	var handler_list = [];
	for(var i=0;i<name_obj.length;i++){
		var handler_dict = {};
		handler_dict['name'] = $(name_obj[i]).val();
		handler_dict['module'] = $(module_obj[i]).val();
		handler_dict['arg'] = $(arg_obj[i]).val();
		handler_list.push(handler_dict);
	}
	return handler_list;
}