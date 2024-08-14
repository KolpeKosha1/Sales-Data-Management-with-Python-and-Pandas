# Sales Data Management with Python and Pandas

This project showcases how to perform CRUD (Create, Read, Update, Delete) operations on a sales dataset using Python and the pandas library. The dataset is stored in a CSV file, and the project includes functions to manage sales data, such as adding new sales records, updating existing ones, and deleting transactions.

## Features

- **Create**: Add new sales entries to the dataset.
- **Read**: View the current sales data.
- **Update**: Modify existing sales entries based on transaction ID.
- **Delete**: Remove specific sales records by transaction ID.
- **Save**: Persist changes back to the CSV file.

## Requirements

- Python 3.x
- pandas library

## Usage

1. Clone this repository.
2. Install the required packages using `pip install pandas`.
3. Run the script to manage your sales data.

```python
# Example usage:

# Load sales data
sales_df = load_sales_data('path_to_your_csv')

# Create a new sale entry
sales_df = create_sale(sales_df, transaction_id=1001, timestamp='01-01-2024 12:00',
                       customer_id=6789, product_id=789, product_category='Electronics',
                       quantity=5, price=150.0, discount=0.1, payment_method='Credit Card',
                       customer_age=25, customer_gender='Male', customer_location='Europe',
                       total_amount=550.0)

# Save the updated DataFrame back to the CSV file
save_sales_data(sales_df, 'path_to_your_csv')
