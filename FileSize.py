import os
def get_FileSize():
    filePath=input("Input filePath:")
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    print(round(fsize,2))
while True:
    get_FileSize()
