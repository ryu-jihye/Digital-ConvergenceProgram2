<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<title>CSS를 일렬로 나열하기</title>
<style type="text/css">
a {/* 기본 설정*/
	text-decoration: none;
	color: #000000;
}
a:hover {
	color: #ff0000;
}
/* nav tag */
nav ul {
	padding-top: 10px; /*  상단 여백 10px  */
} 
nav ul li {
	display: inline; /*  세로나열을 가로나열로 변경 */
	/* border-left: 1px solid #999; /* 각 메뉴의 왼쪽에 "|" 표시(분류 표시) */ */
	font: bold 12px Dotum; /* 폰트 설정 - 12px의 돋움체 굵은 글씨로 표시 */
	padding: 0 30px;
	float: right; /* 각 메뉴 간격 */
	height: 100px;
    line-height: 100px;
    background-color: red;
}
nav ul li:first-child {
	border-left: none;
}
nav ul li img {
	height: 20px;
	width: 25px;
    vertical-align: middle;
}
</style>
</head>
<body>
	<nav>
		<ul>		
			<li><a href="#">예약관리</a></li>
			<li><a href="#"><img src="images/user.png" /><a href="#">회원정보</a></li>
			<li><a href="#">로그인</a></li>
			<li><a href="#">로그아웃</a></li>
			<li><a href="#"><img src="images/home.png" />홈</a></li>
		</ul>
	</nav>
</body>
</html>