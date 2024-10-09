-- Create sales_transactions table
CREATE TABLE sales_transactions (
    transaction_id INT PRIMARY KEY,  -- Unique ID for each transaction
    customer_id INT,                 -- ID of the customer making the transaction
    product_id INT,                  -- ID of the product being purchased
    transaction_date DATE,           -- Date of the transaction
    amount DECIMAL(10, 2)            -- Amount of the transaction
);

-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,     -- Unique ID for each customer
    name VARCHAR(100),               -- Name of the customer
    email VARCHAR(100),              -- Email of the customer
    join_date DATE                   -- Date the customer joined
);

-- Create products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,      -- Unique ID for each product
    name VARCHAR(100),               -- Name of the product
    category VARCHAR(50),            -- Category of the product
    price DECIMAL(10, 2)             -- Price of the product
);
