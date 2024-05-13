import os

def list_directory_contents(path):
    try:
        # Check if the path exists
        if os.path.exists(path):
            print("Listing contents of directory:", path)
            # List all files and subdirectories in the given path
            for item in os.listdir(path):
                print(item)
        else:
            print("The specified directory does not exist.")
    except Exception as e:
        print("An error occurred:", e)

# Prompt the user for the directory path
directory_path = input("Enter the directory path: ")

# Call the function to list directory contents
list_directory_contents(directory_path)
