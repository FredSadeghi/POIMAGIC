import os
def list_files(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().endswith(filetype.lower()):
            paths.append(os.path.join(root, file))
   return(paths)

#https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/

