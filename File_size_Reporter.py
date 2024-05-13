import os

def report_file_sizes(directory):
    try:
        # Check if the directory exists
        if os.path.exists(directory):
            print("Reporting file sizes in directory:", directory)
            # Iterate through files in the directory
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                # Check if it's a file
                if os.path.isfile(file_path):
                    # Get the size of the file
                    file_size = os.path.getsize(file_path)
                    # Print the file name and size
                    print(f"{file}: {file_size} bytes")
        else:
            print("The specified directory does not exist.")
    except Exception as e:
        print("An error occurred:", e)

# Prompt the user for the directory path
directory_path = input("Enter the directory path: ")

# Call the function to report file sizes
report_file_sizes(directory_path)
