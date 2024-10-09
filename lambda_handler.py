import json
from lambda_extract_sales_data import extract_sales_data
from lambda_transform_sales_data import transform_sales_data
from lambda_load_sales_data import load_sales_data

def lambda_handler(event, context):
    sales_data = extract_sales_data()
    transformed_data = transform_sales_data(sales_data)
    load_sales_data(transformed_data)
    
    return {
        'statusCode': 200,
        'body': json.dumps('ETL process completed successfully')
    }

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