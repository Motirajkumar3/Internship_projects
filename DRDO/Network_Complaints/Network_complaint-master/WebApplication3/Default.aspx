<%@ Page Title="Service Request Form" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="front._Default" %>

<asp:Content ID="MainContent" ContentPlaceHolderID="MainContent" runat="server">
  <style>
      body {
          background-image:url("https://wallpapercave.com/wp/wp2003027.jpg");
          background-repeat:no-repeat;
          background-size:cover;
          
      }
    .form-container {

        max-width: 640px;
        background: transparent;
        backdrop-filter:blur(10px);
        padding: 30px 35px;
        border-radius: 10px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.5);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 40px auto;
        border: 1px solid ;
       
    }

    h2 {
        text-align: center;
        color: rgba(0,0,0,1);
        margin-bottom: 30px;
        font-size: 50px;
        font-weight: bold;
       
    }

    .form-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0 18px;
        margin: 0 auto;
    }

    .form-label {
        font-weight: bolder;
        font-size:larger;
        padding-right:10px;
        vertical-align: middle;
        color: rgb(0,0,0);
        width: 160px;
        white-space: nowrap;
    }
    .fetch-button {
    background-color: rgb(225, 111, 45, 0.85);
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 15px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    backdrop-filter: blur(4px);
    margin-right: 10px; /* optional spacing */
}

.fetch-button:hover {
    background-color: rgb(231, 144, 33, 0.90);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.2);
}


    td > input[type="text"],
td > textarea,
td > select,
td > input[type="tel"],
td > .aspNetDisabled {
    width: 100%;
    color:black;
    padding: 10px 12px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 6px;
    font-size: 15px;
    font-family: sans-serif;
    background-color: rgb(141, 134, 134, 0.39);
    backdrop-filter: blur(5px);
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}


    td > input[type="text"]:focus,
    td > textarea:focus,
    td > select:focus,
    td > input[type="tel"]:focus {
        border-color: #3498db;
        box-shadow: 0 0 8px rgba(52, 152, 219, 0.4);
        outline: none;
    }

    textarea {
        resize: vertical;
    }

    tr:last-child td {
        padding-top: 20px;
    }

   .form-buttons asp\:button,
.form-buttons input[type="submit"],
.form-buttons input[type="button"] {
    background-color: rgba(0, 120, 0, 0.85); /* Blue with transparency */
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 15px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    backdrop-filter: blur(4px);
}

.form-buttons asp\:button:hover,
.form-buttons input[type="submit"]:hover,
.form-buttons input[type="button"]:hover {
    background-color: rgba(0, 90, 180, 0.9);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.2);
}

asp\:button[Text="Clear Form"],
input[type="button"].clear-button {
    background-color: rgba(108, 117, 125, 0.75); /* Gray for clear button */
}

asp\:button[Text="Clear Form"]:hover,
input[type="button"].clear-button:hover {
    background-color: rgba(73, 80, 87, 0.85);
}
/* Stylize GridView output table */
.gridview-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    background-color: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    color: white;
    font-size: 15px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.4);
    border-radius: 10px;
    overflow: hidden;
}

/* Header */
.gridview-table th {
    background-color: rgba(255, 215, 0, 0.9); /* gold shade */
    color: black;
    font-weight: bold;
    padding: 10px 12px;
    border-bottom: 2px solid rgba(0, 0, 0, 0.2);
    text-align: left;
}

/* Rows */
.gridview-table td {
    padding: 10px 12px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
}

/* Alternate row background */
.gridview-table tr:nth-child(even) {
    background-color: rgba(255, 255, 255, 0.07);
}

/* Hover effect */
.gridview-table tr:hover {
    background-color: rgba(255, 255, 255, 0.2);
    transition: background-color 0.3s ease;
}
.table-wrapper {
    overflow-x: auto;
    max-width: 100%;
    margin-top: 20px;
    border-radius: 10px;
}

