<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="admin.aspx.cs" Inherits="WebApplication3.admin" %>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Admin Access</title>
    <style>
        body {
            margin: 0;
            background: linear-gradient(110deg, #89f7fe 0%, #66a6ff 100%);
            font-family: Arial, sans-serif;
        }
        .glass-container {
            width: 100%;
            margin: 0;
            padding: 0;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 0;
            color: #000;
            overflow-x: auto;
        }
        .glass-container input[type="text"],
        .glass-container input[type="password"] {
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #000;
            padding: 6px 10px;
            font-size: 0.95rem;
            border-radius: 8px;
            width: 180px;
        }
        .glass-container button,
        .glass-container input[type="submit"],
        .glass-container input[type="button"],
        .glass-button {
            background: rgba(255, 255, 255, 0.25);
            border: 1px solid rgba(255, 255, 255, 0.4);
            color: #000;
            padding: 6px 12px;
            font-weight: 600;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 4px;
        }
        .glass-container button:hover,
        .glass-button:hover {
            background: rgba(255, 255, 255, 0.4);
            box-shadow: 0 4px 10px rgba(255, 255, 255, 0.4);
            color: #111;
        }
        .greeting-label {
            display: block;
            font-size: 20px;
            font-weight: bold;
            padding: 10px;
            text-align: center;
        }
        .styled-gridview {
            width: 100%;
            border-collapse: collapse;
            white-space: normal;
        }
        .styled-gridview th,
        .styled-gridview td {
            border: 1px solid rgba(255, 255, 255, 0.25);
            padding: 4px 6px;
            text-align: center;
            vertical-align: middle;
            color: #000;
            white-space: normal;
            word-wrap: break-word;
            overflow-wrap: break-word;
            max-width: 150px;
        }
        .styled-gridview th:nth-child(1),
        .styled-gridview td:nth-child(1) {
            width: 40px;
            max-width: 40px;
        }
        .styled-gridview input[type="text"],
        .styled-gridview select {
            background-color: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #000;
            padding: 4px 6px;
            border-radius: 5px;
            font-size: 13px;
            width: 100%;
            box-sizing: border-box;
        }
        .glass-container tr:nth-child(even) {
            background-color: rgba(255, 255, 255, 0.08);
        }
        .cmd-button {
            display: inline-block;
            width: 60px;
            margin: 2px 0;
            padding: 4px 6px;
            background-color: #66a6ff;
            color: white !important;
            border-radius: 6px;
            font-size: 12px;
            font-weight: bold;
            text-align: center;
            cursor: pointer;
            text-decoration: none;
        }
        .cmd-button:hover {
            background-color: #3b75e6;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <asp:Button ID="btnBack" runat="server" Text="Back to Service Request" OnClick="btnBack_Click" CssClass="glass-button" />
        <div class="glass-container">
            <h2 style="text-align:center;">Admin Panel</h2>
            <asp:Label ID="lblGreeting" runat="server" CssClass="greeting-label"></asp:Label>

            <div style="padding: 10px; text-align: center;">
                Enter Employee ID: <asp:TextBox ID="txtEmpID" runat="server" />
                Enter Password: <asp:TextBox ID="txtPassword" TextMode="Password" runat="server" />
                <asp:Button ID="btnLogin" Text="Check Access" runat="server" OnClick="btnLogin_Click" CssClass="glass-button" />
            </div>

            <asp:Label ID="lblAccess" runat="server" /><br />

            <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False"
                OnRowEditing="GridView1_RowEditing"
                OnRowUpdating="GridView1_RowUpdating"
                OnRowCancelingEdit="GridView1_RowCancelingEdit"
                OnRowDataBound="GridView1_RowDataBound"
                CssClass="styled-gridview"
                DataKeyNames="sno">
                <Columns>
                    <asp:BoundField DataField="sno" HeaderText="S.No" ReadOnly="True" />
                    <asp:BoundField DataField="Name" HeaderText="Name" ReadOnly="True" />
                    <asp:BoundField DataField="EmployeeID" HeaderText="Employee ID" ReadOnly="True" />
                    <asp:BoundField DataField="Department" HeaderText="Department" ReadOnly="True" />
                    <asp:BoundField DataField="PhoneNumber" HeaderText="Phone Number" ReadOnly="True" />
                    <asp:BoundField DataField="ServiceType" HeaderText="Service Type" ReadOnly="True" />
                    <asp:BoundField DataField="Description" HeaderText="Description" ReadOnly="True" />
                    <asp:BoundField DataField="SubmittedOn" HeaderText="Submitted On" ReadOnly="True" />
                    <asp:TemplateField HeaderText="Priority">
                        <EditItemTemplate>
                            <asp:DropDownList ID="ddlPriority" runat="server">
                                <asp:ListItem Text="Low" Value="Low" />
                                <asp:ListItem Text="Medium" Value="Medium" />
                                <asp:ListItem Text="High" Value="High" />
                            </asp:DropDownList>
                        </EditItemTemplate>
                        <ItemTemplate>
                            <%# Eval("Priority") %>
                        </ItemTemplate>
                    </asp:TemplateField>
                    <asp:BoundField DataField="remark" HeaderText="Remarks" ReadOnly="True" />
                    <asp:BoundField DataField="spareparts_replaced" HeaderText="Spare parts Replaced" ReadOnly="True" />
                    <asp:BoundField DataField="completed_date" HeaderText="Completed Date" ReadOnly="True" />
                    <asp:TemplateField HeaderText="fully cpmpleted :Yes/No">
                        <EditItemTemplate>
                            <asp:DropDownList ID="ddlCompleted" runat="server">
                                <asp:ListItem Text="NO" Value="No" />
                                <asp:ListItem Text="Yes" Value="Yes" />
                            </asp:DropDownList>
                        </EditItemTemplate>
                        <ItemTemplate>
                            <%# Eval("completed") %>
                        </ItemTemplate>
                    </asp:TemplateField>
                    <asp:TemplateField HeaderText="Actions" ItemStyle-HorizontalAlign="Center" ItemStyle-Width="60px">
                        <ItemTemplate>
                            <asp:LinkButton ID="lnkEdit" runat="server" CommandName="Edit" CssClass="cmd-button">Edit</asp:LinkButton>
                        </ItemTemplate>
                        <EditItemTemplate>
                            <asp:LinkButton ID="lnkUpdate" runat="server" CommandName="Update" CssClass="cmd-button">Update</asp:LinkButton><br />
                            <asp:LinkButton ID="lnkCancel" runat="server" CommandName="Cancel" CssClass="cmd-button" CausesValidation="false">Cancel</asp:LinkButton>
                        </EditItemTemplate>
                    </asp:TemplateField>
                </Columns>
            </asp:GridView>
        </div>
    </form>
</body>
</html>
