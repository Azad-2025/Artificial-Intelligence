import pandas as pd
file_path = "C:\\clp\\sales_data.csv"
sales_data = pd.read_csv(file_path)
total_revenue = sales_data.groupby("Product")["Total Revenue"].sum()
print("Total Revenue per Product:\n", total_revenue)