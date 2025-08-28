using System;
using System.Configuration;
using System.Data.SqlClient;
using System.Web.UI.WebControls;

namespace WebApplication3
{
    public partial class admin : System.Web.UI.Page
    {
        protected void GridView1_RowEditing(object sender, GridViewEditEventArgs e)
        {
            GridView1.EditIndex = e.NewEditIndex;
            BindGrid(); // Method to rebind data from DB
        }

        protected void GridView1_RowCancelingEdit(object sender, GridViewCancelEditEventArgs e)
        {
            GridView1.EditIndex = -1;
            BindGrid();
        }

        protected void GridView1_RowUpdating(object sender, GridViewUpdateEventArgs e)
        {
            int rowIndex = e.RowIndex;
            GridViewRow row = GridView1.Rows[rowIndex];
            string sno = GridView1.DataKeys[rowIndex].Value.ToString();

            DropDownList ddlPriority = (DropDownList)row.FindControl("ddlPriority");
            DropDownList ddlCompleted = (DropDownList)row.FindControl("ddlCompleted");

            string newPriority = ddlPriority?.SelectedValue ?? "Low";
            string newCompleted = ddlCompleted?.SelectedValue ?? "No";

            string connStr = ConfigurationManager.ConnectionStrings["ServiceRequestsDBConnection"].ConnectionString;

            using (SqlConnection conn = new SqlConnection(connStr))
            {
                conn.Open();

                if (newCompleted == "Yes")
                {
                    // Fetch full record from ServiceRequests
                    string selectQuery = @"SELECT sno, Name, EmployeeID, Department, PhoneNumber, ServiceType, Description,
                                          SubmittedOn, remark, spareparts_replaced
                                   FROM ServiceRequests
                                   WHERE sno = @sno";

                    SqlCommand selectCmd = new SqlCommand(selectQuery, conn);
                    selectCmd.Parameters.AddWithValue("@sno", sno);

                    SqlDataReader reader = selectCmd.ExecuteReader();

                    if (reader.Read())
                    {
                        var name = reader["Name"].ToString();
                        var empId = reader["EmployeeID"].ToString();
                        var dept = reader["Department"].ToString();
                        var phone = reader["PhoneNumber"].ToString();
                        var serviceType = reader["ServiceType"].ToString();
                        var description = reader["Description"].ToString();
                        var submittedOn = Convert.ToDateTime(reader["SubmittedOn"]);
                        var remark = reader["remark"] != DBNull.Value ? reader["remark"].ToString() : "N/A";
                        var spareparts = reader["spareparts_replaced"] != DBNull.Value ? reader["spareparts_replaced"].ToString() : "N/A";
                        reader.Close();

                        string insertQuery = @"INSERT INTO CompletedServiceRequests
                    (sno, Name, EmployeeID, Department, PhoneNumber, ServiceType, Description, SubmittedOn, Priority, remark, spareparts_replaced, completed_date, completed)
                    VALUES
                    (@sno, @Name, @EmployeeID, @Department, @PhoneNumber, @ServiceType, @Description, @SubmittedOn, @Priority, @remark, @spareparts_replaced, @completed_date, @completed)";

                        SqlCommand insertCmd = new SqlCommand(insertQuery, conn);
                        insertCmd.Parameters.AddWithValue("@sno", sno);
                        insertCmd.Parameters.AddWithValue("@Name", name);
                        insertCmd.Parameters.AddWithValue("@EmployeeID", empId);
                        insertCmd.Parameters.AddWithValue("@Department", dept);
                        insertCmd.Parameters.AddWithValue("@PhoneNumber", phone);
                        insertCmd.Parameters.AddWithValue("@ServiceType", serviceType);
                        insertCmd.Parameters.AddWithValue("@Description", description);
                        insertCmd.Parameters.AddWithValue("@SubmittedOn", submittedOn);
                        insertCmd.Parameters.AddWithValue("@Priority", newPriority);
                        insertCmd.Parameters.AddWithValue("@remark", remark);
                        insertCmd.Parameters.AddWithValue("@spareparts_replaced", spareparts);
                        insertCmd.Parameters.AddWithValue("@completed_date", DateTime.Now);
                        insertCmd.Parameters.AddWithValue("@completed", "Yes");

                        insertCmd.ExecuteNonQuery();

                        // Delete original row from ServiceRequests
                        SqlCommand deleteCmd = new SqlCommand("DELETE FROM ServiceRequests WHERE sno = @sno", conn);
                        deleteCmd.Parameters.AddWithValue("@sno", sno);
                        deleteCmd.ExecuteNonQuery();
                    }
                    else
                    {
                        reader.Close();
                        throw new Exception("Could not find record to move.");
                    }
                }
                else
                {
                    // Only update Priority and Completed status
                    string updateQuery = "UPDATE ServiceRequests SET Priority = @Priority, completed = @completed WHERE sno = @sno";
                    SqlCommand updateCmd = new SqlCommand(updateQuery, conn);
                    updateCmd.Parameters.AddWithValue("@Priority", newPriority);
                    updateCmd.Parameters.AddWithValue("@completed", newCompleted);
                    updateCmd.Parameters.AddWithValue("@sno", sno);
                    updateCmd.ExecuteNonQuery();
                }
            }

            GridView1.EditIndex = -1;
            BindGrid();
        }


