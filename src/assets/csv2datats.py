import pandas as pd

# File paths
input_csv = "SRSC_unique_wwt.csv"  # Replace with your input CSV file name
output_ts = "data.ts"  # Replace with your desired .ts file name

# Read the CSV into a DataFrame
df = pd.read_csv(input_csv)

# Sort by 'frequency'
df = df.sort_values(by="frequency")

# Group by frequency and create export statements
with open(output_ts, "w") as ts_file:
    for freq, group in df.groupby("frequency"):
        # Create the export constant name
        const_name = f"MHZ_{str(freq).replace('.', '_')}_CSV"
        
        # Convert group DataFrame to CSV string without extra newline
        csv_content = group.to_csv(
            index=False, 
            header=True, 
            columns=["Name", "RA", "DEC", "Dist", "frequency", "observatory"], 
            lineterminator="\n"  # Prevent extra newlines
        ).strip()
        
        # Write to the .ts file
        ts_file.write(f"export const {const_name} = `{csv_content}`;\n\n")

print(f"Data successfully exported to {output_ts}")