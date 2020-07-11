<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/WebRoot";
%>

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
				text-align:center;
			}
			a:link{color:#000000}
			</style>
	</head>
  
	<body>
  		<div class="expertDetail">
    		<div class="expertPicture">
    			<img src="images/yeqiu.jpeg" class="img-circle" height="150" width="150">
    		</div>
    		<div class="panel panel-primary" id="expertDescription">
				<div class="panel-heading">
					<h3 class="panel-title">${expert.name}</h3>
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
		<div class="expertArticle">
			<ul class="list-group">
    			<li class="list-group-item active">文章</li>
    			<li class="list-group-item"><a>打怪秘籍</a></li>
    			<li class="list-group-item"><a>武器维修图纸大全</a></li>
    			<li class="list-group-item"><a>一夜暴富秘籍</a></li>
    			<li class="list-group-item"><a>如何讨取富婆的欢心</a></li>
    			<li class="list-group-item"><a>论人类的发展前景</a></li>
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
        			<h3 class="panel-title">代表著作</h3>
    			</div>
    			<div class="panel-body">
        			《五年高考，三年模拟》
    			</div>
			</div>
		</div>
		<div class="projects">
			<div class="panel panel-default">
    			<div class="panel-heading">
        			<h3 class="panel-title">项目</h3>
    			</div>
    			<div class="panel-body">
        			《全职高手》
    			</div>
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
		</div>
		<div class="hot-scholars">
			<div class="panel panel-default">
    			<div class="panel-heading">
        			<h3 class="panel-title">同领域学者</h3>
    			</div>
    			<div class="panel-body">
        			<img src="images/sumucheng.jpg" class="img-circle" height="150" width="150">
        			<img src="images/huangshaotian.jpg" class="img-circle" height="150" width="150">
        			苏沐橙            黄少天<br/>
        			<img src="images/qiaoyifan.jpg" class="img-circle" height="150" width="150">
        			<img src="images/luoji.jpg" class="img-circle" height="150" width="150">
        			<img src="images/tangrou.jpg" class="img-circle" height="150" width="150">
        			<img src="images/baorongxing.jpg" class="img-circle" height="150" width="150">
    			</div>
			</div>
		</div>
	</body>
</html>
