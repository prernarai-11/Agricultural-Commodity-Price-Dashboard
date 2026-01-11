import pandas as pd

# 1. Load Excel file
file_path = r"file path"
df = pd.read_excel(file_path)

# 2. Extract Year from Arrival_Date
df["Arrival_Date"] = pd.to_datetime(df["Arrival_Date"], errors="coerce")
df["Year"] = df["Arrival_Date"].dt.year

# 3. Year + District-wise price rules
price_rules = {
    2022: {
        "Nashik": (30,120), "Mumbai": (30,120), "Satara": (30,120), "Pune": (30,120), "Ahmednagar": (30,120),
        "Anand": (25,100), "Gandhinagar": (25,105), "Kheda": (25,100), "Mehsana": (25,100), "Surat": (25,100),
        "Amritsar": (30,120), "Hoshiarpur": (30,120), "Jalandhar": (30,120), "Ludhiana": (30,120), "Patiala": (30,120),
        "Agra": (25,120), "Kanpur": (25,120), "Meerut": (25,120), "Prayagraj": (25,120), "Varanasi": (25,120),
        "Hooghly": (25,115), "Kolkata": (25,115), "Nadia": (25,115), "North 24 Parganas": (25,115), "Purba Bardhaman": (25,115),
        "Delhi": (30,120)
    },
    2023: {
        "Nashik": (25,100), "Mumbai": (25,100), "Satara": (25,95), "Pune": (25,100), "Ahmednagar": (25,100),
        "Anand": (20,95), "Gandhinagar": (20,100), "Kheda": (20,95), "Mehsana": (20,95), "Surat": (20,95),
        "Amritsar": (25,110), "Hoshiarpur": (25,110), "Jalandhar": (25,110), "Ludhiana": (25,110), "Patiala": (25,110),
        "Agra": (20,110), "Kanpur": (20,110), "Meerut": (20,110), "Prayagraj": (20,110), "Varanasi": (20,110),
        "Hooghly": (20,105), "Kolkata": (20,105), "Nadia": (20,105), "North 24 Parganas": (20,105), "Purba Bardhaman": (20,105),
        "Delhi": (25,110)
    },
    2024: {
        "Nashik": (30,110), "Mumbai": (28,110), "Satara": (28,105), "Pune": (30,110), "Ahmednagar": (28,110),
        "Anand": (25,105), "Gandhinagar": (25,110), "Kheda": (25,105), "Mehsana": (25,105), "Surat": (25,105),
        "Amritsar": (28,115), "Hoshiarpur": (28,115), "Jalandhar": (28,115), "Ludhiana": (28,115), "Patiala": (28,115),
        "Agra": (25,115), "Kanpur": (25,115), "Meerut": (25,115), "Prayagraj": (25,115), "Varanasi": (25,115),
        "Hooghly": (25,110), "Kolkata": (25,110), "Nadia": (25,110), "North 24 Parganas": (25,110), "Purba Bardhaman": (25,110),
        "Delhi": (28,115)
    },
    2025: {
        "Nashik": (28,100), "Mumbai": (30,100), "Satara": (28,95), "Pune": (28,100), "Ahmednagar": (28,95),
        "Anand": (25,95), "Gandhinagar": (25,100), "Kheda": (25,95), "Mehsana": (25,95), "Surat": (25,95),
        "Amritsar": (28,105), "Hoshiarpur": (28,105), "Jalandhar": (28,105), "Ludhiana": (28,105), "Patiala": (28,105),
        "Agra": (25,105), "Kanpur": (25,105), "Meerut": (25,105), "Prayagraj": (25,105), "Varanasi": (25,105),
        "Hooghly": (25,100), "Kolkata": (25,100), "Nadia": (25,100), "North 24 Parganas": (25,100), "Purba Bardhaman": (25,100),
        "Delhi": (28,105)
    }
}

# 4. Mark Keep / Delete
def mark_row(row):
    if row["Commodity"] != "Bhindi":
        return "Keep"

    year = row["Year"]
    district = row["District / City"]

    if year not in price_rules or district not in price_rules[year]:
        return "Keep"

    min_allowed, max_allowed = price_rules[year][district]

    if row["MIN_PRICE_PER_KG"] < min_allowed or row["MAX_PRICE_PER_KG2"] > max_allowed:
        return "Delete"

    return "Keep"

# 5. Apply logic
df["Keep_Delete"] = df.apply(mark_row, axis=1)

# 6. Save cleaned file
output_path = r"C:\Users\Administrator\Desktop\Kropbook\commodity_wise_files\bhindi_cleaned.xlsx"
df.to_excel(output_path, index=False)

print("✅ Bhindi cleaning completed")
print("📁 Output saved to:", output_path)
print(df["Keep_Delete"].value_counts())
