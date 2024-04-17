import os, shutil

#Add the directory path to the folder having files that are needed to be sorted
path = r"Replace this string with the folder path here (Exmaple: C:/Users/)"


#Display the list of files in thee folder
file_name = os.listdir(path)
print(file_name)

#Create folders used to receive sorted files
folder_names = ["csv files", "image files", "text files"]
for name in range(0,3):
    if not os.path.exists(path + folder_names[name]):
        print(path + folder_names[name])
        os.makedirs(path + folder_names[name])

#Add correct files to the folders that were created earlier
for file in file_name:
    if ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)

