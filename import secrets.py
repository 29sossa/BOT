import secrets
import os
from datetime import datetime

# Generate a secure password
password = secrets.token_hex(16)  # 16 bytes -> 32-character hex string

# Define the directory and generate a unique filename with a timestamp
directory = r"/home/leon/Desktop"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"password_{timestamp}.txt"
file_path = os.path.join(directory, file_name)

# Write the password to the new file
try:
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Write the password to a unique file
    with open(file_path, 'w') as file:
        file.write(password)
    print(f"Password successfully saved to: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")