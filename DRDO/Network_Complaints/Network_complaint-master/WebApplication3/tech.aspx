<%@ Page Language="C#" AutoEventWireup="true" CodeFile="tech.aspx.cs" Inherits="WebApplication3.tech" %>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Technician Page</title>
<style>
    body {
        background: linear-gradient(90deg, #89f7fe 0%, #66a6ff 50%);
        font-family: Arial, sans-serif;
    }

    .glass-container input[type="text"],
    .glass-container input[type="password"] {
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: #000;
        padding: 10px 15px;
        font-size: 1rem;
        border-radius: 12px;
        outline: none;
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        box-shadow: inset 0 0 10px rgba(255, 255, 255, 0.2);
        width: 200px;
    }

    .glass-container input[type="text"]:focus,
    .glass-container input[type="password"]:focus {
        border-color: rgba(255, 255, 255, 0.7);
        box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);
        background: rgba(255, 255, 255, 0.25);
        color: #111;
    }

    .glass-container button,
    .glass-container input[type="submit"],
    .glass-container input[type="button"] {
        background: rgba(255, 255, 255, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.4);
        color: #000;
        padding: 10px 20px;
        font-weight: 600;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.25);
    }

    .glass-container button:hover,
    .glass-container input[type="submit"]:hover,
    .glass-container input[type="button"]:hover {
        background: rgba(255, 255, 255, 0.4);
        box-shadow: 0 6px 20px rgba(255, 255, 255, 0.4);
        color: #111;
    }

    .glass-button {
        background: rgba(255, 255, 255, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.4);
        color: #000;
        padding: 10px 20px;
        font-weight: 600;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.25);
        margin-left: 10px;
    }

    .glass-button:hover {
        background: rgba(255, 255, 255, 0.4);
        box-shadow: 0 6px 20px rgba(255, 255, 255, 0.4);
        color: #111;
    }

    .glass-container {
        max-width: 1400px;
        margin: 40px auto;
        padding: 30px 40px;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        color: #000;
        overflow-x: auto;
    }

    .greeting-label {
        display: block;
        font-size: 26px;
        font-weight: bold;
        padding: 12px 20px;
        margin-bottom: 25px;
        text-align: center;
        width: 100%;
    }

    .styled-gridview {
        width: 100%;
        table-layout: auto;
        border-collapse: collapse;
        white-space: nowrap;
    }
   table {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
}

table td, table th {
    word-wrap: break-word;
    white-space: normal;
    max-width: 200px; /* You can adjust as needed */
    padding: 10px;
}

    .styled-gridview th,
    .styled-gridview td {
        text-align: center;
        vertical-align: middle;
        padding: 12px 16px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        border: 1px solid rgba(255, 255, 255, 0.25);
        color: #000;
    }
       .gvWrap {
        width: 100%;
        overflow-x: auto;
    }

    .gvWrap table {
        width: 100%;
        border-collapse: collapse;
        table-layout: auto; /* Use 'auto' instead of 'fixed' */
    }

    .gvWrap th, .gvWrap td {
        padding: 8px 12px;
        text-align: left;
        vertical-align: top;
        white-space: normal;
        word-break: break-word;
        max-width: 200px; /* Prevent overly wide columns */
    }

.responsive-gridview {
    width: 100%;
    table-layout: auto; /* Let table auto-resize based on content */
    border-collapse: collapse;
    word-wrap: break-word;
}

.responsive-gridview td, .responsive-gridview th {
    padding: 10px;
    vertical-align: top;
    word-break: break-word; /* Wrap long words */
    white-space: normal;    /* Allows multi-line content */
}

    .styled-gridview th {
        background-color: rgba(255, 255, 255, 0.3);
    }

    .styled-gridview tr:nth-child(even) {
        background-color: rgba(255, 255, 255, 0.1);
    }

    table td:nth-child(8),
    table th:nth-child(8) {
        max-width: 200px;
        word-wrap: break-word;
        white-space: normal;
        overflow-wrap: break-word;
    }

    .editing-row {
        background-color: #ffffcc !important;
    }

    #lblTechStatus {
        display: block;
        margin-top: 15px;
        font-size: 1.1rem;
        color: #d8000c;
    }

    /* Button styles for Edit/Update/Cancel */
    .cmd-button {
        background: rgba(255, 255, 255, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.4);
        color: #000;
        padding: 6px 12px;
        font-weight: 600;
        border-radius: 8px;
        cursor: pointer;
        margin: 2px 0;
        display: inline-block;
        transition: all 0.3s ease;
        text-decoration: none;
    }

    .cmd-button:hover {
        background: rgba(255, 255, 255, 0.4);
        color: #111;
    }

    /* Update button - light blue background */
    .btn-update {
        background-color: #ADD8E6; /* light blue */
        color: #000; /* black text */
        border: 1px solid #7FB8D5;
    }

    .btn-update:hover {
        background-color: #90c5e3;
    }

    /* Cancel button - light blue background */
    .btn-cancel {
        background-color: #ADD8E6; /* light blue */
        color: #000; /* black text */
        border: 1px solid #7FB8D5;
    }

    .btn-cancel:hover {
        background-color: #90c5e3;
    }
