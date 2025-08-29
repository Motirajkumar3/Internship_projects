🛰️ **Network Complaint Management System** 

This project was developed during my Internship at DRDO. It is a simple web-based Network Complaint Management System that allows users to register, track, and resolve network-related issues in an organized manner.  

---

🚀 **Features**  

- **User-friendly** web interface to log complaints.  
- **Admin panel** to view and manage all registered complaints.  
- Status tracking of complaints (Pending, In-progress, Resolved).  
- Secure login system for both users and admins.  
- Database integration for storing complaints and user details.  

---

## 🛠️ Tech Stack  

- **Frontend**: HTML, CSS, ASP.NET Web Forms  
- **Backend**: C# (.NET Framework)  
- **Database**: SQL Server  
- **IDE/Tools**: Visual Studio  
- **Configuration/Hosting**: IIS / Localhost (via Visual Studio)  

---

📂**Project Structure**  

Network_complaint-master/  <br>
├── .gitattributes<br>
├── .gitignore<br>
├── README.md<br>
├── WebApplication3.sln # Visual Studio Solution file<br>
├── WebApplication3/ # Main application folder<br>
│ ├── About.aspx # About page<br>
│ ├── admin.aspx # Admin panel page<br>
│ ├── App_Start/ # App configuration (routes, bundles)<br>
│ │ ├── BundleConfig.cs<br>
│ │ ├── RouteConfig.cs<br>
│ ├── Bundle.config<br>
│ ├── Contact.aspx # Contact page<br>
│ ├── Content/ # CSS and styling (Bootstrap etc.)<br>
│ ├── Default.aspx # Homepage / Landing page<br>
│ ├── Global.asax # Application lifecycle settings<br>
│ ├── Scripts/ # JavaScript files<br>
│ ├── Site.Master # Master layout page<br>
│ ├── Site.Mobile.Master # Mobile layout page<br>
│ ├── tech.aspx # Technician complaint page<br>
│ ├── ViewSwitcher.ascx # Mobile/Desktop view switcher<br>
│ ├── Web.config # App configuration (database, auth, etc.)<br>
│ ├── Web.Debug.config<br>
│ ├── Web.Release.config
│ ├── welcome.aspx # Welcome page<br>
│ ├── WebApplication3.csproj # Project file<br>

---

⚡ **Installation & Setup** 
1. Clone the repository:  
   git clone https://github.com/Motirajkumar3/Internship_projects.git

2.Move to the project folder:
  cd Internship_projects/DRDO/Network_Complaints/Network_complaint-master

3.Copy the project folder to your htdocs (if using XAMPP) or www (if using WAMP).

4.Import the SQL file located in the /database folder into phpMyAdmin to set up the database.

5.Update the includes/config.php file with your database credentials.

6.Run the project on your localhost:
  http://localhost/Network_complaint-master/

🔑 **Default Credentials**<br>
  **Admin Login**<br>
   Username: admin<br>
    Password: admin123<br>
  **User Login**<br>
    Create a new account via the signup page.<br>

📌 **Future Improvements**<br>
- Email/SMS notifications for complaint updates.<br>
- Role-based access with multiple admin levels.<br>
- Analytics dashboard for complaint trends.<br>
- Cloud deployment with AWS.<br>

---

  **🏆 Internship Note**
<br>
This project was created as part of my Internship at DRDO (Defence Research and Development Organisation), where I worked on understanding network complaint workflows and building an application to simplify the process.
