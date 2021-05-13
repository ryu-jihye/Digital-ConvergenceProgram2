<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
<jsp:include page="../includes/header.jsp" />

 <script type="text/javascript">
      $(document).ready(function() {
         var operForm = $("#operForm");
         $('button[data-oper="modify"]').on("click", function(e) {
        	 alert("수정 중");
        	 console.log("수정중");
            operForm.attr("action", "/board/modify").submit();
         });
         $('button[data-oper="list"]').on("click", function(e) {
        	 alert("목록으로");
        	 console.log("목록으로");
            operForm.find("#bno").remove();
            operForm.attr("action", "/board/list");
            operForm.submit();
         });
      });
   </script>

<!--header ------------------------------------------ -->
<div class="row">
	<div class="col-lg-12">
		<h1 class="page-header">Tables</h1>
	</div>
	<!-- /.col-lg-12 -->
</div>
<!-- /.row -->
<div class="row">
   <div class="col-lg-12">
      <div class="panel panel-default">
         <div class="panel-heading">Board Modify</div>
         <!-- /.panel-heading -->
         <div class="panel-body">
            
               <div class="form-group">
                  <label>Bno</label><input class="form-control" name="bno"
                     value="<c:out value='${board.bno}'/>" readonly="readonly">
               </div>
               <div class="form-group">
                  <label>Title</label><input class="form-control" name="title"
                     value="<c:out value='${board.title}'/>" readonly="readonly">
               </div>
               <div class="form-group">
                  <label>Content</label>
                  <textarea class="form-control" rows="3" name="content" readonly="readonly">${board.content}</textarea>
               </div>
               <div class="form-group">
                  <label>Writer</label><input class="form-control" name="writer"
                     value="<c:out value='${board.writer}'/>" readonly="readonly">
               </div>
					<button data-oper='modify' class="btn btn-warning">Modify</button>
					<button data-oper='list' class="btn btn-success">List</button>
					<form id="operForm" action="/board/modify" method="get">
						<input type='hidden' id='bno' name='bno'	
						value='<c:out value="${board.bno}"/>'>
					</form>

				<!-- /.table-responsive -->
			</div>
			<!-- /.panel-body -->
		</div>
		<!-- /.panel -->
	</div>
	<!-- /.col-lg-12 -->
</div>
<!-- /.row -->

<!--footer ---------------------------------------- -->

<jsp:include page="../includes/footer.jsp" />