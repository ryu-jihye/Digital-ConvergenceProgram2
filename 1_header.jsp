<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<!-- icon link -->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css"/>
<!-- css link -->
	<link rel="stylesheet" type="text/css" href="1header_css.css">
<!-- 반응형 웹 관련 link -->	
	<link rel="stylesheet" media="screen and (max-width: 768px)" href="1header_css.css" />
<!-- font link -->
	<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
<!-- java script -->
	<script src="1header_js.js" defer></script>
</head> 
<meta charset="UTF-8">
<title>Nav Bar</title>
</head>
<body>
	<nav class="navbar">
		<a href="#"><img class="main_logo_img" src="images/logo.png" ></a>
		<div class="navbar_logo">
			<a href="#"><i class="fas fa-pen-square">관리자</i></a>
		</div>
		<!-- 관리자 ~ 회원정보 간격 조정 -->
		<ul class="navbar_interval">
			<li></li><li></li><li></li>
			<li></li><li></li><li></li>
		</ul>	
		<ul class="navbar_menu">
			<li><a href="#"><i class="fas fa-sign-in-alt">로그인</i></a></li>
			<li><a href="#"><i class="fas fa-sign-out-alt">로그아웃</i></a></li>
			<li><a href="#"><i class="fas fa-bookmark">예약관리</i></a></li>
			<li><a href="#"><i class="fas fa-address-card">회원정보</i></a></li>
		</ul>
		
		<ul class="navbar_icons">
			<li><a href="#"><i class="fas fa-home">홈</i></a></li>
		</ul>
		<a href="#" class="navbar_toogleBtn">
			<i class="fas fa-bars"></i></a>
	</nav>
</body>
</html>