</style>

</head>
<body>
<form id="form1" runat="server">
    <asp:Button ID="btnBack" runat="server" Text="Back to Dashboard" CssClass="glass-button" OnClick="btnBack_Click" />
    
    <div class="glass-container">
        <asp:Label ID="lblGreeting" runat="server" CssClass="greeting-label" Text="Technician Dashboard" />

        Tech ID:
        <asp:TextBox ID="txtTechID" runat="server" />
        Password:
        <asp:TextBox ID="txtTechPwd" runat="server" TextMode="Password" />
        <asp:Button ID="btnTechLogin" runat="server" Text="Login" CssClass="glass-button" OnClick="btnTechLogin_Click" />
        
        <br /><br />
        <asp:Label ID="lblTechStatus" runat="server" />
        <div class="gvWrap">

           <asp:GridView ID="gvTechRequests" runat="server" AutoGenerateColumns="False" DataKeyNames="sno"
                CssClass="styled-gridview"
                OnRowEditing="gvTechRequests_RowEditing"
                OnRowCancelingEdit="gvTechRequests_RowCancelingEdit"
                OnRowUpdating="gvTechRequests_RowUpdating"
                OnRowDataBound="gvTechRequests_RowDataBound">
                <Columns>
                    <asp:BoundField DataField="Name" HeaderText="Name" ReadOnly="True" />
                    <asp:BoundField DataField="Priority" HeaderText="Priority" ReadOnly="True" />
                    <asp:BoundField DataField="Description" HeaderText="Description" ReadOnly="True" />
                    <asp:BoundField DataField="Completed_date" HeaderText="Completed Date" 
                        DataFormatString="{0:yyyy-MM-dd HH:mm}" HtmlEncode="false" ReadOnly="True" />

                    <asp:TemplateField HeaderText="Remark">
                        <ItemTemplate>
                            <%# Eval("remark") %>
                        </ItemTemplate>
                        <EditItemTemplate>
                            <asp:TextBox ID="txtRemark" runat="server" Text='<%# Bind("remark") %>' Width="150px" />
                        </EditItemTemplate>
                    </asp:TemplateField>

                    <asp:TemplateField HeaderText="Spare Parts">
                        <ItemTemplate>
                            <%# Eval("spareparts_replaced") %>
                        </ItemTemplate>
                        <EditItemTemplate>
                            <asp:TextBox ID="txtSpareParts" runat="server" Text='<%# Bind("spareparts_replaced") %>' Width="150px" />
                        </EditItemTemplate>
                    </asp:TemplateField>

                    <asp:TemplateField HeaderText="Actions" ItemStyle-HorizontalAlign="Center" ItemStyle-Width="90px">
                        <ItemTemplate>
                            <asp:LinkButton ID="lnkEdit" runat="server" CommandName="Edit" CssClass="cmd-button">Edit</asp:LinkButton>
                        </ItemTemplate>
                        <EditItemTemplate>
                            <asp:LinkButton ID="lnkUpdate" runat="server" CommandName="Update" CssClass="cmd-button btn-update">Update</asp:LinkButton><br />
                            <asp:LinkButton ID="lnkCancel" runat="server" CommandName="Cancel" CssClass="cmd-button btn-cancel" CausesValidation="false">Cancel</asp:LinkButton>
                        </EditItemTemplate>
                    </asp:TemplateField>
                </Columns>
            </asp:GridView>

        </div>
    </div>
</form>
</body>
</html>
