def main():
    while True:
        file_name = get_valid_filename("Enter the name of a text file: ")

        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

        write_option = input("Do you want to write to this file? (yes/no): ").lower()

        if write_option == 'yes':
            append_content(file_name)
        elif write_option == 'no':
            write_new_file()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def get_valid_filename(prompt):
    while True:
        try:
            file_name = input(prompt)
            with open(file_name, 'r'):
                return file_name
        except FileNotFoundError:
            print("Error: The file doesn't exist. Please enter a valid filename.")
        except ValueError:
            print("Error: Invalid filename. Please enter a valid filename.")

def append_content(file_name):
    with open(file_name, 'a') as file:
        new_content = input("Enter the content you want to add: ")
        file.write(new_content + '\n')
        print("Content has been added to the file.")
        print("Writing successful.")
    print("File has been closed.")

def write_new_file():
    new_file_name = input("Enter a new filename for writing: ")
    try:
        with open(new_file_name, 'w') as new_file:
            new_content = input("Enter the content you want to write: ")
            new_file.write(new_content)
            print("Content has been written to the new file.")
            print("Writing successful.")
    except FileNotFoundError:
        print("Error: Could not create the new file.")
    print("File has been closed.")

if __name__ == "__main__":
    main()
