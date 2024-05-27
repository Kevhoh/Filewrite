# 1. File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("2nd line with a number: 42\n")
        file.write("The third line is here.\n")
except Exception as e:
    print(f"Error occurred while creating the file: {e}")

# 2. File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        contents = file.readlines()
        print("File contents:")
        for line in contents:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Error occurred while reading the file: {e}")

# 3. File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This line is appended.\n")
        file.write("Another appended line.\n")
        file.write("3rd appended line with a number: 3.14\n")
except Exception as e:
    print(f"Error occurred while appending to the file: {e}")
finally:
    print("File appending operation completed.")

# 4. Error Handling
try:
    with open("non_existent_file.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("The file 'non_existent_file.txt' does not exist.")
except PermissionError:
    print("You do not have permission to access the file.")
except Exception as e:
    print(f"An error occurred: {e}")