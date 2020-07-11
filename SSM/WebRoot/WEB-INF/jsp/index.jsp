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
	.a{
		text-decoration: none;
    	line-height: 35px;
	}
	.b{
		z-index:10;
		position: fixed;
		width:100%;
	    height:180px;
		text-align:center;
	 	background:url(images/bg.jpg);
		background-size:cover;
	}
	.mainnav {
		z-index:10;
	    height: 40px;
	    line-height: 40px;
		border-bottom: 3px solid #ff7900; 
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
	</style>
  </head>
  
  <body>
  <div id="div1" class="b">
  	<br>
    <img id="image"src="images/logo.png" width="100" height="100" style="vertical-align:middle;" > 
    <font style="FONT-FAMILY:华文行楷" size=8>欢迎访问高校学者专家系统 </font>
    <br>
    <br>
    <div class="mainnav">
    <form action="expert/getExpertByName"  method="post" accept-charset="UTF-8" onsubmit="document.charset='UTF-8'">    
    <div id="mainnav" style="text-align:center;display:block;">    
    <a href="${pageContext.request.contextPath}" class="a"><font color="red" size="6"><b>首页</b></font></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="expert/getExpertList" class="a"><font color="red" size="6"><b>专家</b></font></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="expert/getExpertList" class="a"><font color="red" size="6"><b>高校</b></font></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="expert/getExpertList" class="a"><font color="red" size="6"><b>专业领域</b></font></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="expert/getExpertList" class="a"><font color="red" size="6"><b>论文</b></font></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="expert/getExpertList" class="a"><font color="red" size="6"><b>研究领域</b></font></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <input type="text" name="name" style="width:200px; height:30px;line-height:40px;" placeholder="请输入专家名"/> 
    <input type="submit" style="width:40px; height:30px;line-height:40px;" value="搜索" />  
    </div>
  	</form>
    </div>
  </div>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
 	<c:forEach items="${expertList}" var="expert">
  		<div class="expertDetail panel" style="background:#F8F8FF;text-align:center;width:100%;">
    		<div class="expertPicture">
    			<img src="images/logo.png" class="img-circle" height="150" width="150">
    		</div>
    		<div class="panel panel-primary" id="expertDescription">
				<div class="panel-heading">
					<h3 class="panel-title"><a href="expert/getExpertList">${expert.name}</a></h3>
					<span class="label label-warning"><a>${expert.school}</a></span>
					<span class="label label-warning"><a>${expert.major}</a></span>
					<span class="label label-warning"><a>${expert.subject}</a></span>
					<span class="label label-warning"><a>${expert.research_direction}</a></span>
				</div>
			<div class="panel-body">
				${expert.introduction}
			</div>
			</div>
		</div>
		<br>	
	</c:forEach>

    
    
<!-- <form action="expert/getExpertByName"  method="post" accept-charset="UTF-8" onsubmit="document.charset='UTF-8'"> -->
<!--     	搜索用户名：<input type="text" name="name" /> -->
<!--     	<input type="submit" value="点击提交" />    	 -->
<!--     	<br> -->
<!-- </form>  -->


  </body>
</html>
