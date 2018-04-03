$(document).ready(function(){
	var cpuChart = echarts.init(document.getElementById('cpu'));
	var memChart = echarts.init(document.getElementById('mem'));
	var diskChart = echarts.init(document.getElementById('disk'));
	var netChart = echarts.init(document.getElementById('net'));
	var cpuoption = {
		    title: {
		        text: 'cpu 利用率 (10m)',
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
		        data: ['21:01', '21:02', '21:03', '21:04', '21:05', '21:06', '21:07', '21:08', '21:09', '21:10']
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
		            data: [10.1,6.5,38.6,66.8,9.3,29.3,49.5,19.3,39.3,75.7],
		        },
		        {
		            name:'iowait',
		            type:'line',
		            color: 'red',
		            itemStyle: {normal: {
		    			label : {show:true,position:'top',formatter:'{c}'}
		    		}},
		            smooth: true,
		            data: ['0.0','0.1','0.0','0.0','0.0','0.2','0.0','0.0','0.0','0.4'],
		        }
		    ]
		}; 
	
		var memoption = {
		    title: {
		        text: '可用内存 (10m)',
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
		        data: ['21:01', '21:02', '21:03', '21:04', '21:05', '21:06', '21:07', '21:08', '21:09', '21:10']
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
	            data: [6.1,6.5,6.7,6.8,6.3,6.3,6.5,6.3,6.9,7.0],
		        },
		        {
	            name:'总量',
	            type:'line',
	            areaStyle: {},
	            itemStyle: {normal: {
	    			label : {show:true,position:'top',formatter:'{c}'}
	    		}},
	            smooth: true,
	            data: [8,8,8,8,8,8,8,8,8,8],
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
			        data: ['已用', '可用'],
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
			        data: ['/','/home','/data','/boot','/run'],
			    },
			    series: [
			        {
			            name: '已用',
			            type: 'bar',
			            color: 'red',
			            itemStyle: {normal: {
			    			label : {show:true,position:'right',formatter:'{c} GB'}
			    		}},
			            data: [18, 3, 29, 1, 3]
			        },
			        {
			            name: '可用',
			            color: 'green',
			            type: 'bar',
			            itemStyle: {normal: {
			    			label : {show:true,position:'right',formatter:'{c} GB'}
			    		}},
			            data: [19, 23, 71, 9, 7]
			        }
			    ]
			};
		
		
		netoption = {
			    title: {
			        text: 'eth0网络流量'
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
			            data: ['21:01', '21:02', '21:03', '21:04', '21:05', '21:06', '21:07', '21:08', '21:09', '21:10']
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
			            data:[120, 132, 101, 134, 134, 134, 134,134,112,154]
			        },
			        {
			            name:'接收',
			            type:'line',
			            areaStyle: {normal: {}},
			            data:[100, 92, 81, 34, 94, 56, 78,84,112,100]
			        },
			        {
			            name:'丢弃',
			            type:'line',
			            areaStyle: {normal: {}},
			            data:[10, 9, 6, 0, 1, 4, 3,0,0,0]
			        },
			    ]
			};
        
       cpuChart.setOption(cpuoption);  
       memChart.setOption(memoption);
       diskChart.setOption(diskoption);
       netChart.setOption(netoption);
      
	
})







