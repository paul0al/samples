<%@ page import="sample.User" %>

<html>
	<head>
		<title>Hi Paul</title>
	</head>

	<body>
		Hi Paul...
		
		<%
			User user = new User("xxxx");
			user.debug();
		%>
	</body>
</html>