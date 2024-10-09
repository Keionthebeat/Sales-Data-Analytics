def transform_sales_data(data):
    transformed_data = []
    for record in data:
        transformed_record = {
            'transaction_id': record[0],
            'customer_id': record[1],
            'product_id': record[2],
            'transaction_date': record[3],
            'amount': record[4]
        }
        transformed_data.append(transformed_record)
    return transformed_data