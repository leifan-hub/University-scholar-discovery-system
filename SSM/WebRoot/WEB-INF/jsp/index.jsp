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
		background:url(images/bg.jpg) 0 0 no-repeat #B0E0E6;
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
	</style>
  </head>
  
  <body>
	<div id="div1" class="b">
    <img id="image"src="images/logo.png" width="100" height="100" style="vertical-align:middle;" > 
    <font style="FONT-FAMILY:华文行楷" size=8>欢迎访问高校学者专家系统 </font>
    </div>
    <br>
    <br>
    <br>
    <br>
    <div class="nav" style="text-align:center;width:100%;background:#F8F8FF;background-size:cover;">
        <ul>
		<li style="margin-left:120px;"><a class="on" href="${pageContext.request.contextPath}"><font color="red" size="5"><b>首页</b></font></a></li>
		<li><a href="expert/getExpertByName"><font color="red" size="5"><b>专家</b></font></a></li>
		<li><a href="expert/getExpertBySchool"><font color="red" size="5"><b>高校</b></font></a></li>
		<li><a href="expert/getExpertByMajor"><font color="red" size="5"><b>专业</b></font></a></li>
		<li><a href="expert/getExpertBySubject"><font color="red" size="5"><b>学科</b></font></a></li>
		<li><a href="expert/getExpertByPaper"><font color="red" size="5"><b>论文</b></font></a></li>
		<li><a href="expert/getExpertByResearchDirection"><font color="red" size="5"><b>研究领域</b></font></a></li>
		<li style="margin-left:50px;">
			<form action="expert/getExpertByName"  method="post" accept-charset="UTF-8" onsubmit="document.charset='UTF-8'">    
		    <input type="text" name="name" style="width:200px; height:40px;" placeholder="请输入专家名"/> 
		    <input type="submit" style="width:40px; height:40px;" value="搜索"/>  
		  	</form>
		</li>
	    </ul>   
    </div>
<br>
<br>
<br>
<br>
 	<c:forEach items="${expertList}" var="expert">
  		<div class="expertDetail panel c">
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
				${expert.introduction}
			</div>
			</div>
		</div>
		<br>	
	</c:forEach>

  </body>
</html>
