<%@ page language="java" contentType="text/html; charset=utf-8"
	pageEncoding="utf-8"%>
<%@ page import="java.sql.*"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%
	request.setCharacterEncoding("utf-8");
Class.forName("oracle.jdbc.driver.OracleDriver");
String url = "jdbc:oracle:thin:@localhost:1521:xe";
String id = "scott";
String pass = "tiger";

String userid = "";
String password = "";
String title = "";
String content = "";
int idx = Integer.parseInt(request.getParameter("idx"));

try {

	Connection conn = DriverManager.getConnection(url, id, pass);
	Statement stmt = conn.createStatement();

	String sql = "SELECT userid, PASSWORD, TITLE, CONTENT FROM inquiry WHERE IQNO=" + idx;
	ResultSet rs = stmt.executeQuery(sql);

	if (rs.next()) {

		userid = rs.getString(1);
		password = rs.getString(2);
		title = rs.getString(3);
		content = rs.getString(4);
	}

	rs.close();
	stmt.close();
	conn.close();
} catch (SQLException e) {
	out.println(e.toString());
}
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
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
	box-shadow: inset 0px 1px 0px 0px #ffffff;
	background: linear-gradient(to bottom, #ffffff 5%, #f6f6f6 100%);
	background-color: #fffff;
	border-radius: 6px;
	border: 1px solid #dcdcdc;
	display: inline-block;
	cursor: pointer;
	color: #CCCBA5;
	font-size: 15px;
	font-weight: bold;
	padding: 6px 24px;
	text-decoration: none;
}
</style>
<title>수정 페이지</title>
<jsp:include page="../menu.jsp" />
</head>
<br>
<br>
<br>
<br>
<br>
<h1>수정 페이지</h1>
<body>
	<%
		String userID = null; // 로그인이 된 사람들은 로그인정보를 담을 수 있도록한다
	if (session.getAttribute("userID") != null)//이 세션을 유지하는 사람이라면 이 아이디 값을 받아서 관리할 수 있게 해줌
		userID = (String) session.getAttribute("userID"); //userID값 가져옴
	%>
	<table>
		<form name=modifyform method=post
			action="nmodifyProc.jsp?idx=<%=idx%>">
			<tr>
				<td>
					<table width="100%" cellpadding="0" cellspacing="0" border="0">
					</table>
					<div class="ip">
						<h3>제목</h3>
						<input type="text" name="title" value=<%=title%>>
					</div>
					<div class="ip">
						<h3>이름</h3>
						<input type="text" type=hidden name="userid" value=<%=userid%>>
					</div> <c:if test="${userID != null}">
						<div class="ip">
							<h3>비밀번호</h3>
							<input type="text" name="password" value="">
						</div>
					</c:if> <c:if test="${userID == 'manager'}">
						<div class="ip">
							<h3>참고용 비밀번호</h3>
							<input type="text" name="password1" value="<%=password%>">
						</div>
					</c:if>
					<div class="ip">
						<h3>내용</h3>
						<input type="text" name="content" value=<%=content%>>
					</div> 
					<input type=button value="취소" class="faqButton" OnClick="javascript:history.back(-1)">
					<input type="button" value="수정" class="faqButton" OnClick="javascript:modifyCheck();"> 
			</tr>
</body>
<script language="javascript">
	// 자바 스크립트 시작
	function modifyCheck() {
		var form = document.modifyform;

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
			form.memo.focus();
			return;
		}
		form.submit();
	}
</script>
</html>