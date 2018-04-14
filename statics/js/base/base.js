$(document).ready(function(){
var currentURL = document.location.pathname;
var currentURLlen = currentURL.split('/');  //判断  url 路径长度 ，如果>=4 就是二级菜单，需要设置collapse,设置 active
var myNav = $("#col-md-2 .nav li > a");
if(currentURLlen.length >=4){
	var new_currentURL = '/'+currentURLlen[1]+'/'+currentURLlen[2]+'/' //这里考虑3级菜单的情况,如/zabbix/configure/addHost/
	                                                                   //,这种就匹配不到二级href，需要截取
	var secondmenu = currentURLlen[1]; // 每个二级菜单都有一个id  这个id与currentURLlen[1]相等
	$("#"+secondmenu).collapse('show');
	var secondNav = $("#"+secondmenu).children().find("a");
	setliactive(new_currentURL,secondNav);
	$("#"+secondmenu).prev().children("span").toggleClass("glyphicon-chevron-down");
}else{
	setliactive(currentURL,myNav);
}

$("#col-md-2 .nav-header").bind("click",function(){
	$(this).children("span").toggleClass("glyphicon-chevron-down");
});
get_notify_amount();
setInterval(get_notify_amount,120000);

});

function setliactive(currentURL,myNav){ // myNav 为二级菜单下的所有  a 对象
	for(i=0;i<myNav.length;i++){
		var links = myNav[i].getAttribute("href"); // 获取一个 a 实例的 href属性
		if(currentURL == links){  // 如果 当前页面path 等于 某个 a 实例的href属性 就设置  active
		    $(myNav[i]).parent().addClass("active");
		   }
		if(currentURL == '/'){
			$(myNav[0]).parent().addClass("active");
		}
	};
}

$(function (){
    $("[data-toggle='popover']").popover(
    {
    //	trigger:'click', //触发方式
        html: true, // 为true的话，data-content里就能放html代码了
     //   content: function() {
    //        return $('#component-footer').html();
     //     }
    }		
    );
});

$(function(){
	$(".close").click(function(){
		$(this).parent().css('display','none');
	});
});

function get_notify_amount(){
	$.ajax({
		type: 'GET',
		url: '/master/api/problems/?search=UNCONFIRMED',
		success: function(data){
			$(notify_amount).html(data.length);
		}
	})
}