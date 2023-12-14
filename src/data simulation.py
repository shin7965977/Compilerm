import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set the seed for reproducibility
np.random.seed(0)

# Define the start and end date
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 31)

# Generate a date range
date_range = pd.date_range(start_date, end_date)

# Define ad groups and ad types
ad_groups = ['A', 'B', 'C']
ad_types = [1, 2]

# Generate synthetic data
data = []
for current_date in date_range:
    for ad_group in ad_groups:
        for ad_type in ad_types:
            # Generate random data based on the provided sample
            impression = np.random.randint(40000, 60000)
            clicks = np.random.randint(100, 300)
            views = np.random.randint(7000, 9000)
            buy = np.random.randint(8, 20)
            ctr = clicks / impression
            vtr = views / impression
            btr = buy / views
            cpv = np.random.randint(20, 50)
            cpb = np.random.randint(400, 900)
            ad_cost = np.random.randint(6000, 8000)
            product_cost = 500  # assuming fixed cost
            product_price = 700  # assuming fixed price
            roas = (buy * product_price - ad_cost) / ad_cost
            
            # Append the row to the data
            data.append([current_date, ad_group, ad_type, impression, clicks, views, buy, 
                         ctr, vtr, btr, cpv, cpb, ad_cost, product_cost, product_price, roas])

# Create a DataFrame
column_names = ["date", "ad_group", "ad", "Impression", "Clicks", "Views", "Buy", "CTR", 
                "VTR", "BTR", "CPV", "CPB", "ad_Cost", "product_Cost", "product_price", "ROAS"]
synthetic_df = pd.DataFrame(data, columns=column_names)

# You can then save this DataFrame to a CSV file or use it directly in your machine learning pipeline
# synthetic_df.to_csv('synthetic_data.csv', index=False)

# Display the first few rows to check
print(synthetic_df.head())

# Save the DataFrame to a CSV file in a specific directory
synthetic_df.to_csv(r'C:\Users\shin7\Downloads\synthetic_data.csv', index=False)
