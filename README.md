# Sales Data Analytics Platform

## Project Overview

The Sales Data Analytics Platform is designed to provide businesses with comprehensive insights into their sales performance, customer behavior, and market trends. By leveraging Power BI for visualisation, AWS Redshift for data warehousing, AWS Lambda for ETL (Extract, Transform, Load) processes, Microsoft Entra ID for identity management, and MySQL for transactional data storage, this platform offers a robust and scalable solution for data-driven decision-making.

## Objectives

- **Centralised Data Storage**: Consolidate sales, customer, and product data from various sources into a single data warehouse.
- **Automated Data Processing**: Implement automated ETL processes to ensure data is consistently updated and transformed for analysis.
- **Interactive Data Visualisation**: Create interactive dashboards and reports in Power BI to visualize key performance indicators (KPIs) and trends.
- **Secure Access Management**: Use Microsoft Entra ID to manage user authentication and access to the Power BI dashboards and reports.


## Solution

### Components

1. **MySQL Database**: Stores raw sales, customer, and product data.
2. **AWS Redshift**: Central data warehouse for analytics.
3. **AWS Lambda**: Automates data extraction, transformation, and loading (ETL) processes.
4. **Power BI**: Visualises data through interactive dashboards and reports.
5. **Microsoft Entra ID**: Manages user authentication and access to Power BI.

### Implementation

1. **MySQL Database Setup**:
   - Create tables for `sales_transactions`, `customers`, and `products`.
   - Populate the tables with initial data.

2. **AWS Redshift Setup**:
   - Create corresponding tables in Redshift for `sales_transactions`, `customers`, and `products`.

3. **AWS Lambda Functions**:
   - Develop Lambda functions to extract data from MySQL, transform it, and load it into Redshift.

4. **Power BI Configuration**:
   - Connect Power BI to the Redshift data warehouse.
   - Create and publish dashboards and reports.

5. **Microsoft Entra ID Configuration**:
   - Set up Microsoft Entra ID for user authentication and authorization.
   - Define user roles and permissions for accessing Power BI dashboards and reports.

## Benefits

- **Improved Decision-Making**: Provides real-time insights into sales performance, enabling data-driven decisions.
- **Enhanced Data Accuracy**: Automated Extract, Transform, Load (ETL) processes to ensure data consistency and accuracy.
- **Scalability**: The platform can scale with the business, accommodating growing data volumes and user numbers.
- **Security**: Microsoft Entra ID ensures secure access to sensitive data and reports.

## How to Execute the Code

1. **Install Required Libraries**:
   - Open a terminal and run the following command to install the necessary Python libraries:
     ```sh
     pip install pymysql psycopg2-binary
     ```

2. **Prepare the Data**:
   - Ensure you have the data in the correct format. 
   Please check `mysql_tables.sql`


3. **Update the Connection Details**:
   - Replace the placeholders in the `psycopg2.connect` function with your actual Redshift cluster details:
     ```python
     conn = psycopg2.connect(
         dbname='your_db',             # Change to your Redshift database name
         user='your_user',             # Change to your Redshift user
         password='your_password',     # Change to your Redshift password
         host='your_redshift_cluster'  # Change to your Redshift cluster endpoint
     )
     ```
 `psycopg2.connect` is a function call in Python used to establish a connection to a PostgreSQL database, which in this case is AWS Redshift.

4. **Run the Main Lambda Handler**:
   - Save the main Lambda handler script as `lambda_handler.py`.
     - Open a terminal and navigate to the directory where your [lambda_handler.py] script is located:
     ```sh
     cd /path/to/your/project/directory
     ```
   - Execute the script from the command line:
     ```sh
     python lambda_handler.py
     ```

This will execute the ETL process, extracting data from MySQL, transforming it, and loading it into AWS Redshift.

## Conclusion

The Sales Data Analytics Platform provides a comprehensive solution for businesses to analyze their sales data, gain valuable insights, and make informed decisions. By integrating various technologies such as Power BI, AWS Redshift, AWS Lambda, Microsoft Entra ID, and MySQL, the platform ensures data accuracy, scalability, and security.