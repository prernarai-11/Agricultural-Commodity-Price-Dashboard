import pandas as pd
import os

# Path to your apples folder
folder_path = r"your file path"

# Get list of all CSV files
csv_files = [
    os.path.join(folder_path, file)
    for file in os.listdir(folder_path)
    if file.endswith(".csv")
]

print(f"Total files found: {len(csv_files)}")

# Read & append all files
df_list = []

for file in csv_files:
    df = pd.read_csv(file)
    
    # Optional but highly recommended
    df["source_file"] = os.path.basename(file)
    
    df_list.append(df)

# Combine into single DataFrame
final_df = pd.concat(df_list, ignore_index=True)

# Save combined file
output_path = os.path.join(folder_path, "apple_all_markets_combined.csv")
final_df.to_csv(output_path, index=False)

print(" All apple CSV files combined successfully!")
print("Rows:", final_df.shape[0])
print("Columns:", final_df.shape[1])