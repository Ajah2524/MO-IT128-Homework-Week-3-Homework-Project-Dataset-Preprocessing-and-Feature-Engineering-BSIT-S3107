# Import necessary libraries
import pandas as pd

# Create the dataset from the provided data
data = {
    'Product_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 10, 3, 6, 1],
    'Product_Name': [
        'Platinum Credit Card', 'Gold Savings Account', 'High-Yield Investment Account',
        'Mortgage Loan', 'Auto Loan', 'Personal Loan', 'Youth Savings Account',
        'Retirement Investment Fund', 'Business Loan', 'Travel Credit Card', 
        'Gold Savings Account', 'Travel Credit Card', 
        'High-Yield Investment Account', 'Personal Loan', 'Platinum Credit Card'
    ],
    'Product_Type': [
        'Credit Card', 'Savings Account', 'Investment', 'Loan', 'Loan', 'Loan', 
        'Savings Account', 'Investment', 'Loan', 'Credit Card', 
        'Savings Account', 'Credit Card', 
        'Investment', 'Loan', 'Credit Card'
    ],
    'Risk_Level': ['Medium', 'Low', 'High', 'Medium', 'Medium', 'Medium', 'Low', 'High', 'Medium', 'Medium', 'Low', 'Medium', 'High', 'Medium', 'Medium'],
    'Target_Age_Group': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    'Target_Income_Group': ['Medium', 'Low', 'High', 'High', 'Medium', 'Low', 'Low', 'High', 'Medium', 'Medium', 'Low', 'Medium', 'High', 'Low', 'Medium']
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
df.head()

# Basic Data Exploration
print("Dataset Overview:")
print(df.info())  # Get data types and null values count
print("\nDataset Summary:")
print(df.describe(include='all'))  # Summary statistics for all columns

# Checking for duplicates in the dataset
duplicates = df[df.duplicated()]
print("\nDuplicate Rows:")
print(duplicates)

# Handling missing values (if any)
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Dropping duplicate rows
df_cleaned = df.drop_duplicates()

# Checking the cleaned dataset
print("\nCleaned Dataset (duplicates removed):")
print(df_cleaned.head())

# Example of filtering data: Get all 'Loan' products with 'Medium' risk level
medium_risk_loans = df_cleaned[(df_cleaned['Product_Type'] == 'Loan') & (df_cleaned['Risk_Level'] == 'Medium')]
print("\nMedium Risk Loans:")
print(medium_risk_loans)

# Example of Grouping data by 'Product_Type' and counting the number of products in each category
product_type_count = df_cleaned.groupby('Product_Type').size()
print("\nCount of Products by Type:")
print(product_type_count)

# Example of Grouping data by 'Risk_Level' and 'Target_Income_Group'
risk_income_group_count = df_cleaned.groupby(['Risk_Level', 'Target_Income_Group']).size()
print("\nCount of Products by Risk Level and Target Income Group:")
print(risk_income_group_count)
