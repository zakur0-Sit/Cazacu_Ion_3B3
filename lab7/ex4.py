import sys
import os

directory = sys.argv[1]
extension_dict = {}
files_found = False

try:
    if not os.path.exists(directory):
        raise FileNotFoundError("Directory does not exists")

    for file in os.listdir(directory):
        extension = os.path.splitext(file)[1]
        files_found = True
        if extension not in extension_dict:
            extension_dict.update({extension: 1})
        else:
            extension_dict[extension] += 1

    if not files_found:
        raise FileNotFoundError(f"No files in directory : {directory}")

except FileNotFoundError as e:
    print(f"Error : {e}")
except PermissionError as e:
    print(f"Error : {e}")
except Exception as e:
    print(f"Error : {e}")

for key, value in extension_dict.items():
    print(f"Key : {key} | Value : {value}")

# python ex4.py C:\Users\Zakur0\Downloads