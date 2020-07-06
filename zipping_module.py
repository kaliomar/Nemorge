import os
import shutil


def zipit():
  Files = os.listdir(os.getcwd())
  Folders = []
  Rars = []

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
    shutil.make_archive(folder,'zip',folder)
