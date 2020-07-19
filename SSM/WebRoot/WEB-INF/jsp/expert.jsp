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
	
	<link rel="stylesheet" type="text/css" href="css/style1.css">
	

  </head>
  
 <body >
    <c:forEach items="${expertList}" var="expert">
    	<hr>
    	id:${expert.id}
    	<br>
    	name:${expert.name}
    	<br>
    	${expert.research_direction}
    	<br>
    	<a href="expert/delete?id=${expert.id}">删除</a>
    	<a href="expert/preupdate?id=${expert.id}">修改</a>
    	<hr>
    </c:forEach>
    <div >
        <c:forEach items="${expertrelatedList}" var="expertrelated">
       
            <div style="width:700px;height:170px;padding:5px;line-height: 1.8;border:1px solid #ddd;background-color:rgb(250,250,250)" >
           
            <div style="position:absolute;width:160px">
            <img style="border-radius:50%; width:120px;height: 120px;border:2px solid #ddd;
                         position:absolute;left:20px; top:17px;" 
                        src="images/head.png">
            <img style="position:absolute;left:235px; top:22px;width:16px; height:16px" src="images/identity.png"/>
            
            </div>
            <div style="margin-left:180px">
                  <a href="expert/getExpertById?id=${expertrelated.id}" style="display:block;text-decoration:none;margin-top:16px">
                  <span style="color: #333;font-size: 18px;font-weight:400;">${expertrelated.name}</span>
                  <span style="color: #666;font-size: 16px;margin-left:40px"> ${expertrelated.school}</span>       
                  </a>          
    	          <p style="display: -webkit-box;
                            overflow: hidden;
                            padding-right: 20px;
                            height: 40px;
                            line-height: 20px;
                            font-size: 14px;
                            color: #666;
                            text-overflow: ellipsis;
                            -webkit-line-clamp: 2;
                            -webkit-box-orient: vertical;">
                                     简介${expertrelated.introduction}1982年、1988年分获海军工程大学学士和硕士学位，
                 1997年获清华大学博士学位。曾在德国不伦瑞克工业大学作访问学者。
                                     现为烟台海军航空工程学院院长、教授、博士生导师，海战场信息感知与融合技术军队重点实验室主任，
                                     中国航空学会信息融合分会主任委员，中国电子学会会士，IET Fellow等。2013年当选为中国工程院院士。 </p>
                 <p style="color: #666;font-size: 16px;">研究方向：${expertrelated.research_direction}</p>
            </div>                

    	    </div>
    	    
        </c:forEach>
    </div>
    
     <a href="${pageContext.request.contextPath}">返回主页</a>
     <a href="expert/returnIndex">返回主页</a>
  </body>
</html>