.gridview-table {
    width: 100%;
    min-width: 800px; /* Ensures wide content fits */
    
    border-collapse: collapse;
    background-color: rgba(255, 255, 255,0.7);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    color: black;
    font-weight:bold;
    font-size: 15px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.4);
}
.admin-button {
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    border: none;
    padding: 10px 18px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 15px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(4px);
}

.admin-button:hover {
    background-color: rgba(255, 193, 7, 0.9); /* Warm yellow on hover */
    color: #000;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.4);
}



/* The rest of your existing styles... */




  </style>

  <div class="form-container">
      <div style="display: flex; justify-content: flex-end;">
    <asp:Button ID="btnAdmin" runat="server" Text="Admin Panel" CssClass="admin-button" OnClick="btnAdmin_Click" />
         <asp:Button ID="btnTechnician" runat="server" Text="Technician Panel"
    CssClass="admin-button" PostBackUrl="~/tech.aspx" />


</div>

    <h2>Service Request Form</h2>
    <asp:Panel ID="pnlForm" runat="server">
        <table class="form-table">
     <tr>
     <td class="form-label">Employee ID:</td>
     <td><asp:TextBox ID="txtEmployeeID" runat="server" /> <asp:Button ID="btnFetch" runat="server" Text="Fetch" CssClass="fetch-button" OnClick="btnFetch_Click" />
</td>
       </tr>  
          


            <tr>
                <td class="form-label">Name:</td>
                <td><asp:TextBox ID="txtFirstName" runat="server" /></td>
            </tr>
           
            <tr>
                <td class="form-label">Division:</td>
                <td>
                    <asp:DropDownList ID="ddlDepartment" runat="server">
                        <asp:ListItem Text="-- Select --" Value="" />
                        <asp:ListItem Text="IT" Value="it" />
                        <asp:ListItem Text="HR" Value="hr" />
                        <asp:ListItem Text="Finance" Value="Finance" />
                        <asp:ListItem Text="Operations" Value="Operations" />
                    </asp:DropDownList>
                </td>
            </tr>
              <tr>
      <td class="form-label">Designation:</td>
      <td>
     <asp:DropDownList ID="ddlDesignation" runat="server">
    <asp:ListItem Text="-- Select --" Value="" />
    <asp:ListItem Text="Maintenance" Value="Maintenance" />
    <asp:ListItem Text="Technical Support" Value="Technical Support" />
</asp:DropDownList>


      </td>
  </tr>
            <tr>
                <td class="form-label">Phone Number:</td>
                <td><asp:TextBox ID="txtPhone" runat="server" /></td>
            </tr>
          
            <tr>
                <td class="form-label">Description:</td>
                <td><asp:TextBox ID="txtDescription" runat="server" TextMode="MultiLine" Rows="4" Columns="40" /></td>
            </tr>
            <tr>
                <td></td>
                <td class="form-buttons">
                    <asp:Button ID="btnSubmit" runat="server" Text="Submit" OnClick="btnSubmit_Click" />
                    <asp:Button ID="btnClear" runat="server" Text="Clear Form" OnClick="btnClear_Click" CausesValidation="False" />
                   

                </td>
                <asp:Label ID="lblStatus" runat="server" Font-Bold="True" />

            </tr>
        </table>
        <asp:Panel ID="pnlAdmin" runat="server" Visible="false" style="margin-top: 20px;">
    <asp:Label ID="lblAdminPrompt" runat="server" Text="Enter Employee ID:" Font-Bold="true" />
    <asp:TextBox ID="txtAdminEmpID" runat="server" />
    <asp:Button ID="btnCheckAdmin" runat="server" Text="Check Access" OnClick="btnCheckAdmin_Click" CssClass="fetch-button" />

    <br /><br />
    <asp:Label ID="lblAdminStatus" runat="server" Font-Bold="true" />

   <div class="table-wrapper">
    <asp:GridView ID="gvServiceRequests" runat="server" AutoGenerateColumns="true"
        CssClass="gridview-table" Visible="false">
    </asp:GridView>
</div>


</asp:Panel>

    </asp:Panel>
  </div>
    </asp:Content>