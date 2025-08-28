using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Web.UI.WebControls;

namespace WebApplication3
{
    public partial class tech : System.Web.UI.Page
    {
        private string connectionString = ConfigurationManager.ConnectionStrings["ServiceRequestsDBConnection"].ConnectionString;

        private DataTable TechData
        {
            get
            {
                if (ViewState["TechData"] == null)
                {
                    DataTable dt = new DataTable();
                    dt.Columns.Add("sno");
                    dt.Columns.Add("Name");
                    dt.Columns.Add("Priority");
                    dt.Columns.Add("Description");
                    dt.Columns.Add("remark");
                    dt.Columns.Add("spareparts_replaced");

                    dt.Rows.Add("1", "Printer", "High", "Not working", "Needs repair", "Cartridge");
                    dt.Rows.Add("2", "Scanner", "Medium", "Slow scan", "Update drivers", "N/A");

                    ViewState["TechData"] = dt;
                }
                return (DataTable)ViewState["TechData"];
            }
            set { ViewState["TechData"] = value; }
        }

        protected void btnTechLogin_Click(object sender, EventArgs e)
        {
            string techId = txtTechID.Text.Trim();
            string password = txtTechPwd.Text.Trim();

            using (SqlConnection con = new SqlConnection(connectionString))
            {
                con.Open();
                string query = "SELECT admin FROM emp WHERE empno = @techID AND passworddb = @password";
                using (SqlCommand cmd = new SqlCommand(query, con))
                {
                    cmd.Parameters.AddWithValue("@techID", techId);
                    cmd.Parameters.AddWithValue("@password", password);

                    var adminRole = cmd.ExecuteScalar();

                    if (adminRole != null && adminRole.ToString() == "T")
                    {
                        lblTechStatus.Text = "Login successful.";
                        gvTechRequests.Visible = true;
                        BindTechRequests();
                    }
                    else
                    {
                        lblTechStatus.Text = "Invalid credentials.";
                        gvTechRequests.Visible = false;
                    }
                }
            }
        }

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                gvTechRequests.Visible = false;
            }
        }

        private void BindTechRequests()
        {
            using (SqlConnection con = new SqlConnection(connectionString))
            {
                string query = @"
            SELECT sno, Name, Priority, Description, Completed_date, remark, spareparts_replaced 
            FROM ServiceRequests 
            WHERE priority IN ('Low', 'Medium', 'High')
            ORDER BY 
                CASE Priority
                    WHEN 'High' THEN 1
                    WHEN 'Medium' THEN 2
                    WHEN 'Low' THEN 3
                    ELSE 4
                END";

                using (SqlCommand cmd = new SqlCommand(query, con))
                {
                    SqlDataAdapter da = new SqlDataAdapter(cmd);
                    DataTable dt = new DataTable();
                    da.Fill(dt);

                    gvTechRequests.DataSource = dt;
                    gvTechRequests.DataBind();
                }
            }
        }



        protected void gvTechRequests_RowEditing(object sender, GridViewEditEventArgs e)
        {
            gvTechRequests.EditIndex = e.NewEditIndex;
            BindTechRequests();
        }

        protected void btnBack_Click(object sender, EventArgs e)
        {
            Response.Redirect("Default.aspx"); // Adjust redirect as needed
        }

        protected void gvTechRequests_RowCancelingEdit(object sender, GridViewCancelEditEventArgs e)
        {
            gvTechRequests.EditIndex = -1;
            BindTechRequests();
        }

        protected void gvTechRequests_RowDataBound(object sender, GridViewRowEventArgs e)
        {
            if (e.Row.RowState.HasFlag(DataControlRowState.Edit))
            {
                e.Row.CssClass = "editing-row";
            }
        }

        protected void gvTechRequests_RowUpdating(object sender, GridViewUpdateEventArgs e)
        {
            int sno = Convert.ToInt32(gvTechRequests.DataKeys[e.RowIndex].Value);
            GridViewRow row = gvTechRequests.Rows[e.RowIndex];

            TextBox txtRemark = (TextBox)row.FindControl("txtRemark");
            TextBox txtSpareParts = (TextBox)row.FindControl("txtSpareParts");

            string remark = txtRemark.Text.Trim();
            string spareParts = txtSpareParts.Text.Trim();

            DateTime? completedDate = null;
            if (!string.IsNullOrEmpty(remark) || !string.IsNullOrEmpty(spareParts))
            {
                completedDate = DateTime.Now;
            }

            string query = @"
                UPDATE ServiceRequests
                SET remark = @remark,
                    spareparts_replaced = @spareparts,
                    Completed_date = @completedDate
                WHERE sno = @sno";

            using (SqlConnection con = new SqlConnection(connectionString))
            {
                using (SqlCommand cmd = new SqlCommand(query, con))
                {
                    cmd.Parameters.AddWithValue("@remark", remark);
                    cmd.Parameters.AddWithValue("@spareparts", spareParts);
                    if (completedDate.HasValue)
                        cmd.Parameters.AddWithValue("@completedDate", completedDate.Value);
                    else
                        cmd.Parameters.AddWithValue("@completedDate", DBNull.Value);

                    cmd.Parameters.AddWithValue("@sno", sno);

                    con.Open();
                    cmd.ExecuteNonQuery();
                }
            }

            gvTechRequests.EditIndex = -1;
            BindTechRequests(); // Rebind updated data
        }
    }
}
