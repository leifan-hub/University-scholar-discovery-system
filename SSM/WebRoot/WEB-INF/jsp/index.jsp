<%@ page language="java" import="java.util.*" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE>
<html>
  <head>
    <base href="<%=basePath%>">
    <title>zero</title>
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!-- 新 Bootstrap 核心 CSS 文件 -->
	<link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
	<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
	<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
	<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
	<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<script src="https://cdn.staticfile.org/echarts/4.3.0/echarts.min.js"></script>
	<style type="text/css">
	*{
 		padding:0px;
 		margin:0px;
 		border:0px;
 	}
	body{	
		background:url(images/bg1.jpg);
		background-size:cover;	
	}
	.b{
		z-index:10;
		position: fixed;
		width:100%;
		text-align:center;
		background:url(images/bg4.png) 0 0 no-repeat #B0E0E6;
		background-size:cover;
	}
	.c{
		z-index:8;
		text-align:center;
		width:100%;
		background:url(images/bggif1.gif) 0 0 no-repeat #F8F8FF;
		background-size:cover;	
	}
	#expertDescription {
		display: inline-block;
    	line-height:30px;
    	width:1000px;
    	text-align:center;
    	float:top;
	}
	.expertPicture {
		z-index:0;
		display: inline-block;
		vertical-align: middle;
		position:relative;
		float:top;
	}
	.nav{
		z-index:10;
		position: fixed;
	   	height:40px;
	   	width:100%;
	   	margin-top:20px;
	}
	.nav ul{
	   list-style:none;
	   height:45.15px;
	   border-bottom:5px solid #FF6600;
	}
	.nav li{
	   float:left;
	   margin-top:0px;
	}
	.nav li a{
	    background-color:#EEEEEE;
	    text-decoration:none;
	    color:#000000;
	    display:block;
	    width:120px;
	    height:40px;
	    line-height:40px;
	    text-align:center;
	    margin-left:1px;
	    border-top-left-radius:15px;
    	border-top-right-radius:15px;
	}
	.nav li a:hover,.nav li a.on{
	    background-color:#FF6600;
	    color:#FFFFFF;
	    /*伸缩变换设置高度变化*/
	    height:40px;
	    /*和使用负值向反方向移动*/
	    margin-top:0px;
	    line-height:40px;
	}
 	input{
	    outline-style: none ;
	    border: 1px solid #ccc; 
	    border-radius: 3px;
	}
	.loading{
            width: 100%;
            height: 4px;
            border-radius: 2px;
            margin: 0 auto;
            position: relative;
            background: lightgreen;
            -webkit-animation: changeBgColor 6.4s ease-in infinite alternate;
        }
        .loading span{
            display: inline-block;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: lightgreen;
            position: absolute;
            margin-top: -7px;
            margin-left:10%;
            -webkit-animation: changePosition 6.4s ease-in infinite alternate;
        }
        @-webkit-keyframes changeBgColor{
            0%{
                background: lightgreen;
            }
            100%{
                background: lightblue;
            }
        }
        @-webkit-keyframes changePosition{
            0%{
                background: lightgreen;
            }
            100%{
                margin-left: 90%;
                background: lightblue;
            }
        }
	html,body,p{margin:0;padding: 0}
	.summary{
	    position: relative;
	    overflow: hidden;
	    margin-bottom: 5px;
	    line-height: 22px;
	    word-break: break-all;
	    text-indent:5em;
	}
	.packup p{
	    height: 90px;
	}
	.packup:before{
	    display: block;
	    content: attr(data-content);
	    position: absolute;
	    z-index: 1;
	    left: 0;
	    top: 0;
	    height: 66px;
	    width: 100%;
	    overflow: hidden;
	    color: #000;
	    background-color: #fff;
	    text-indent: 5em;
	       
	}
	.packup:after{
	    display: -webkit-box;
	    -webkit-box-orient: vertical;
	    -webkit-box-sizing: border-box;
	    box-sizing: border-box;
	    -webkit-line-clamp: 4;
	    content: attr(data-content);
	    position: absolute;
	    left: 0;
	    top: 0;
	    width: 100%;
	    height: 100%;
	    text-indent: -4em;
	    padding-right: 3em;
	    color: #000;
	    background-color: #fff;
	}
	@keyframes move
	{
	    0%
	    {
	        transform:translateY(0px);
	    }
		50%
	    {
	        transform:translateY(-58px);
	    }
	    100%
	    {
	        transform:translateY(0px);
	    }
	}
	.picTab{height:25px; margin:20px auto;overflow:hidden;}
	.picTab .topDiv{width:200px;height:10px; animation:move 8s linear infinite;text-align:center;}
	.picTab div {margin:6px;color:black;  }		
	footer{
		bottom:0px;
		height:79px;
		border-top:1px solid #ddd;
		width:100%;
		background: #f7f7f7;
	}
	.sub-foot{width:1000px;margin:0 auto;text-align: center;}
	.sub-foot ul{}
	.sub-foot li{display:inline-block; height:30px;line-height:30px;margin-left:15px;}
	.sub-foot p{height:30px;line-height: 30px;}
	</style>
  </head>
  
  <body>
	<div id="div1" class="b">
	<div style="display:inline-block;margin-left:120px;">
    <img id="image"src="images/logo.png" width="100" height="100" style="vertical-align:middle;" > 
    <font style="FONT-FAMILY:华文行楷" size=8>欢迎访问高校学者专家系统 </font>	
	</div>
    <DIV class="picTab" style="display:inline-block;margin-left:120px;">
	<div  class="topDiv">
	<div>制作团队：zero</div>
	<div>暑期实训作品</div>
	<div>联系我们：QQ706346717</div>
	</div>
	</DIV>
    </div>

    <br>
    <br>
    <br>
    <br>
    
    
    
     <script>
    $().ready( function() {
    	 
        // do something
    
    getJson();
        
    } );
    </script>
    <script>
	function toUs()
	{
		alert("联系我们： \n雷凡：QQ706346717 \n李龙军：QQ185824626")
	}
	function aboutUs()
	{
		alert("zero团队 \n成员：雷凡 胡志豪 涂珈玮 李龙军 叶茂盛 \n指导老师：孙老师 赵老师 刘老师")
	}
	function aboutThis()
	{
		alert("本项目为zero团队暑期实训项目，由于技术不强、时间不足，项目依旧存在一些问题，请多多包涵，我们也欢迎您向我们提出您宝贵的建议。")
	}
   
    function getJson(){
        $.ajax({
            type:"get",
            dataType:"json",
            url:"expert/getJson",
            success:function(data){
           // 	confirm("123");
            //	var list=${countnums}
            //	confirm(list);
            	datas=JSON.stringify(data)
           // 	confirm(datas);
            	
            	
				var bardata = [];
            	var names= [] ;
            
            	
            	for(var j=0;j<data.length;j++){    //遍历data数组
            							var ls = data[j];     
                	                       var m={};
                    m["value"]=ls.num;
                    m["name"]=ls.name;

                    bardata.push(m);
                	names.push(ls.name);                 
                          
                	                    }
            	
            	var myEchart = echarts.init(document.querySelector('#main'));
            	myEchart.setOption({
                        //设置
                        title:{
                            text:'高校专家数量分布',
                            subtext:'',
                            x:'center'
                        },
                        tooltip:{
                            trigger:'item',
                            formatter: "{a} <br/>{b} : {c} ({d}%)"
                        },
                        //对图例组件的不同系列进行标记说明
                        legend:{
                            orient:'vertical',  //设置图例列表的布局朝向
                            left:'left',
                            data:names
                           
                        },
                        
                        toolbox: {  
                            show : true,  
                            feature : {  
                                mark : {show: true},  
                                dataView : {show: true, readOnly: false},  
                                magicType : {  
                                    show: true,   
                                    type: ['pie', 'funnel'],  
                                    option: {  
                                        funnel: {  
                                            x: '25%',  
                                            width: '50%',  
                                            funnelAlign: 'left',  
                                            max: 1548  
                                        }  
                                    }  
                                },  
                                restore : {show: true},  
                                saveAsImage : {show: true}  
                            }  
                        },  
                        calculable : true,  
                        //系列列表
                        series:[
                            //系列1
                            {
                                name:'高校专家数量分布',
                                type:'pie',    //数据统计图的类型
                                
                                radius : '55%',//饼图的半径大小  
                        		center: ['50%', '60%'],//饼图的位置  
                         	    data:bardata//放置要展示的数据
                            }
                        ]
                    });
    
            	
            	
           //	 var names = [];
            	
            	
            	
            	
            	
            	
            	                
            	
            	
				
            	            
            	  				
            	
        //   	myEchart.setOption(option);        //加载数据图表                
			//		 legend: {                    
		    //                data: names
		    //            },
           //        series: [{                    
           //            data: brower
          //         }]
         //      });
            },
     　　　　error:function(e){
    	 confirm("error");
    　　　　　　alert(e);
    　　    }
        })
    }
    
    
    </script>
    
    
  



    <div class="nav" style="text-align:center;width:100%;background:#EEEEEE;background-size:cover;">
        <ul>
		<li style="margin-left:120px;"><a class="on" href="${pageContext.request.contextPath}"><font color="#856363" size="5"><b>首页</b></font></a></li>
		<li><a href="expert/getExpertByName"><font color="#856363" size="5"><b>专家</b></font></a></li>
		<li><a href="expert/getExpertBySchool"><font color="#856363" size="5"><b>高校</b></font></a></li>
		<li><a href="expert/getExpertByMajor"><font color="#856363" size="5"><b>专业</b></font></a></li>
		<li><a href="expert/getExpertBySubject"><font color="#856363" size="5"><b>学科</b></font></a></li>
		<li><a href="expert/getExpertByPaper"><font color="#856363" size="5"><b>论文</b></font></a></li>
		<li><a href="expert/getExpertByResearchDirection"><font color="#856363" size="5"><b>研究领域</b></font></a></li>
		<li style="margin-left:50px;">
			<form action="expert/getExpertByName"  method="post" accept-charset="UTF-8" onsubmit="document.charset='UTF-8'">    
		    <input type="text" name="name" style="width:200px; height:40px;vertical-align: top;" placeholder="请输入专家名"/> 
		    <input type="image" src="images/query1.jpg" style="width:40px; height:40px;"/>  
		  	</form>
		</li>
	    </ul>   
    </div>
