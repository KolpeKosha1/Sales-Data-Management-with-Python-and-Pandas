import pandas as pd

# Load the sales DataFrame from a CSV file
def load_sales_data(file_path):
    return pd.read_csv(file_path)

# Save the sales DataFrame back to the CSV file
def save_sales_data(sales_df, file_path):
    sales_df.to_csv(file_path, index=False)

# Function to create a new sale entry
def create_sale(sales_df, transaction_id, timestamp, customer_id, product_id, 
                product_category, quantity, price, discount, payment_method, 
                customer_age, customer_gender, customer_location, total_amount):
    new_sale = pd.DataFrame([{
        'transaction_id': transaction_id,
        'timestamp': timestamp,
        'customer_id': customer_id,
        'product_id': product_id,
        'product_category': product_category,
        'quantity': quantity,
        'price': price,
        'discount': discount,
        'payment_method': payment_method,
        'customer_age': customer_age,
        'customer_gender': customer_gender,
        'customer_location': customer_location,
        'total_amount': total_amount
    }])
    sales_df = pd.concat([sales_df, new_sale], ignore_index=True)
    return sales_df

# Function to update a sale entry
def update_sale(sales_df, transaction_id, **kwargs):
    index = sales_df[sales_df['transaction_id'] == transaction_id].index
    if not index.empty:
        for key, value in kwargs.items():
            if key in sales_df.columns and value is not None:
                sales_df.loc[index, key] = value
    return sales_df

# Function to delete a sale entry
def delete_sale(sales_df, transaction_id):
    sales_df = sales_df[sales_df['transaction_id'] != transaction_id]
    return sales_df

# Function to read sales DataFrame
def read_sales(sales_df):
    return sales_df

# File path to the sales CSV file
file_path = 'C:/Users/shiva/Downloads/online_retail_sales_dataset.csv'

# Load sales data
sales_df = load_sales_data(file_path)

# Demonstrate CRUD operations

# Create a new sale entry
sales_df = create_sale(sales_df, transaction_id=1001, timestamp='01-01-2024 12:00',
                       customer_id=6789, product_id=789, product_category='Electronics',
                       quantity=5, price=150.0, discount=0.1, payment_method='Credit Card',
                       customer_age=25, customer_gender='Male', customer_location='Europe',
                       total_amount=550.0)
save_sales_data(sales_df, file_path)  # Save changes to CSV

# Read the sales DataFrame after creating a new entry
sales_after_create = read_sales(sales_df)
print(sales_after_create.tail())  # Display last few rows to show the new entry

# Update an existing sale entry
sales_df = update_sale(sales_df, transaction_id=2, price=200.0, discount=0.2)
save_sales_data(sales_df, file_path)  # Save changes to CSV

# Read the sales DataFrame after updating an entry
sales_after_update = read_sales(sales_df)
print(sales_after_update[sales_after_update['transaction_id'] == 2])

# Delete a sale entry
sales_df = delete_sale(sales_df, transaction_id=1)
save_sales_data(sales_df, file_path)  # Save changes to CSV

# Read the sales DataFrame after deleting an entry
sales_after_delete = read_sales(sales_df)
print(sales_after_delete.head())  # Display first few rows to show the deleted entry