        private void BindGrid()
        {
            string connStr = ConfigurationManager.ConnectionStrings["ServiceRequestsDBConnection"].ConnectionString;
            using (SqlConnection conn = new SqlConnection(connStr))
            {
                conn.Open();
                string dataQuery = "SELECT sno, Name, EmployeeID, Department, PhoneNumber, ServiceType, Description, SubmittedOn, Priority FROM ServiceRequests";
                SqlCommand dataCmd = new SqlCommand(dataQuery, conn);
                SqlDataReader reader = dataCmd.ExecuteReader();
                GridView1.DataSource = reader;
                GridView1.DataKeyNames = new string[] { "sno" };
                GridView1.DataBind();
                reader.Close();
            }
        }

        protected void btnBack_Click(object sender, EventArgs e)
        {
            Response.Redirect("Default.aspx"); // Replace with your actual form URL
        }

        protected void btnLogin_Click(object sender, EventArgs e)
        {
            string empID = txtEmpID.Text.Trim();
            string password = txtPassword.Text.Trim();

            string connStr = ConfigurationManager.ConnectionStrings["ServiceRequestsDBConnection"].ConnectionString;

            using (SqlConnection conn = new SqlConnection(connStr))
            {
                conn.Open();

                string query = "SELECT COUNT(*) FROM emp WHERE empNo = @empNo AND passworddb = @password AND admin = 'A'";
                SqlCommand cmd = new SqlCommand(query, conn);
                cmd.Parameters.AddWithValue("@empNo", empID);
                cmd.Parameters.AddWithValue("@password", password);

                int count = (int)cmd.ExecuteScalar();

                if (count == 1)
                {
                    lblGreeting.Text = "👋 Welcome, Admin!";
                    lblAccess.Text = "✅ Access granted. Displaying requests:";
                    lblAccess.ForeColor = System.Drawing.Color.Green;
                    BindGrid();




                    string dataQuery = "SELECT sno, Name, EmployeeID, Department, PhoneNumber, ServiceType, Description, SubmittedOn, Priority FROM ServiceRequests";

                    SqlCommand dataCmd = new SqlCommand(dataQuery, conn);


                    SqlDataReader reader = dataCmd.ExecuteReader();

                    GridView1.DataSource = reader;
                    GridView1.DataBind();

                    reader.Close();
                }
                else
                {
                    lblAccess.Text = "❌ Access denied. Invalid credentials.";
                    lblAccess.ForeColor = System.Drawing.Color.Red;
                    GridView1.DataSource = null;
                    GridView1.DataBind();
                }
            }
        }
    }
}
