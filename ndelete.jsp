<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page import="java.sql.*"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<%
	String userID = null; // 로그인이 된 사람들은 로그인정보를 담을 수 있도록한다
if (session.getAttribute("userID") != null)//이 세션을 유지하는 사람이라면 이 아이디 값을 받아서 관리할 수 있게 해줌
	userID = (String) session.getAttribute("userID"); //userID값 가져옴
//nview.jsp에서 보낸 idx값 저장
%>
<style>
h1 {
	text-align: center;
}

table {
	width: 980px;
	border: 3px solid #E2E8CA;
}

#order {
	padding-top: 15px;
	padding-bottom: 15px;
}

tr, th {
	padding-top: 8px;
	padding-bottom: 8px;
	border-bottom: 1px solid #E2E8CA;
}

#tablebt {
	align: left;
	padding-top: 10px;
	font-size: 18px;
}

#boardtable {
	padding-top: 30px;
	padding-bottom: 20px;
}

.faqName {
	padding-bottom: 30px;
}

.faqh1 {
	text-align: center;
	color: white;
}

.total {
	float: right;
	color: white;
}

.container {
	padding-top: 100px;
	padding-bottom: 30px;
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
<title>삭제 페이지</title>
<%-- <jsp:include page="../menu.jsp" /> --%>
<br>
<br>
<h1>삭제 페이지</h1>
</head>
<body>
<%
	request.setCharacterEncoding("utf-8");
	Class.forName("oracle.jdbc.driver.OracleDriver");
	String url = "jdbc:oracle:thin:@localhost:1521:xe";
	String id = "scott";
	String pass = "tiger";
	String password = "";
	password = request.getParameter("password");
	int idx = Integer.parseInt(request.getParameter("idx"));

	try {

		Connection conn = DriverManager.getConnection(url, id, pass);
		Statement stmt = conn.createStatement();

		String sql = "SELECT PASSWORD FROM inquiry WHERE IQNO=" + idx;
		ResultSet rs = stmt.executeQuery(sql);

		if (rs.next()) {
			password = rs.getString(1);
		}

		rs.close();
		stmt.close();
		conn.close();
	} catch (SQLException e) {
		out.println(e.toString());
	}

%>
	<jsp:include page="../menu.jsp" />

		<form name=deleteform method=post
			action="ndeleteProc.jsp?idx=<%=idx%>">
			<tr>
				<td>
					<c:if test="${userID!=null}">
							<tr>
								<div class="ip">
								<h3>비밀번호</h3><input type="text" name="password">
								</div>
						</c:if>
						
						<c:if test="${userID == 'manager'}">
							<tr>
								<div class="ip">
								<h3>위의 비밀번호를 해당 것과 동일하게 입력</h3><input type="text" name="password1" value="<%=password%>">
								</div>
						</c:if>
						<!-- <div1><a href='ndelete.jsp' onclick="javascript:deleteCheck();" style="float:left;"><h2>삭제</h2></a><br><br></div> -->
							<td colspan="2"><input type=button value="취소" OnClick="javascript:history.back(-1)" class="faqButton">
							<td colspan="2"><input type=button value="삭제" OnClick="javascript:deleteCheck();" class="faqButton">
							<td>&nbsp;</td>
						</tr>
				</td>
			</tr>
</body>	
<script language="javascript">
	function deleteCheck() {
		var form = document.deleteform;

		if (!form.password.value) {
			alert("비밀번호를 적어주세요");
			form.password.focus();
			return;
		}
		form.submit();
	}
</script>
</html>