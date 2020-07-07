import os


def sizeit():
    Files = os.listdir(os.getcwd())
    Folders = []
    Rars = []
    max_size = 0

    for item in Files:
        if item[-4:] == '.rar' or item[-4:] == '.zip' or item[-3:] == '.7z':
            Rars.append(item)

    for item in Files:
        if os.path.isdir(item):
            if item+'.rar' in Rars or item+'.zip' in Rars or item+'.7z' in Rars:
                pass
            else:
                Folders.append(item)
    for folder in Folders:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder):
            for i in filenames:
                f = os.path.join(dirpath, i)
                total_size += os.path.getsize(f)
        max_size += total_size
    print(max_size)


