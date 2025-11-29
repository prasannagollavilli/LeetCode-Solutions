import re

def extract_print_ids(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regex to find all Print IDs
    print_ids = re.findall(r'Print ID:\s*(\d+)', content)

    # Join them with commas
    return ', '.join(print_ids)

# Example usage
file_path = 'C:\\Users\\prasa\\Desktop\\Failedletter.txt'  # Replace with your actual file path
print_ids_list = extract_print_ids(file_path)
print("Print IDs:", print_ids_list)
print(print_ids_list)



import os

print("Current working directory:", os.getcwd())
