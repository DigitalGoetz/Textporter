
import base64
import os
import sys

target_directory = os.getenv("TARGET", "./dummy")
output_name = os.getenv("BUNDLE", "output.txt")
start_directory = os.getcwd()

print(f"Using target: {target_directory}")
print(f"Output file: {output_name}")

if not os.path.exists(target_directory):
   print(f"Target directory: {target_directory} doesn't exist")
   sys.exit(1)

if os.path.exists(output_name):
   print(f"Output file: {output_name} already exists")
  #  sys.exit(2)

def file_to_string(file_path: str):
  with open(file_path, "rb") as file:
      file_content = file.read()
      file_content_base64 = base64.b64encode(file_content).decode("utf-8")

  return (file_path, file_content_base64)

def get_all_file_paths(directory):
    print(f"using dir: {directory}")
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            print(filename)
            file_paths.append(os.path.join(root, filename))
    return file_paths

directory_path = os.path.abspath(target_directory)
os.chdir(os.path.dirname(directory_path))
base_directory = os.path.basename(directory_path)
all_file_paths = get_all_file_paths(base_directory)

os.chdir(start_directory)
with open(output_name, "w") as out:
  os.chdir(os.path.dirname(directory_path))
  for file_path in all_file_paths:
    data = file_to_string(file_path)
    out.write(data[0])
    out.write("\n")
    out.write(data[1])
    out.write("\n")