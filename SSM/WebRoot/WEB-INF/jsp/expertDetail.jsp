<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/WebRoot";
String str_id=request.getParameter("id");
%>
<!-- 
 author：雷凡 叶茂盛 
 create: time: 2020-07-07
 update：time:  2020-07-16
 -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
	<head>
    	<base href="<%=basePath%>">
    	<title>expert detail</title>
    	<meta http-equiv="pragma" content="no-cache">
		<meta http-equiv="cache-control" content="no-cache">
		<meta http-equiv="expires" content="0">    
		<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
		<meta http-equiv="description" content="This is my page">
		<link href="css/style1.css" rel="stylesheet">
		<!-- 新 Bootstrap 核心 CSS 文件 -->
		<link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
		<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
		<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
		<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
		<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
		<style type="text/css">
			#expertDescription {
				display: inline-block;
		    	line-height:30px;
		    	width:800px;
		    	text-align:center;
		    	float:top;
		}
			.expertPicture {
				display: inline-block;
				vertical-align: middle;
				position:relative;

				float:top;
			}
			#changePage{
				position:relative;
		    	left:130px;
			}
			.expertArticle{
				float:left;
				width:900px;
			}
			.representative-works{
				float:right;
				width:350px;
			}
			.projects{
				float:right;
				width:350px;
			}
			.hot-tags{
				float:right;
				width:350px;
			}
			.hot-scholars{
				float:right;
				width:350px;
			}
			a:link{color:#000000}
			</style>
	</head>
  
	<body>
  		<div class="expertDetail">
    		<div class="expertPicture">
    			<img src=${picUrl} class="img-circle" height="150" width="150">
    		</div>
    		<div class="panel panel-primary" id="expertDescription">
				<div class="panel-heading">
					<h3 class="panel-title">${expert.name}</h3>
					<span class="label label-warning"><a href="expert/getExpertBySchool?school=${expert.school}">${expert.school}</a></span>
					<c:forEach var="expertTag" items="${expertTags}" >
        				<span class="label label-warning"><a href="expert/getExpertByResearchDirection?research_direction=${expertTag}">${expertTag}</a></span>
   					</c:forEach>
				</div>
			<div class="panel-body">
				${expert.introduction}
			</div>
			</div>
			<a href="expert/returnIndex"><font color="blue" size="5"><b>返回主页</b></font></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
		</div>
		<div class="expertArticle">
			<ul class="list-group">
    			<li class="list-group-item active">文章</li>
    			<c:forEach var="expertPaper" items="${expertPapers}" >
        			<li class="list-group-item"><a>${expertPaper}</a></li>
   				</c:forEach>
    			<li class="list-group-item">
    				<ul class="pagination" id="changePage">
						<li><a href="#">&laquo;</a></li>
						<li class="active"><a>1</a></li>
						<li><a>2</a></li>
						<li><a>3</a></li>
						<li><a>4</a></li>
						<li><a>5</a></li>
						<li><a>&raquo;</a></li>
					</ul>
    			</li>
			</ul>			
		</div>
		<div class="representative-works">
			<div class="panel panel-default">
    			<div class="panel-heading">
        			<h3 class="panel-title">玫瑰图</h3>
    			</div>
    			<div class="panel-body">
        			<img src="RoseCharts/${expert.name}_rose.png" class="img-rounded" height="300" width="300">
    			</div>
			</div>
				<div class="projects">
					<div class="panel panel-default">
	    				<div class="panel-heading">
	        				<h3 class="panel-title">词云图</h3>
	    				</div>
	    				<div class="panel-body">
	        				<img src="WordClouds/${expert.name}.png" class="img-rounded" height="200" width="200">
	    				</div>
					</div>
					<div class="hot-tags">
						<div class="panel panel-default">
		    				<div class="panel-heading">
		        				<h3 class="panel-title">热门标签</h3>
		    				</div>
		    				<div class="panel-body">
		    					<h4>
		        				<span class="label label-warning"><a>大数据</a></span>
								<span class="label label-warning"><a>人工智能</a></span>
								<span class="label label-warning"><a>机器学习</a></span>
								<span class="label label-warning"><a>区块链</a></span>
								</h4>
		    				</div>
						</div>
						<div class="hot-scholars">
							<div class="panel panel-default">
		    					<div class="panel-heading">
		        					<h3 class="panel-title">同领域学者</h3>
		    					</div>
		    					<div class="panel-body">
		    						<c:forEach items="${expertRelated}" var="expertR">   
			        					<a href="expert/getExpertById?id=${expertR.id}"><img src=${expertR.major} class="img-rounded" height="200" width="200"></a>
			        					<h3><a href="expert/getExpertById?id=${expertR.id}">${expertR.name}</a></h3>
			        				</c:forEach>
		    					</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		<!--
		<div style="float:left">
		<div class="d-sty">
		<h3 class="h-sty">同研究方向学者</h3>
		</div>
          <c:forEach items="${expertrelatedList}" var="expertrelated">   
            <div class="div-style1">
            <div class="div-style2">
            <img class="img-style1" src="images/head.png">
            <img class="img-style2" src="images/identity.png"/> 
            </div>
            <div class="m-180">
                  <a class="a-style1" href="expert/getExpertById?id=${expertrelated.id}" >
                  <span class="s-style1">${expertrelated.name}</span>
                  <span class="s-style2">${expertrelated.school}</span>       
                  </a>          
                                     
    	          <p class="p-style1">
                                     简介:${expertrelated.introduction} </p>
                 <p style="color: #666;font-size: 16px;">研究方向：${expertrelated.research_direction}</p>
            </div>                
    	    </div> 	    
        </c:forEach>
    </div>
		-->
		
	</body>
</html>
