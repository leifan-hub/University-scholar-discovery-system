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
    
    <c:forEach items="${expertList}" var="expert">
    	<hr>
    	id:${expert.id}
    	<br>
    	name:${expert.name}
    	<br>
    	<a href="expert/delete?id=${expert.id}">删除</a>
    	<a href="expert/preupdate?id=${expert.id}">修改</a>
    	<hr>
    </c:forEach>
     <a href="${pageContext.request.contextPath}">返回主页</a>
     <a href="expert/returnIndex">返回主页</a>
  </body>
</html>
