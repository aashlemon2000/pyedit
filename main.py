import os
import json

userinputraw = input()
userinput = userinputraw.split()

def listtostr(list, addspace=True):
  mystr = ""

  for x in list:
    mystr += x
    if addspace:
      mystr += " "

  return mystr

def make(userinputg):
  f = open(listtostr(userinputg[1:]), "x")
  os.system("clear")
  mydict = {}

  running = True

  while running:
    userinput = input().split()
    
    if userinput[0] == "create" or userinput[0] == "edit":
      mydict[userinput[1]] = listtostr(userinput[2:])
    elif userinput[0] == "remove":
      mydict[userinput[1]].pop()
    elif userinput[0] == "end":
      running = False
    elif userinput[0] == "show-all":
      print(mydict)

    os.system("clear")
  
  f.write(json.dumps(mydict))
  f.close()

if userinput[0] == "make":
  make(userinput)
