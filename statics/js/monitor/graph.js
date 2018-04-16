$(document).ready(function(){
	cpuChart = echarts.init(document.getElementById('cpu'));
	memChart = echarts.init(document.getElementById('mem'));
	diskChart = echarts.init(document.getElementById('disk'));
	netChart = echarts.init(document.getElementById('net'));
	var cpuoption = {
		    title: {
		        text: 'cpu 利用率 ',
		    },
		    legend:{
		    	data:['use','iowait'],
		    
		    },
		    tooltip: {
		        trigger: 'axis',
		        axisPointer: {
		            type: 'cross'
		        }
		    },
		    xAxis:  {
		        type: 'category',
		        boundaryGap: false,
		        data: []
		    },
		    yAxis: {
		        type: 'value',
		        axisLabel:{formatter:'{value} %'}
		        
		    },
		    visualMap: {
		        show: false,
		        pieces: [{
                 gte:0,
                 lte:30,
                 color:'green'
                 },{
		         gt:30,
		         lte:60,
		         color:'yellow'
		         },{
		         gt:60,
		         color:'red'
		         }]
		    },
		    series: [
		        {
		            name:'use',
		            type:'line',
		            itemStyle: {normal: {
		    			label : {show:true,position:'top',formatter:'{c}'}
		    		}},
		            smooth: true,
		            data: [],
		        },
		        {
		            name:'iowait',
		            type:'line',
		            color: 'red',
		            itemStyle: {normal: {
		    			label : {show:true,position:'top',formatter:'{c}'}
		    		}},
		            smooth: true,
		            data: [],
		        }
		    ]
		}; 
	
		var memoption = {
		    title: {
		        text: '可用内存 ',
		    },
		    legend:{
		    	data:['可用','总量'],
		    },
		    tooltip: {
		        trigger: 'axis',
		        axisPointer: {
		            type: 'cross'
		        }
		    },
		    xAxis:  {
		        type: 'category',
		        boundaryGap: false,
		        data: []
		    },
		    yAxis: {
		        type: 'value',
		        axisLabel:{formatter:'{value} GB'}
		        
		    },
		    visualMap: {
		        show: false,
		        pieces: [{
                 gte:0,
                 lte:30,
                 color:'green'
                 },{
		         gt:30,
		         lte:60,
		         color:'yellow'
		         },{
		         gt:60,
		         color:'red'
		         }]
		    },
		    series: [
		        {
	            name:'可用',
	            type:'line',
	            color: 'green',
	            areaStyle: {},
	            itemStyle: {normal: {
	    			label : {show:true,position:'top',formatter:'{c}'}
	    		}},
	            smooth: true,
	            data: [],
		        },
		        {
	            name:'总量',
	            type:'line',
	            areaStyle: {},
	            itemStyle: {normal: {
	    			label : {show:true,position:'top',formatter:'{c}'}
	    		}},
	            smooth: true,
	            data: [],
		        },
		    ]
		}; 
		
		diskoption = {
			    title: {
			        text: '分区情况',
			    },
			    tooltip: {
			        trigger: 'axis',
			        axisPointer: {
			            type: 'shadow'
			        }
			    },
			    legend: {
			        data: ['已用', '总量'],
			    },
			    grid: {
			        left: '3%',
			        right: '4%',
			        bottom: '3%',
			        containLabel: true
			    },
			    xAxis: {
			        type: 'value',
			        boundaryGap: [0, 0.01],
			        axisLabel:{formatter:'{value} GB'}
			    },
			    yAxis: {
			        type: 'category',
			        data: [],
			    },
			    series: [
			        {
			            name: '已用',
			            type: 'bar',
			            color: 'red',
			            itemStyle: {normal: {
			    			label : {show:true,position:'right',formatter:'{c} GB'}
			    		}},
			            data: []
			        },
			        {
			            name: '总量',
			            color: 'green',
			            type: 'bar',
			            itemStyle: {normal: {
			    			label : {show:true,position:'right',formatter:'{c} GB'}
			    		}},
			            data: []
			        }
			    ]
			};
		
		
		netoption = {
			    title: {
			        text: '网络流量'
			    },
			    tooltip : {
			        trigger: 'axis',
			        axisPointer: {
			            type: 'cross',
			            label: {
			                backgroundColor: '#6a7985'
			            }
			        }
			    },
			    legend: {
			        data:['发送','接收','丢弃']
			    },
			    grid: {
			        left: '3%',
			        right: '4%',
			        bottom: '3%',
			        containLabel: true
			    },
			    xAxis : [
			        {
			            type : 'category',
			            boundaryGap : false,
			            data: []
			        }
			    ],
			    yAxis : [
			        {
			            type : 'value',
			            axisLabel:{formatter:'{value} Kib'}
			        }
			    ],
			    series : [
			        {
			            name:'发送',
			            type:'line',
			            areaStyle: {normal: {}},
			            data:[]
			        },
			        {
			            name:'接收',
			            type:'line',
			            areaStyle: {normal: {}},
			            data:[]
			        },
			        {
			            name:'丢弃',
			            type:'line',
			            areaStyle: {normal: {}},
			            data:[]
			        },
			    ]
			};
        
       cpuChart.setOption(cpuoption);  
       memChart.setOption(memoption);
       diskChart.setOption(diskoption);
       netChart.setOption(netoption);
       select_time();
      
	
})

