import pandas as pd

def transform_data(csv_file_path, output_file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Extract the columns containing year values
    year_columns = [col for col in df.columns if col.isdigit()]
    
    # Melt the DataFrame to reshape it
    melted_df = pd.melt(df, id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
                        value_vars=year_columns, var_name='Year', value_name='Value')
    
    # Pivot the DataFrame to get the desired format
    pivoted_df = melted_df.pivot_table(index=['Country Name', 'Year'], columns='Indicator Name', values='Value').reset_index()
    
    # Write the result to a new CSV file
    pivoted_df.to_csv(output_file_path, index=False)
    print("Data transformed and saved to:", output_file_path)

csv_file_path = "../files/WDICSV.csv"
output_file_path = "../files/WDI_transformed.csv" 
transform_data(csv_file_path, output_file_path)
