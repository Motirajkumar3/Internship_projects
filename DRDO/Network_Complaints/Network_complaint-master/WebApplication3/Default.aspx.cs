using System;
using System.Configuration;
using System.Data.SqlClient;
using System.Web.UI.WebControls;

namespace front
{
    public partial class _Default : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                BindEmployeeDropdown();
            }
        }

        private void BindEmployeeDropdown()
        {
            string connectionString = "your_connection_string_here";
            string query = "SELECT empNo, empName FROM emp";

            using (SqlConnection con = new SqlConnection(connectionString))
            {
                using (SqlCommand cmd = new SqlCommand(query, con))
                {
                    con.Open();
                    SqlDataReader reader = cmd.ExecuteReader();
                    ddlEmployeeID.DataSource = reader;
                    ddlEmployeeID.DataTextField = "empNo";   // What the user will see
                    ddlEmployeeID.DataValueField = "empNo";  // The value submitted
                    ddlEmployeeID.DataBind();
                    con.Close();
                }
            }

            // Optional: Insert a default "Select" option at the top
            ddlEmployeeID.Items.Insert(0, new ListItem("-- Select Employee ID --", ""));
        }


        protected void btnFetch_Click(object sender, EventArgs e)
        {
            string connStr = ConfigurationManager.ConnectionStrings["ServiceRequestsDBConnection"].ConnectionString;

            using (SqlConnection conn = new SqlConnection(connStr))
            {
                string query = "SELECT empName, Division, phoneNo, designation FROM emp WHERE empNo = @empNo";

                SqlCommand cmd = new SqlCommand(query, conn);
                cmd.Parameters.AddWithValue("@empNo", txtEmployeeID.Text.Trim());

                try
                {
                    conn.Open();
                    SqlDataReader reader = cmd.ExecuteReader();
                    if (reader.Read())
                    {
                        txtFirstName.Text = reader["empName"].ToString();
                        ddlDepartment.SelectedValue = reader["Division"].ToString();
                        txtPhone.Text = reader["phoneNo"].ToString();

                        string designation = reader["Designation"].ToString().Trim();



                        if (ddlDesignation.Items.FindByValue(designation) != null)
                        {
                            ddlDesignation.SelectedValue = designation;
                        }
                        else
                        {
                            ddlDesignation.ClearSelection();
                            lblStatus.Text = $"⚠️ Designation '{designation}' not found in dropdown.";
                            lblStatus.ForeColor = System.Drawing.Color.OrangeRed;
                        }

                    }
                    else
                    {
                        lblStatus.Text = "⚠️ Employee not found.";
                        lblStatus.ForeColor = System.Drawing.Color.OrangeRed;
                    }
                }
                catch (Exception ex)
                {
                    lblStatus.Text = "❌ Error: " + ex.Message;
                    lblStatus.ForeColor = System.Drawing.Color.Red;
                }
            }
        }



        protected void btnSubmit_Click(object sender, EventArgs e)
        {
            // Server-side validation for empty fields
            if (string.IsNullOrWhiteSpace(txtFirstName.Text) ||
                string.IsNullOrWhiteSpace(txtEmployeeID.Text) ||
                string.IsNullOrWhiteSpace(txtPhone.Text) ||
                string.IsNullOrWhiteSpace(txtDescription.Text) ||
                string.IsNullOrEmpty(ddlDepartment.SelectedValue) ||
                string.IsNullOrEmpty(ddlDesignation.SelectedValue))
            {
                lblStatus.Text = "⚠️ Please fill in all fields before submitting.";
                lblStatus.ForeColor = System.Drawing.Color.OrangeRed;
                return;
            }

            string connectionString = ConfigurationManager.ConnectionStrings["ServiceRequestsDBConnection"].ConnectionString;

            using (SqlConnection conn = new SqlConnection(connectionString))
            {
                string query = @"INSERT INTO ServiceRequests 
                         (Name, EmployeeID, Department, PhoneNumber, ServiceType, Description, SubmittedOn)
                         VALUES 
                         (@Name, @EmployeeID, @Department, @PhoneNumber, @ServiceType, @Description, @SubmittedOn)";

                using (SqlCommand cmd = new SqlCommand(query, conn))
                {
                    cmd.Parameters.AddWithValue("@Name", txtFirstName.Text);
                    cmd.Parameters.AddWithValue("@EmployeeID", txtEmployeeID.Text);
                    cmd.Parameters.AddWithValue("@Department", ddlDepartment.SelectedValue);
                    cmd.Parameters.AddWithValue("@PhoneNumber", txtPhone.Text);
                    cmd.Parameters.AddWithValue("@ServiceType", ddlDesignation.SelectedValue);
                    cmd.Parameters.AddWithValue("@Description", txtDescription.Text);
                    cmd.Parameters.AddWithValue("@SubmittedOn", DateTime.Now);

                    try
                    {
                        conn.Open();
                        cmd.ExecuteNonQuery();

                        lblStatus.ForeColor = System.Drawing.Color.Green;
                        lblStatus.Text = "✔️ Your request has been submitted successfully!";
                        ClearForm();
                    }
                    catch (Exception ex)
                    {
                        lblStatus.ForeColor = System.Drawing.Color.Red;
                        lblStatus.Text = "❌ Error saving data: " + ex.Message;
                    }
                }
            }
        }



        protected void btnAdmin_Click(object sender, EventArgs e)
        {
            Response.Redirect("admin.aspx");
            pnlAdmin.Visible = true;
            
        }

        protected void btnCheckAdmin_Click(object sender, EventArgs e)
        {
            string empId = txtAdminEmpID.Text.Trim();

            if (string.IsNullOrEmpty(empId))
            {
                lblAdminStatus.Text = "⚠️ Please enter an Employee ID.";
                lblAdminStatus.ForeColor = System.Drawing.Color.OrangeRed;
                return;
            }

            string connStr = ConfigurationManager.ConnectionStrings["ServiceRequestsDBConnection"].ConnectionString;

            using (SqlConnection conn = new SqlConnection(connStr))
            {
                string query = "SELECT admin FROM emp WHERE empNo = @empNo";
                SqlCommand cmd = new SqlCommand(query, conn);
                cmd.Parameters.AddWithValue("@empNo", empId);

                try
                {
                    conn.Open();
                    object result = cmd.ExecuteScalar();

                    if (result != null && result.ToString().ToLower() == "a")
                    {
                        ShowServiceRequests(conn);
                    }
                    else
                    {
                        lblAdminStatus.Text = "🚫 No Access: You are not an admin.";
                        lblAdminStatus.ForeColor = System.Drawing.Color.Red;
                        gvServiceRequests.Visible = false;
                    }
                }
                catch (Exception ex)
                {
                    lblAdminStatus.Text = "❌ Error: " + ex.Message;
                    lblAdminStatus.ForeColor = System.Drawing.Color.Red;
                }
            }
        }

        private void ShowServiceRequests(SqlConnection conn)
        {
            string query = "SELECT * FROM ServiceRequests";
            SqlCommand cmd = new SqlCommand(query, conn);
            SqlDataReader reader = cmd.ExecuteReader();

            System.Data.DataTable dt = new System.Data.DataTable();
            dt.Load(reader);

            gvServiceRequests.DataSource = dt;
            gvServiceRequests.DataBind();

            gvServiceRequests.Visible = true;
            lblAdminStatus.Text = "✅ Access granted. Displaying all service requests:";
            lblAdminStatus.ForeColor = System.Drawing.Color.Green;
        }








        protected void btnClear_Click(object sender, EventArgs e)
        {
            ClearForm();
            lblStatus.Text = "";
        }

        private void ClearForm()
        {
            txtEmployeeID.Text = "";
            txtFirstName.Text = "";
            ddlDepartment.SelectedIndex = 0;
            txtPhone.Text = "";
            ddlDesignation.SelectedIndex = 0;
            txtDescription.Text = "";
        }

    }
}