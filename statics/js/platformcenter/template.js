function add_template(){
	$.ajax({
		type:'POST',
		data:$("#template-form").serialize(),
		success:function(){
			window.location.href='/platform/template/';
		}
	})
}

function edit_template(){
	var name = $(".templateradio:checked").parent().next().html();
	if(name == undefined){
		alert('请选择要编辑的模版!!!');
	}else{
		window.location.href="/platform/template/editTemplate/"+name;
	}
	
	
}

function delete_component_ask(obj){
	var template_name_list = new Array();
	var templateobj = $(".templateradio:checked").parent().next();
	for(i=0;i<templateobj.length;i++){
		template_name_list.push($(templateobj[i]).html()+'\n');
	}
	$("#delete-name").html(template_name_list);
}

function del_template(){
	var template_name_list = new Array();
	var templateobj = $(".templateradio:checked").parent().next();
	for(i=0;i<templateobj.length;i++){
		template_name_list.push($(templateobj[i]).html());
	}
	$.ajax({
		type: 'POST',
		url: '/platform/template/delTemplate/',
		data: {'template_name_list':JSON.stringify(template_name_list)},
		success:function(data){
			dataobj = eval('('+data+')');
			for(var i=0;i<template_name_list.length;i++){
				if(dataobj[template_name_list[i]]=='success'){
					for(j=0;j<templateobj.length;j++){
						if($(templateobj[j]).html()==template_name_list[i]){
							$(templateobj[j]).parent().remove();
						}
					}
				}else{
					console.log('failure');
				}
			}
		}
	})
}

function controller_all(obj){
	if (obj.tag==1)
    {
        obj.checked=false;
        obj.tag=0;
        $(".templateradio").prop('checked',false);
    }
    else
    {
        obj.checked=true;
        obj.tag=1;
        $(".templateradio").prop('checked','checked');
    }
}

function controller(obj){
	if (obj.tag==1)
    {
        obj.checked=false;
        obj.tag=0;
    }
    else
    {
        obj.checked=true;
        obj.tag=1
    }
}

function change_data_row(obj){
	var datarow = $(obj).find("option:selected").val();
	$.ajax({
		type:'GET',
		data:{'datarow':datarow},
		success:function(data){
			document.body.innerHTML = data;
			$("#component-show").append('<script src="/static/js/base/base.js"></script>');
			if( datarow == 5 ){
				$("#template-footer select").html("<option>"+datarow+"</option><option>10</option><option>15</option>");
			}
			if( datarow == 10 ){
				$("#template-footer select").html("<option>"+datarow+"</option><option>5</option><option>15</option>");
			}
			if( datarow == 15 ){
				$("#template-footer select").html("<option>"+datarow+"</option><option>5</option><option>10</option>");
			}
		},
	});
}


