<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<!-- icon link -->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css"/>
<head>
<style>
body {
	margin: 0;
	padding: 0;
}
.btn-big {
	padding: .7rem 1.3rem;
	line-height: 1.3rem;
}
.footer {
	background: #303036;
	color: #d3d3d3;
	height: 400px;
	position: relative; 
}
.footer .footer-content { /*3단락으로 구분됨*/
	/* border : 1px solid red; */
	height: 350px;
	display: flex;
}

.footer .footer-content .footer-section {
	flex: 1;
	padding: 25px;
	/* border: 1px solid white; */
}
.footer .footer-content h1,
.footer .footer-content h2 {
	color: white;	
}
.footer .footer-content .about h1 span {
	color: ##05f7ff;
}
.footer .footer-content .about .contact span {
	display: block;
	font-size: 1.1em;
	margin-bottom: 8px; /*Awalnspires 아이콘 내 간격 넓어짐*/
}
.footer .footer-content .about .socials a {
	border: 1px solid grey;
	width: 45px;
	height: 41px;
	padding-top: 5px;
	margin-right: 5px;
	text-align: center;
	display: inline-block;
	font-size: 1.3em;
	border-radius: 5px;
	transition: all .3s;
}
.footer .footer-content .about .socials a:hover {
	border: 1px solid white;
	color: white;
	transition: all .3s;
}
.footer .footer-content .links ul a {
	display: block;
	margin-bottom : 10px;
	font-size: 1.2em;
	transition: all .3s;
}
.footer .footer-content .links ul a:hover {
	color: white;
	margin-left: 15px;
	transition: all .3s;
}
.footer .footer-content .contact-form .contact-input{ /*contact us 속성 부분*/
	background: #272727;
	color: ##bebdbd;
	margin-bottom: 10px;
	line-height: 1.5rem;
	padding: .9rem 1.4rem;
	border: none;
	
}


.footer .footer-content .contact-form .contact-input: focus {
	background: #1a1a1a;
}

.footer .footer-content .contact-form .contact-btn {
	float:right;
}

.footer .footer-bottom {
	background: #303036;
	color: #686868;
	height: 50px;
	width: 100%; /*중앙배치됨*/
	text-align: center;
	position: absolute; 
	bottom: 0px;
	left: 0px;
	padding-top: 20px;
}
</style>
<meta charset="UTF-8">
<title>footer</title>
</head>
<body>
<div class="footer">
	<div class="footer-content">
		<div class="footer-section about">
			<h1 class="logo-text"><span>Awa</span>Inspires</h1>
			<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
			ut labore et dolore magna aliqua.
			</p>
			<div class="contact">
				<span><i class="fas fa-phone"></i>&nbsp; 123-456-789</span>
				<span><i class="fas fa-envelope"></i>&nbsp; info@travel.com</span>
			</div>
			<div class="socials">
				<a href="#"><i class="fab fa-facebook"></i></a>
				<a href="#"><i class="fab fa-instagram"></i></a>
				<a href="#"><i class="fab fa-twitter"></i></a>
				<a href="#"><i class="fab fa-youtube"></i></a>
			</div>
		</div>
		<div class="footer-section links">
			<h2>Quick Links</h2>
			<br>
			<ul>
				<a href="#"><li>Event</li></a>
				<a href="#"><li>Team</li></a>
				<a href="#"><li>Member</li></a>
			</ul>
		</div>
		<div class="footer-section contact-form">
			<h2>Contact us</h2>
			<br>
			<form action="index.html" method="post">
				<input type="email" name="email" class="text-input contact-input" placeholder="Your email Address....">
				<textarea name="message" class="text-input contact-input"  placeholder="Your Message..."></textarea>
				<button type="submit" class="btn btn-big contact-btn">
					<i class="fas fa-envelope"></i>
					Send
				</button>
			</form>
		</div>	
	</div>
	<div class="footer-bottom">
	&copy; codingpoets.com | Desinged by Awa Melvine 
	</div>
</div>
</body>
</html>