<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="utf-8"%>
<%@page import="java.text.SimpleDateFormat"%>
<%@ page import="java.sql.*"%>  
<%@ page import="java.util.Date" %>

 <%
	request.setCharacterEncoding("UTF-8");	
 	String url = "jdbc:oracle:thin:@localhost:1521:xe";
	String id = "scott";
	String pw = "tiger";
	
	Class.forName("oracle.jdbc.driver.OracleDriver");
	String title = "";
	int idx = Integer.parseInt(request.getParameter("idx"));
	
	try {
		
		
		Connection conn = DriverManager.getConnection(url,id,pw);
		Statement stmt = conn.createStatement();

		
		String sql = "SELECT TITLE FROM inquiry WHERE IQNO=" + idx;
		ResultSet rs = stmt.executeQuery(sql);

 		if(rs.next()){
			title = rs.getString(1);
 		}
			
	rs.close();
	stmt.close();
	conn.close();
 	
} catch(SQLException e) {

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
h3 {text-align: center; color:white;}
h4 {text-align: left; color:black;}
.container{padding-top: 100px; padding-bottom: 30px;}
.tacontent{width:550px; height:100px; padding:8px; border-radius: 5px;}

input[type=text], input[type=password], textarea{
width:550px; height:30px;
border: none;  font-size: 18px;
background-color:white;}
input[type=submit]{
width:563px; height:40px;
border: none;  font-size: 18px;}
.ip{
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

.sm>input{
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 18px;
	background-color: white;
	border-radius: 5px;
}

.sm>input:hover {background-color: black;}
table{width:980px;}
#order{padding-top:15px; padding-bottom:15px;}
.container{padding-top: 100px; padding-bottom: 30px;}
input[readonly]{background-color: #E3DCAC}
.content{padding-top: 20px; padding-bottom:20px;}
.ip {padding-top: 30px; }
.sm {padding-top: 20px;}
.aleft{padding-right:20px;}
.aright{padding-left:20px;}
.tacontent{width:550px; height:100px; padding:8px; border-radius: 5px;}
h1{text-align: center; color:white;}
h3{text-align: left; color:white;}
div1{float:left;}
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
 <title>답글 페이지(관리자용)</title>
<jsp:include page="../menu.jsp"/>
 <br>
 <br>
 <br>
 <br>
  <h1>답글 페이지(관리자용)</h1>
 </head>
 <body>
  <%
 	SimpleDateFormat sdformat = new SimpleDateFormat("yyyy-MM-dd");
 	Date time = new Date();
 	String iqdate = sdformat.format(time);
 %>
<table>
<form name=replyform method=post action="nreplyProc.jsp?idx=<%=idx%>">
  <tr>
   <td>
    <table width="100%" cellpadding="0" cellspacing="0" border="0">
    </table>
   <table>
     <tr>
     <div class="ip">
		<h3>제목</h3><input type="text" name="title" value = "[관리자 답변]:">
	</div>
     <div class="ip">
		<h3>이름</h3><input type="text" name="userid" value = "관리자" readonly>
	</div>
	 <div class="ip">
		<h3>비밀번호</h3><input type="text" name="password">
	</div>
	 <div class="ip">
		<h3>작성날짜</h3><input type="text" name="iqdate" value=<%=iqdate %> readonly>
	</div>
    <div class="ip">
		<h3>내용</h3><input type=text name="content">
	</div>
		<input type=button value="취소" OnClick="javascript:history.back(-1)" class="faqButton">
       <input type=button value="등록"  OnClick="javascript:replyCheck();" class="faqButton">
    </table>
   </td>
  </tr>
 </table>
</body> 
<script language = "javascript">
function replyCheck()
  {
   var form = document.replyform;
   if( !form.password.value )
   {
    alert( "비밀번호를 적어주세요" );
    form.password.focus();
    return;
   }
   
  if( !form.title.value )
   {
    alert( "제목을 적어주세요" );
    form.title.focus();
    return;
   }
 
  if( !form.content.value )
   {
    alert( "내용을 적어주세요" );
    form.memo.focus();
    return;
   }
 
  form.submit();
  }
 </script>
</html>
