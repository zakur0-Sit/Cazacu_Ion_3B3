import os

directory = r"I:\Python\Laborator\lab7\fisiere"
new_name = "file"
index = 1

try:
    if not os.path.exists(directory):
        raise FileNotFoundError("Directory does not exists")

    for file in os.listdir(directory):
        full_path = directory + "\\" + file
        new_full_path = directory + "\\" + new_name + str(index) + os.path.splitext(full_path)[1]
        os.rename(full_path, new_full_path)
        index += 1

except FileNotFoundError as e:
    print(f"Error :  {e}")

except PermissionError:
    print("No permission to open the file")

except Exception as e:
    print(f"Error : {e}")
