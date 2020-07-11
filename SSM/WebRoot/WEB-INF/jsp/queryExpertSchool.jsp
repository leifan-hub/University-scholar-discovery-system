<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>user.jsp</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->
	<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
	<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
  </head>
  

    <body style="background:#FFFFF4">
      <div id="div1" style="text-align:center;">

    <img id="image"src="images/query.jpg" width="100" height="100" style="vertical-align:middle" > 
    <font style="FONT-FAMILY:华文行楷" size=6>按专家所属学校进行查询 </font>
  </div>
  <br>
    <nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">切换查询方式</a>
    </div>
    <div>
        <ul class="nav navbar-nav">
            <li><a href="expert/getExpertByName">按名字查询</a></li>
            <li><a href="expert/getExpertByMajor">按专业查询</a></li>
            <li><a href="expert/getExpertBySubject">按学科查询</a></li>
            <li><a href="expert/getExpertByPaper">按论文查询</a></li>
            <li><a href="expert/getExpertByResearchDirection">按研究方向查询</a></li>
        </ul>
    </div>
    </div>
</nav>
    <form action="expert/getExpertBySchool"  method="post" accept-charset="UTF-8" onsubmit="document.charset='UTF-8'">
    	搜索专家所属学校：<input type="text" name="school" />
    	<br>
    	
    	<input type="submit" value="搜索" />
    </form>  
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
     <a href="${pageContext.request.contextPath}"><img src="images/return.jpg"  class="img-full" style="width: 68px; height: 37px; "/></a>
     <br>
     <a href="expert/returnIndex"><img src="images/return.jpg"  class="img-full" style="width: 68px; height: 37px; "/></a>
  </body>
</html>
