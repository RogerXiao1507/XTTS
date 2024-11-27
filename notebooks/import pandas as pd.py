import pandas as pd

# Read the CSV file
input_file = '/Users/rogerxiao/Downloads/XTTS/notebooks/ruanmei_data/ruanmei.csv'  # Replace with the actual file name
output_file = '/Users/rogerxiao/Downloads/XTTS/notebooks/ruanmei_data/ruanmeiv2.csv'

# Load the data into a DataFrame with a custom separator
df = pd.read_csv(input_file, sep='|', header=None, names=["key", "text"])

# Increment the numeric part at the end of each key
def increment_key(key, start_value=101):
    if key.startswith('VO_side0_rm_ruanmei_'):
        prefix = 'VO_side0_rm_ruanmei_'
        number = int(key[len(prefix):])  # Extract the number
        incremented_key = f"{prefix}{number + 1}"  # Increment the number
        return incremented_key
    return key

# Apply the transformation
df['key'] = df['key'].apply(increment_key)

# Save the updated data into a new CSV file
df.to_csv(output_file, sep='|', index=False, header=False)

print(f"Updated CSV saved to {output_file}")
