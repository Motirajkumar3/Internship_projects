<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Welcome.aspx.cs" Inherits="WebApplication3.Welcome" %>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Welcome</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
            background-color: #f2f2f2;
            padding-top: 80px;
        }

        h1 {
            color: #333;
        }

        .service-img {
            width: 200px;
            height: auto;
            margin-top: 30px;
            cursor: pointer;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            transition: transform 0.2s;
        }

        .service-img:hover {
            transform: scale(1.05);
        }

        p {
            font-size: 18px;
            color: #555;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <h1>Welcome to the IT Service Complaint Portal</h1>
        <p>Click below to proceed to the Complaint Form</p>

        <a href="Default.aspx">
            click here
        </a>
    </form>
</body>
</html>
