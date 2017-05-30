import os

def renameFiles():
    # (1) get file names from a folder
    files = os.listdir(r"C:\Users\David\OneDrive\Documents\Python\Udacity\Projects\SecretMessage\prank")
    # print(files)
    savedPath = os.getcwd()
    print("The Current Working Directory is: " + savedPath)
    os.chdir(r"C:\Users\David\OneDrive\Documents\Python\Udacity\Projects\SecretMessage\prank")
    
    # (2) for each file, rename filename
    for fileName in files:
        print("Old file name: " + fileName)
        print("New file name: " + fileName.translate(None, "123456789"))
        os.rename(fileName, fileName.translate(None, "0123456789"))

    os.chdir(savedPath)

renameFiles()

