import os

def count_file_extensions(directory):
    try:
        # Check if the directory exists
        if os.path.exists(directory):
            print("Counting file extensions in directory:", directory)
            # Dictionary to store counts of each file extension
            extension_count = {}

            # Iterate through files in the directory
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                # Check if it's a file
                if os.path.isfile(file_path):
                    # Get the file extension and convert it to lowercase
                    file_extension = os.path.splitext(file)[1].lower()
                    # Increment the count for the file extension
                    extension_count[file_extension] = extension_count.get(file_extension, 0) + 1
            
            # Print the count of each file extension
            for extension, count in extension_count.items():
                print(f"{extension.upper()}: {count}")
        else:
            print("The specified directory does not exist.")
    except Exception as e:
        print("An error occurred:", e)

# Prompt the user for the directory path
directory_path = input("Enter the directory path: ")

# Call the function to count file extensions
count_file_extensions(directory_path)