function select_host(obj){
	host = $(obj).find("option:selected").html();
	console.log(host);
	$.ajax({
		type: 'POST',
		data: {'host':host},
		success: function(data){
			console.log(data);
		}
	})
}

function set_cpu_option(dataobj){
	cpuChart.setOption({
		xAxis:  {
	        type: 'category',
	        boundaryGap: false,
	        data: dataobj.cpu.timestamp,
	    },
	    series: [
			        {
			            name:'use',
			            type:'line',
			            itemStyle: {normal: {
			    			label : {show:true,position:'top',formatter:'{c}'}
			    		}},
			            smooth: true,
			            data: dataobj.cpu.usage,
			        },
			        {
			            name:'iowait',
			            type:'line',
			            color: 'red',
			            itemStyle: {normal: {
			    			label : {show:true,position:'top',formatter:'{c}'}
			    		}},
			            smooth: true,
			            data: dataobj.cpu.iowait,
			        }
			    ]
	});
}

function set_memory_option(dataobj){
	memChart.setOption({
		xAxis:  {
	        type: 'category',
	        boundaryGap: false,
	        data: dataobj.memory.timestamp,
	    },
	    series: [
			        {
		            name:'可用',
		            type:'line',
		            color: 'green',
		            areaStyle: {},
		            itemStyle: {normal: {
		    			label : {show:true,position:'top',formatter:'{c}'}
		    		}},
		            smooth: true,
		            data: dataobj.memory.free,
			        },
			        {
		            name:'总量',
		            type:'line',
		            areaStyle: {},
		            itemStyle: {normal: {
		    			label : {show:true,position:'top',formatter:'{c}'}
		    		}},
		            smooth: true,
		            data: dataobj.memory.total,
			        },
			    ]
	});
}

function set_disk_option(dataobj){
	diskChart.setOption({
		yAxis: {
	        type: 'category',
	        data: dataobj.disk.partition,
	    },
	    series: [
			        {
			            name: '已用',
			            type: 'bar',
			            color: 'red',
			            itemStyle: {normal: {
			    			label : {show:true,position:'right',formatter:'{c} GB'}
			    		}},
			            data: dataobj.disk.used,
			        },
			        {
			            name: '总量',
			            color: 'green',
			            type: 'bar',
			            itemStyle: {normal: {
			    			label : {show:true,position:'right',formatter:'{c} GB'}
			    		}},
			            data: dataobj.disk.total,
			        }
			    ]
	});
}

function set_network_option(dataobj){
	netChart.setOption({
		title: {
	        text: dataobj.network.device+'网络流量'
	    },
		xAxis : [
			        {
			            type : 'category',
			            boundaryGap : false,
			            data: dataobj.network.timestamp,
			        }
			    ],
	    series : [
			        {
			            name:'发送',
			            type:'line',
			            areaStyle: {normal: {}},
			            data: dataobj.network.transmit,
			        },
			        {
			            name:'接收',
			            type:'line',
			            areaStyle: {normal: {}},
			            data: dataobj.network.receive,
			        },
			        {
			            name:'丢弃',
			            type:'line',
			            areaStyle: {normal: {}},
			            data: dataobj.network.drop,
			        },
			    ]

	});
}

function select_time(){
	var data = {};
	var host = $("select[name='host']").find("option:selected").val();
	var graph_item = $("select[name='graph-item']").find("option:selected").val();
	var time_value = $("select[name='time-range']").find("option:selected").val();
	data["host"] = host;
	data["graph_item"] = graph_item;
	data["time_value"] = time_value;
	$.ajax({
		type: 'POST',
		data: {"data": JSON.stringify(data)},
		success: function(data){
			dataobj = eval('('+data+')');
			set_cpu_option(dataobj);
			set_memory_option(dataobj);
			set_disk_option(dataobj);
			set_network_option(dataobj);
		}
	})
}





