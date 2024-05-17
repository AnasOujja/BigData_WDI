import pandas as pd

def read_columns_from_txt(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def create_csv_with_selected_columns(input_csv_path, output_csv_paths, columns_txt_paths):
    # Read the original CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv_path)
    
    # Write each DataFrame with selected columns to a separate CSV file
    for output_csv_path, columns_txt_path in zip(output_csv_paths, columns_txt_paths):
        # Include 'Country Name' and 'Year' columns in the selected columns
        selected_columns = ['Country Name', 'Year']

        # Read column names from the text file
        selected_columns.extend(read_columns_from_txt(columns_txt_path))

        # Select the specified columns
        df_selected = df[selected_columns]
        
        # Write the DataFrame to a CSV file
        df_selected.to_csv(output_csv_path, index=False)

input_csv_path = "../files/WDI_transformed.csv"
output_csv_paths = ["../files/WDI_environment.csv", "../files/WDI_economy.csv"]
columns_txt_paths = ["../files/indicators_environment.txt", "../files/indicators_economy.txt"]

create_csv_with_selected_columns(input_csv_path, output_csv_paths, columns_txt_paths)
