import re

def extract_emails(filename):
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Read the file content
            content = file.read()
            
            # Use regex to find all email addresses
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, content)
            
            # Convert the list of emails to a set to remove duplicates
            unique_emails = set(emails)
            
            return unique_emails
    except Exception as e:
        print("An error occurred:", e)
        return []

# File example content
file_content = """
Contact List:
John Doe - john.doe@example.com
Jane Smith - jane.smith@gmail.com

For inquiries, please contact info@example.com
"""

# Write the file content to a temporary file
filename = "contacts.txt"
with open(filename, 'w') as file:
    file.write(file_content)

# Extract emails from the file
emails = extract_emails(filename)

# Print the list of unique email addresses
print("Unique email addresses found in the file:")
for email in emails:
    print(email)

# Remove the temporary file
import os
os.remove(filename)
