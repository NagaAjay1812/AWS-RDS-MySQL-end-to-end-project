# AWS RDS MySQL – End-to-End Database Connectivity with Windows & Ubuntu

## 📌 Project Overview
This project demonstrates a real-world AWS database architecture where a centralized MySQL database hosted on **AWS RDS** is accessed and managed from multiple servers using different tools and technologies.

The objective is to understand:
- How applications connect to a managed database
- How data is shared across multiple servers
- How high availability works using Multi-AZ deployments

---

## 🏗️ Architecture

                    Internet
                        |
                        |
            +-------------------------+
            |     AWS VPC (us-east-1) |
            |                         |
            |  Public Subnets         |
            |  -------------------    |
            |  Windows EC2            |
            |  (MySQL Workbench)      |
            |                         |
            |  Ubuntu EC2             |
            |  (Python App)           |
            |                         |
            |          |              |
            |          | MySQL (3306) |
            |          v              |
            |  -------------------    |
            |  RDS MySQL (Multi-AZ)   |
            |  Primary (AZ-1C)        |
            |  Standby (AZ-1A)        |
            |                         |
            +-------------------------+


- AWS RDS MySQL (Multi-AZ enabled)
- Windows EC2 instance (Database administration)
- Ubuntu EC2 instance (Application server)
- Python application using SQLAlchemy & PyMySQL

---

## 🔹 Step 1: RDS Subnet Group Creation
- Created an **RDS Subnet Group** using subnets from multiple Availability Zones
- This allows RDS to support **Multi-AZ high availability**

📌 **Why?**  
RDS must be deployed inside subnets, and Multi-AZ requires subnets in different AZs.

---

## 🔹 Step 2: Create AWS RDS MySQL Database
- Created an AWS RDS MySQL instance
- Enabled **Multi-AZ deployment**
- Configured security groups to allow access on port `3306`

📌 **Why RDS?**  
RDS provides a managed, durable, and highly available database without manual OS or database maintenance.

---

## 🔹 Step 3: Launch EC2 Instances
Two EC2 instances were created for different roles:

### 1️⃣ Windows EC2 (Database Administration)
- Used Windows AMI
- This instance is used to manage the database using GUI tools

### 2️⃣ Ubuntu EC2 (Application Server)
- Used Ubuntu AMI
- This instance simulates a real application server connecting to the database

---

## 🔹 Step 4: Windows EC2 Configuration
Inside the Windows instance:
- Disabled IE Enhanced Security and firewall (lab purpose only) 
- Installed Google Chrome
- Installed Visual C++ Redistributable
- Installed **MySQL Workbench**

📌 **Important Note:**  
MySQL Workbench is only a **client tool**.  
All database data is stored **inside AWS RDS**, not on the EC2 instance.

---

## 🔹 Step 5: Database Setup Using MySQL Workbench
- Connected MySQL Workbench to RDS using the RDS endpoint
- Created schemas and tables
- Inserted movie data using SQL scripts

📌 Any SQL query executed from MySQL Workbench directly updates the RDS database.

---

## 🔹 Step 6: Ubuntu EC2 – Application Setup
On the Ubuntu server:
- Installed Python and required system packages
- Created a Python virtual environment
- Installed required libraries:
  - SQLAlchemy
  - PyMySQL

📌 This represents how real applications connect to databases using code.

---

## 🔹 Step 7: Python Application – Database Connectivity
A Python script (`test_db.py`) was created to:
- Connect to the same RDS MySQL database
- Execute SQL queries
- Read and display movie data

### Sample Code:
python

from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://<user>:<password>@<rds-endpoint>:3306/myflixdb"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM movies"))
    for row in result:
        print(row)


📌 Data inserted from Windows was successfully retrieved from Ubuntu, proving multi-client database access.

🔹 Step 8: High Availability Testing (Multi-AZ Failover)
Performed RDS reboot with failover
Primary database switched to standby Availability Zone
Application continued to access the database using the same endpoint
📌 This validates automatic failover and high availability.

✅ Final Outcome
Centralized data storage using AWS RDS
Database accessed from both Windows and Ubuntu servers
Application-level connectivity verified
High availability and failover behavior tested successfully