<br>
<br>
<br>
<div id="main" style="width:100%;height:500px"></div>
<br>
<br>
<br>
 	<c:forEach  items="${expertList}" var="expert">
  	 	<div class="loading">
        <span></span>
		</div>
  		<div style="margin:0;" class="expertDetail panel c">
  		<br>
    		<div class="expertPicture">
    			<img src="images/logo.png" class="img-circle" height="150" width="150">
    		</div>
    		<br>
    		<div class="panel panel-primary" id="expertDescription">
				<div class="panel-heading">
					<h3 class="panel-title"><a href="expert/getExpertById?id=${expert.id}">${expert.name}</a></h3>
					<span class="label label-warning"><a href="expert/getExpertBySchool?school=${expert.school}">${expert.school}</a></span>
					<span class="label label-warning"><a href="expert/getExpertByMajor?major=${expert.major}">${expert.major}</a></span>
					<span class="label label-warning"><a href="expert/getExpertBySubject?subject=${expert.subject}">${expert.subject}</a></span>
					<span class="label label-warning"><a href="expert/getExpertByResearchDirection?research_direction=${expert.research_direction}">${expert.research_direction}</a></span>
				</div>
			<div class="panel-body">
				    <details>
 			        <summary style="margin-left:-900px;outline:none;"><font color="#4B0082" size="4">详情</font></summary>
			            <p>${expert.introduction}</p>
    				</details>
			</div>
			</div>
		</div>
	</c:forEach>
	<div>
	<footer class="footer">
			<div class="sub-foot">
				<ul>
					<li><a onclick="aboutUs()"><font size="2.5px">关于我们</font></a></li>
					<li><svg width="16" height="16" style="vertical-align:middle;"
					 		 xmlns="http://www.w3.org/2000/svg">
					 		<path d="M2.167 2h11.666C14.478 2 15 2.576 15 3.286v9.428c0 .71-.522 1.286-1.167 1.286H2.167C1.522 14 1 13.424 1 12.714V3.286C1 2.576 1.522 2 2.167 2zm-.164 3v1L8 10l6-4V5L8 9 2.003 5z" fill="#999AAA" fill-rule="evenodd"></path>
					 	</svg>
					 	<a href="mailto:706346717@qq.com"><font size="2.5px">706346717@qq.com</font></a>
					 	</li>
					<li><a onclick="toUs()"><font size="2.5px">联系我们</font></a></li>
					<li><a onclick="aboutThis()"><font size="2.5px">常见问题</font></a></li>
				</ul>
				<p>版权所有@2020zero团队</p>
			</div>
		</footer>
	</div>
  </body>
</html>
