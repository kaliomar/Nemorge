# pattern = re.compile(r"^[^.]+$")
# ^.*aaa.*$
import os
import re


def renameit():
  AFiles = os.listdir(os.getcwd())
  Folders = []
  Files = []
  Patterns = []
  Purecouples = []
  Couples = []

  suffex = str(os.getcwd().split('/')[-1])[:3] + ' '

  for item in AFiles:
    if os.path.isdir(item):
      Folders.append((item))
    else:
      Files.append(item)
      Patterns.append(re.escape(os.path.splitext(item)[0]))

  for pat in Patterns:
    temp = re.compile(r"^.*^{}\S.*$".format(pat))
    SubList = []
    for file in Files:
      match = temp.search(file)
      if match is not None:
        if len(re.escape(os.path.splitext(match.string)[0])) == len(pat):
          SubList.append(match.string)
    curname = re.sub(r'\\(.)',r'\1',pat)
    if curname in Folders:
      SubList.append(curname)
    if len(SubList)>=2:
      Couples.append(SubList)
  for couple in Couples:
    if couple not in Purecouples:
      Purecouples.append(couple)

  name = 0
  while name < len(Purecouples):
    for pucpl in Purecouples[name]:
      strname = suffex+str(name)
      if os.path.isdir(pucpl):
        newname = strname
        os.rename(pucpl,newname)
      else:
        clearname = os.path.splitext(pucpl)
        newname = strname+clearname[1]
        os.rename(pucpl,newname)
    name +=1
