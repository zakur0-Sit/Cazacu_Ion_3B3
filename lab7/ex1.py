import sys
import os

try:
    directory = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.exists(directory):
        raise FileNotFoundError("Directory does not exists")

    file_found = False
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_found = True
            print("File : " + filename + "\n")
            print("Content : ")
            with open(directory + "/" + filename, "r", encoding='utf-8') as file:
                print(file.read())
    if not file_found:
        raise FileNotFoundError(f"No files with extension {extension} found")

except FileNotFoundError as e:
    print(f"Error :  {e}")
except PermissionError:
    print("No permission to open the file")
except Exception as e:
    print(f"Error : {e}")

# python ex1.py C:\Users\Zakur0\Downloads .txt