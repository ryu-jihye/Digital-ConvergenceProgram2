<%@page import="java.text.SimpleDateFormat"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ page import="java.util.Date"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<style>
h1 {
	text-align: center;
}

table {
	margin-left: auto;
	margin-right: auto;
}

h3 {
	text-align: center;
	color: white;
}

h4 {
	text-align: left;
	color: black;
}

.container {
	padding-top: 100px;
	padding-bottom: 30px;
}

.tacontent {
	width: 550px;
	height: 100px;
	padding: 8px;
	border-radius: 5px;
}

input[type=text], input[type=password], textarea {
	width: 550px;
	height: 30px;
	border: none;
	font-size: 18px;
	background-color: white;
}

input[type=submit] {
	width: 563px;
	height: 40px;
	border: none;
	font-size: 18px;
}

.ip {
	display: flex;
	justify-content: center;
	align-items: center;
}

.ip>input {
	font-size: 18px;
	border-radius: 5px;
	padding: 8px;
	background-color: white;
	border: white;
}

.sm {
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 18px;
}

.sm>input {
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 18px;
	background-color: white;
	border-radius: 5px;
}

.sm>input:hover {
	background-color: black;
}

table {
	width: 980px;
}

#order {
	padding-top: 15px;
	padding-bottom: 15px;
}

.container {
	padding-top: 100px;
	padding-bottom: 30px;
}

input[readonly] {
	background-color: #E3DCAC
}

.content {
	padding-top: 20px;
	padding-bottom: 20px;
}

.ip {
	padding-top: 30px;
}

.sm {
	padding-top: 20px;
}

.aleft {
	padding-right: 20px;
}

.aright {
	padding-left: 20px;
}

.tacontent {
	width: 550px;
	height: 100px;
	padding: 8px;
	border-radius: 5px;
}

h1 {
	text-align: center;
	color: white;
}

h3 {
	text-align: left;
	color: white;
}

div1 {
	float: left;
}
.faqButton {
	float: right;
	box-shadow:inset 0px 1px 0px 0px #ffffff;
	background:linear-gradient(to bottom, #ffffff 5%, #f6f6f6 100%);
	background-color:#fffff;
	border-radius:6px;
	border:1px solid #dcdcdc;
	display:inline-block;
	cursor:pointer;
	color:#CCCBA5;
	font-size:15px;
	font-weight:bold;
	padding:6px 24px;
	text-decoration:none;
}
</style>
<meta charset="UTF-8">
<title>관리자 글쓰기</title>
<jsp:include page="../menu.jsp" />
</head>
<body>
	<br>
	<br>
	<br>
	<br>
	<h1>글쓰기 페이지</h1>
	<%
		String userID = null; // 로그인이 된 사람들은 로그인정보를 담을 수 있도록한다
	if (session.getAttribute("userID") != null)//이 세션을 유지하는 사람이라면 이 아이디 값을 받아서 관리할 수 있게 해줌
		userID = (String) session.getAttribute("userID"); //userID값 가져옴

	String userPassword = null; // 로그인이 된 사람들은 로그인정보를 담을 수 있도록한다
	if (session.getAttribute("userPassword") != null)//이 세션을 유지하는 사람이라면 이 아이디 값을 받아서 관리할 수 있게 해줌
		userPassword = (String) session.getAttribute("userPassword"); //userID값 가져옴

	SimpleDateFormat sdformat = new SimpleDateFormat("yyyy-MM-dd");
	Date time = new Date();
	String iqdate = sdformat.format(time);
	%>
	<table>
		<form name=writeform method=post action="nwriteProc.jsp">
			<tr>
				<td>
					<table width="100%" cellpadding="0" cellspacing="0" border="0">
						<div class="ip">
							<h3>이름</h3>
							<input type="text" name="userid">
						</div>
						<div class="ip">
							<h3>비밀번호</h3>
							<input type="text" name="password" value>
						</div>

						<div class="ip">
							<h3>날짜</h3>
							<input type="text" name="iqdate" value=<%=iqdate%> readonly>
						</div>
						<div class="ip">
							<h3>제목</h3>
							<input type="text" name="title">
						</div>
						<div class="ip">
							<h3>내용</h3>
							<input type="text" name="content">
						</div>

						<a href="faq/nlist.jsp" OnClick="javascript:writeCheck();" returnfalse;></a>

						<input type=button value="취소" OnClick="javascript:history.back(-1)" class="faqButton">
						<input type=button value="등록" OnClick="javascript:writeCheck();" class="faqButton"> 
	</table>
	</td>
	</tr>
	</form>
	</table>
</body>
<script language="javascript">
	function writeCheck() {
		var form = document.writeform;

		if (!form.userid.value) // form 에 있는 name 값이 없을 때
		{
			alert("이름을 적어주세요"); // 경고창 띄움
			form.userid.focus(); // form 에 있는 name 위치로 이동
			return;
		}

		if (!form.password.value) {
			alert("비밀번호를 적어주세요");
			form.password.focus();
			return;
		}

		if (!form.title.value) {
			alert("제목을 적어주세요");
			form.title.focus();
			return;
		}

		if (!form.content.value) {
			alert("내용을 적어주세요");
			form.content.focus();
			return;
		}

		form.submit();
	}
</script>
</html>