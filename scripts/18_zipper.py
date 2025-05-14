import os
from datetime import datetime
from zipfile import ZipFile


# # set file name and time of creation
# today = datetime.now()
# file_name = 'zipper_' + today.strftime('%Y.%m.%dh%H%M') + '.zip'
# dir_name = 'tmp/'  # update path
# 
# 
# def zipdir(path, zip):
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             zip.write(os.path.join(root, file))
# 
# if __name__ == '__main__':
#     zipfile = ZipFile(file_name, 'w')
#     zipdir(dir_name, zipfile)
#     zipfile.close()

# # set file name and time of creation
today = datetime.now()
file_name = 'zipper_' + today.strftime('%Y.%m.%dh%H%M') + '.zip'
dir_name = 'tmp/'  # update path

def add_folder_to_zip(folderPath,zipFile):
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            print(file)
            print(root)
            full_path = os.join(root, file)
            zipfile.write(full_path)
#         zipfile.write()
#         print(root, dirs, files)

with ZipFile("test_zip","w") as my_zip:
    #add_folder_to_zip("testFolder8",my_zip)
    print(my_zip)




