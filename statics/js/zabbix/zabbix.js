$(document).ready(function(){
	$("#zabbix-menu div").bind("click",function(){
		var displayobj = $(".zabbix-detail");
		$(displayobj).css('display','none');
		$("#zabbix-menu div").removeAttr("style");
		$("#zabbix-menu div").removeClass("add-underline");
		$(this).addClass("add-underline");
		$(displayobj[$(this).index()]).css('display','block');
	})
	
})

function add_host(){
	$.ajax({
		type:'GET',
		url:'addHost/',
	})
}

function save_repository(){
	$.ajax({
		type:'POST',
		data:$("#zabbix-form").serialize(),
		success:function(){
			window.location.href="/zabbix/";
		}
	})
}




