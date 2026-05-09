import pandas as pd
import numpy as np

# 1. Define the files and their corresponding column headers
file_mapping = {
    'out_p1_d.csv': 'Washing machine',
    'out_p2_d.csv': 'Electric Iron',
    'out_p3_d.csv': 'LED Tv',
    'out_p4_d.csv': 'CFL Lamp',
    'out_ps.csv': 'MCP_data'
}

# 2. Initialize an empty DataFrame to hold all the combined data
merged_df = pd.DataFrame()
time_column_created = False

print("Starting data processing and merge...\n")

for file_name, header_name in file_mapping.items():
    try:
        # Read the raw CSV (no headers)
        df = pd.read_csv(file_name, header=None)
        
        new_times = []
        averaged_data = []
        
        # 3. Process the file in pairs (Downsampling)
        for i in range(0, (len(df) // 2) * 2, 2):
            row1 = df.iloc[i]
            row2 = df.iloc[i+1]
            
            # Average the data column(s)
            mean_vals = (row1.iloc[1:] + row2.iloc[1:]) / 2
            
            # Calculate the new timestamp
            new_row_index = i // 2
            new_time = round(0.01 + (new_row_index * 0.04), 2)
            
            new_times.append(new_time)
            
            # Assuming there is 1 main data column per file (index 1)
            # We extract it and round to 2 decimal places
            averaged_data.append(round(mean_vals.iloc[0], 2))
        
        # 4. Add the Time column to the merged DataFrame (only need to do this once)
        if not time_column_created:
            merged_df['Time'] = new_times
            time_column_created = True
            
        # 5. Add the averaged data as a new column with the specific header
        merged_df[header_name] = averaged_data
        
        print(f"Processed {file_name} -> Added as column '{header_name}'")
        
    except FileNotFoundError:
        print(f"Warning: {file_name} not found. Skipping.")
    except Exception as e:
        print(f"Error processing {file_name}: {e}")

# 6. Save the final combined DataFrame to a single CSV file
output_filename = 'merged_training_data.csv'

# index=False prevents pandas from writing row numbers
# header=True ensures your custom column names are saved at the top
if not merged_df.empty:
    merged_df.to_csv(output_filename, index=False, header=True)
    print(f"\nSuccess! Merged dataset saved to: {output_filename}")
    print(f"Dataset shape: {merged_df.shape[0]} rows and {merged_df.shape[1]} columns.")
    
    # Preview the first few rows in the console to verify
    print("\nFirst 3 rows of the merged dataset:")
    print(merged_df.head(3).to_string())
else:
    print("\nFailed to merge: No data was processed.")