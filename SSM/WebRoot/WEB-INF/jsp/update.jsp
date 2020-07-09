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

  </head>
  
  <body>
    This is my JSP page. <br>
    
    <form action="expert/update"  method="post" accept-charset="UTF-8" onsubmit="document.charset='UTF-8'">
    	编号：<input type="text" value="${expert.id}" name="id" readonly="true"/>
    	<br>
    	用户名：<input type="text" value="${expert.name}" name="name" />
    	<br>
    	
    	<input type="submit" value="点击修改" />
    </form> 

     <a href="${pageContext.request.contextPath}">返回主页</a>
     <a href="expert/returnIndex">返回主页</a>
  </body>
</html>