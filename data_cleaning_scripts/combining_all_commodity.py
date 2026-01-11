import pandas as pd
import os

# Folder path
folder_path = r"your file path"

# Get all CSV files
csv_files = [
    os.path.join(folder_path, file)
    for file in os.listdir(folder_path)
    if file.endswith(".csv")
]

print("Total CSV files found:", len(csv_files))

# List to hold all DataFrames
df_list = []

for file in csv_files:
    df = pd.read_csv(file)
    
    # Extract commodity name from file name
    commodity = os.path.basename(file).replace("commodity_", "").replace(".csv", "")
    df["commodity"] = commodity
    
    df_list.append(df)

# Combine all CSVs
combined_df = pd.concat(df_list, ignore_index=True)

# Save combined CSV
output_file = os.path.join(folder_path, "all_commodities_combined.csv")
combined_df.to_csv(output_file, index=False)

print("All commodity CSV files combined successfully!")
print("Final Shape:", combined_df.shape)
