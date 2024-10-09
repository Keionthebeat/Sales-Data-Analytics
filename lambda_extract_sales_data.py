import pymysql

def extract_sales_data():
    connection = pymysql.connect(
        host='your_mysql_host',
        user='your_mysql_user',
        password='your_mysql_password',
        database='your_mysql_db'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sales_transactions")
    sales_data = cursor.fetchall()
    cursor.close()
    connection.close()
    return sales_data