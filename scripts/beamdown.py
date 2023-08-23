import base64
import os

source_relative = os.getenv("BUNDLE", "./output.txt")
source = os.path.abspath(source_relative)

destination = os.getenv("TARGET", "./replica")
if not os.path.exists(destination):
  os.makedirs(destination)
os.chdir(destination)

with open(source, "r") as data:
  while True:
    path = data.readline()
    content = data.readline()

    if not path and not content:
      break
    
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
      os.makedirs(directory)

    with open(path, "wb") as newfile:
      newfile.write(base64.b64decode(content.strip()))      
