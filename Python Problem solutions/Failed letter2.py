import pandas as pd
import re

# Load the file line by line
with open('C:/Users/prasa/Desktop/Failedletter.txt', 'r') as f:
    lines = f.readlines()

# Create a DataFrame with one column named 'raw'
df = pd.DataFrame(lines, columns=['raw'])

# Extract alphanumeric Print IDs using updated regex
df['Print_ID'] = df['raw'].str.extract(r'Print ID:\s*([A-Za-z0-9]+)')

# Drop NaNs and get the list
print_ids = df['Print_ID'].dropna().tolist()

# Join and print
print(', '.join(print_ids))