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

  location = ""
  running = True

  while running:
    print(location)
    userinput = input().split()
    
    if userinput[0] == "create" or userinput[0] == "edit":
      if location != "{":
        mydict[location.split("{")[-1]][userinput[1]] = listtostr(userinput[2:])
      else:
        mydict[userinput[1]] = listtostr(userinput[2:])
    elif userinput[0] == "create-dict":
      if location != "{":
        mydict[location.split("{")[-1]][listtostr(userinput[1:])] = {}
      else:
        mydict[userinput[1]] = {}
      
      location = location + "{" + userinput[1]
    elif userinput[0] == "remove":
      if location != "{":
        mydict[location.split("{")[-1]][userinput[1]].pop()
      else:
        mydict[userinput[1]].pop()
    elif userinput[0] == "end":
      running = False

    os.system("clear")
  
  f.write(json.dumps(mydict))
  f.close()

if userinput[0] == "make":
  make(userinput)
