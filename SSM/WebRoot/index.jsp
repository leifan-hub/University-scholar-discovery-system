<%@ page language="java" import="java.util.*" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'index.jsp' starting page</title>
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	
	<link rel="stylesheet" type="text/css" href="css/style1.css">
	
  </head>
  
  <body class="c-red">
  <img src="images/350.jpg">
    This is my JSP page. <br>
    
    
    <a href="expert/getExpertList">点击进入列表页</a>
    <br>
    <a href="expert/preaddExpert">点击进入添加用户页</a>
    <a href="expert/expertDetail">点击进入用户详情页</a>
    <center>
   <br>
	<!--	<form action="getUserList" method="get">
			123
		  	 <input type="submit" value="确定">  
		</form> -->
	</center>
<form action="expert/getExpertByName"  method="post" accept-charset="UTF-8" onsubmit="document.charset='UTF-8'">
    	搜索用户名：<input type="text" name="name" />
    	<br>
    	
    	<input type="submit" value="点击提交" />
    </form> 



  </body>
</html>
