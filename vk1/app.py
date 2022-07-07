from flask import Flask , request
import json
from flask import Response
app = Flask(__name__)
import random
import urllib.request
import io

@app.route("/vt1") #tämä rivi kertoo osoitteen, josta tämä sovellus löytyy

def vk1():
    joukkuenimi = request.args.get("nimi",default ="")
    nimet = (request.args.getlist("jasen"))
    sarja = request.args.get("sarja",default="")
    reset  = request.args.get("reset",default=0,type=int)
    tila = request.args.get("tila",default="insert",type=str) 
    if reset == 1:
        with urllib.request.urlopen("http://hazor.eu.pythonanywhere.com/2022/data2022s.json")as response:
                data = json.load(response)
    if reset != 1:
       tiedosto = io.open("data.json",encoding="UTF-8")   
       data =json.load(tiedosto)
    def jarjesta():
        
        
        rastit = ""
        lista = []
        sarjat = data["sarjat"]
        for sarja in sarjat:
            for joukkue in sarja["joukkueet"]:
                lista.append(joukkue["nimi"])
            
        lista.sort(key=lambda x: x.lower())     
        for x in lista:
            rastit = rastit + x + "\n"
       
        #return data
        return rastit
    testiJoukkue = {
          "nimi": joukkuenimi,
          "jasenet": nimet,
          "id": 777, 
          "leimaustapa": [3],
       "rastileimaukset": [{
        "aika": "2017-03-18 12:06:42",
        "rasti": 3892036
},]
         }



    def poistaJoukkue(sarja, nimi):
        sarjaindeksi =0
        joukkueindeksi = 0
        sarjat = data["sarjat"]
        for srj in sarjat:
            if srj["nimi"]==sarja:
                for jk in srj["joukkueet"]:
                    if jk["nimi"].lower() == nimi.lower():
                        data["sarjat"][sarjaindeksi]["joukkueet"].pop(joukkueindeksi)
                    joukkueindeksi +=1    
            sarjaindeksi +=1    






    def lisaaJoukkue(sarja, joukkue):
        
             
            sarjat = data["sarjat"]
            condition = True
            if len(sarja)==0 or len(testiJoukkue["nimi"])==0:
                return
                
            if set(("id","nimi","jasenet","leimaustapa","rastileimaukset")).issubset(joukkue.keys()):
                i = 0
               
                for srj in sarjat:
                    if srj["nimi"] == sarja:
                        for jk in srj["joukkueet"]:
                            if jk["nimi"].lower() == joukkue["nimi"].lower():
                                return
                        data["sarjat"][i]["joukkueet"].append(joukkue)
                        
                    i+=1        

                while condition:
                        id = random.randint(1, 1000000000)
                        for sarja in sarjat:
                            for jk in sarja["joukkueet"]:
                                if jk["id"] != id:
                                    joukkue["id"] = id
                                    condition = False
    def haeRastit():
        rastit = ""
        for rasti in data["rastit"]:
            if rasti["koodi"][0].isdigit():
                rastit = rastit +";"+rasti["koodi"]

        return rastit
    
    
    if tila == "delete":
        poistaJoukkue(sarja, joukkuenimi)
        
    if tila != "delete":
        lisaaJoukkue(sarja, testiJoukkue)
    

    def joukkueTiedot():
        rastit = ""
        lista = []
        sarjat = data["sarjat"]
        for sarja in sarjat:
            for joukkue in sarja["joukkueet"]:
                jasenet = " \n"
                
                for jasen in joukkue["jasenet"]:
                    jasenet += " "+jasen+"\n"   
                lista.append(joukkue["nimi"]+ jasenet)
            
        lista.sort(key=lambda x: x.lower())     
        for x in lista:
            rastit = rastit + x + "\n"
       
        #return data
        return rastit
    taso2 = joukkueTiedot()
    rastit = haeRastit()
    joukkueet = jarjesta() 
    with open("data.json","w",encoding="UTF-8") as f:
        f.write(json.dumps(data))
    return   Response(joukkueet + rastit + "\n\n"+taso2,mimetype="text/plain;charset=UTF-8")