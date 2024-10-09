import psycopg2

def load_sales_data(data):
    # Connect to Redshift
    conn = psycopg2.connect(
        dbname='your_db',             # Change to your Redshift database name
        user='your_user',             # Change to your Redshift user
        password='your_password',     # Change to your Redshift password
        host='your_redshift_cluster'  # Change to your Redshift cluster endpoint
    )
    cur = conn.cursor()
    
    # Load data into Redshift table
    for record in data:
        cur.execute("""
            INSERT INTO sales_transactions (transaction_id, customer_id, product_id, transaction_date, amount)
            VALUES (%s, %s, %s, %s, %s)
        """, (record['transaction_id'], record['customer_id'], record['product_id'], record['transaction_date'], record['amount']))
    
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    data = [
        {
            'transaction_id': 1,
            'customer_id': 101,
            'product_id': 1001,
            'transaction_date': '2023-10-01',
            'amount': 99.99
        },
        {
            'transaction_id': 2,
            'customer_id': 102,
            'product_id': 1002,
            'transaction_date': '2023-10-02',
            'amount': 49.99
        }
        # Add more records as needed
    ]
    load_sales_data(data)