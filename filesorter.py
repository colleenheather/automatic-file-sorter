import os, shutil

# use forward slashes for path and end with a forward slash
path = r""
file_name = os.listdir(path)

folder_names =['csv files', 'image files', 'text files']

for folder in range(0,3):
    if not os.path.exists(path + folder_names[folder]):
        print(path + folder_names[folder])
        os.makedirs(path + folder_names[folder])

for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    if ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    if ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
