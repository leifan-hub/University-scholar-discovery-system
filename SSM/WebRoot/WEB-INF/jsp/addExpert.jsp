
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
 <!-- 
 author： 李龙军  胡志豪
 create: time: 2020-07-05
 update：time:  2020-07-10
 -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'addUser.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->
 
  </head>
  
  <body>
    <form action="expert/addExpert" method="post" accept-charset="UTF-8" onsubmit="document.charset='UTF-8'">
    	id：<input type="text" name="id" />
    	<br>
    	name：<input type="text" name="name" />
    	<br>
    	school：<input type="text" name="school" />
    	<br>
    	major：<input type="text" name="major" />
    	<br>
    	subject：<input type="text" name="subject" />
    	<br>
    	paper：<input type="text" name="paper" />
    	<br>
    	research_direction：<input type="text" name="research_direction" />
    	<br>
    	introduction：<input type="text" name="introduction" />
    	<br>
    	<input type="submit" value="点击提交" />
    </form> 
  </body>
</html>