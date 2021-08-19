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
  f = open(listtostr(userinputg[1:]), "w")
  os.system("clear")
  mydict = {}

  location = ""
  running = True

  while running:
    currentlocation = location.split("/")
    for x in currentlocation:
      if x == "":
        currentlocation.remove(x)

    print(location, "\n", mydict)
    userinput = input().split()
    
    if userinput[0] == "create" or userinput[0] == "edit":
      if location != "":
        if not currentlocation[-1] == "$array"
          mydict[currentlocation[-1]][userinput[1]] = listtostr(userinput[2:])
        else:
          thislist = currentlocation.reverse()
          for x in thislist:
            
      else:
        mydict[userinput[1]] = listtostr(userinput[2:])
    elif userinput[0] == "create-array":
      withinarray = None

      if location != "":
        try:
          mydict[currentlocation[-1]][listtostr(userinput[1:])] = []
        except:
          mydict[currentlocation[-1]][userinput[1]] = []
          withinarray = True
      else:
        mydict[userinput[1]] = []
      
      if not withinarray:
        location = location + userinput[1] + "/"
      elif withinarray:
        location = location + "$array/"
    elif userinput[0] == "remove":
      if location != "":
        mydict[currentlocation[-1]][userinput[1]].pop()
      else:
        mydict[userinput[1]].pop()
    elif userinput[0] == "end":
      running = False

    os.system("clear")
  
  f.write(json.dumps(mydict))
  f.close()

if userinput[0] == "make":
  make(userinput)
