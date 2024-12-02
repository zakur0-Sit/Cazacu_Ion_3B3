import sys
import os

directory = sys.argv[1]
total_size = 0

try:
    if not os.path.exists(directory):
        raise FileNotFoundError("Directory does not exists")

    for root, dirs, files in os.walk(directory):
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))

except FileNotFoundError as e:
    print(f"Error :  {e}")
except PermissionError as e:
    print(f"Error : {e}")
except Exception as e:
    print(f"Error : {e}")

print(f"Total size of files in directory {directory} is {total_size} bytes")

# python ex3.py C:\Users\Zakur0\Downloads