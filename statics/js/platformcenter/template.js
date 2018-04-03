function add_template(){
	$.ajax({
		type:'POST',
		data:$("#template-form").serialize(),
		success:function(){
			window.location.href='/platform/template/';
		}
	})
	
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


