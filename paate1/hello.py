import json
import io 
import urllib.request



# with open("tietorakenne.json",'w',encoding = 'utf-8') as f:
#    f.write(json.dumps(data))
   
   
# tiedosto = io.open("tietorakenne.json",encoding="UTF-8")

# data = json.load(tiedosto)


# for person in data:
#     try:
#         print(person["nimi"])
#     except:
#         pass    

# data.sort(key=lambda hlo: hlo["nimi"])


# for person in data:
#     try:
#         print(person["nimi"])
#     except:
#         pass    
# func = lambda x: x*2
# print(func(5))
with urllib.request.urlopen('https://appro.mit.jyu.fi/ties4080/ohjaus/ohjaus1/malli.json') as response:
   data = json.load(response)


for donut in data["items"]["item"]:
    print (donut["name"])
    print("toppings")
    for topping in donut["topping"]:
        print("     ",topping["type"])
    print("batters")
    for  batter in donut["batters"]["batter"]:
        print("     ",batter["type"])    
   