$(document).ready(function(){
	templatejson = {};
	$("#cpu").children().attr('checked','checked');
	$("input[name='item']").attr('disabled',true);
	$("#cpu").children().attr('disabled',false);
//	$(".item-selected-delete").bind('click',function(){
//		$(this).parent().remove();
//	})
	
})

function selected_detail_remove(obj){
	var name = $(obj).parent().siblings().eq("0").html();
	$.each(templatejson,function(key,value){
		if(name == key){
			delete templatejson[name];
			console.log(templatejson);
		}else{
			if( $.inArray(name,templatejson[key]) == 1 ){
				(templatejson[key]).splice($.inArray(name,templatejson[key]));
			}
		}
		});
	$(obj).parent().parent().remove();
	
	
}

function item_select_add(){
	var items = $(".item-selected-value");
	for(var i=0;i<items.length;i++){
		$("#input-table-selected").append('<tr class="selected-detail">\
							<td>cpu</td>\
							<td>cpu.use,cpu.iowait</td>\
							<td><a onclick="selected_detail_remove(this)">取消选择</a></td>\
						</tr>')
	}
	$("#multiselect-list").remove();
	
}

function select_all(){
	$(".monitor_item input[type='checkbox']").prop('checked',true);
}

function unselect_all(){
	$(".monitor_item input[type='checkbox']").prop("checked",false);
}

function get_items(){
	var items = new Array();
	($(".monitor_item input[type='checkbox']:checked")).each(function(){ 
		var key = $(this).parent().next().html();
		items.push(key);
		templatejson['items']=items;
		$("#input-table-selected").append('<tr class="selected-detail">\
				<td>'+key+'</td>\
				<td><a onclick="selected_detail_remove(this)">取消选择</a></td>\
			</tr>')
	})
}

function save_template(){
	var name = $("input[name='name']").val();
	var interval = $("select[name='interval']").find("option:selected").html();
	templatejson['name']=name
	templatejson['interval'] = interval
	$.ajax({
		type: 'POST',
		data: {'template':JSON.stringify(templatejson),},
		success: function(){
			window.location.href="/monitor/configure/";
		}
	})
}


function policy_select_all(){
	$(".policy_item input[type='checkbox']").prop('checked',true);
}

function policy_unselect_all(){
	$(".policy_item input[type='checkbox']").prop("checked",false);
}

function policy_get_items(){
	var policys = new Array();
	($(".policy_item input[type='checkbox']:checked")).each(function(){
		var policyobj = $(this).parent().parent().find("td");
		var name = $(policyobj).eq(1).html();
		var warning_threshold = $(policyobj).eq(2).html();
		var danger_threshold = $(policyobj).eq(3).html();
		var promote = $(policyobj).eq(4).html();
		policys.push(name);
		$("#policy-select-table").append('<tr class="selected-detail">\
				<td>'+name+'</td>\
				<td><a onclick="selected_detail_remove(this)">取消选择</a></td>\
			</tr>')
	})
	templatejson['policys']=policys;
}

function disable_item(obj){
	var item = $(obj).find('option:checked').html();
	$("input[name='item']").attr('disabled',true);
	//$("input[name='item']").prop('checked','checked');
	$("#"+item).children().attr('disabled',false);
	$("#"+item).children().attr('checked','checked');
}

function save_item(){
	var name = $("input[name='name']").val();
	var item = $("select[name='type']").val();
	var value = $("select[name="+item+"]").val();
	var itemjson = {"name":"","type":"","value":""};
	itemjson["name"]=name;
	itemjson["type"]=item;
	itemjson["value"]=value.join(",");
	$.ajax({
		type: 'POST',
		data: {'item':JSON.stringify(itemjson),},
		success: function(){
			window.location.href="/monitor/configure/";
		}
	})
	
}