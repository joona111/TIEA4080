data = [
        { 'nimi': 'Kalle',
          'ammatti': 'Yliopistonopettaja',
          'syntymävuosi': 1980,
          'palkka': 2000
        },
        {  'nimi': 'Ville',
    'ammatti': 'Opiskelija',
    'syntymävuosi': 1995,
    'kotipaikka': 'Jyväskylä',
    'palkka': 1000
},
        { 'nimi': 'Maija',
          'ammatti': 'Professori',
          'syntymävuosi': 1970,
          'palkka': 3000
        }
]     
joona = {
    "nimi": "Joona",
    "ammatti": "opiskelija",
    "syntymävuosi":1998
    
}
data.append(joona)
# for person in data:
    
#         for key,value in sorted(person.items()):
            
#             print (key,value)
    
"""   
for person in data:
    for key,value in person.items():
        if key =="ammatti":
            print (value) """
""" 
for person in data:
    try:
        print(person["kotipaikka"])       
    except:
        print("ei oo")
 """
summa = 0
maara = 0
for person in data:
    
    try:
        
        summa += person["palkka"]
        maara +=1
       
    except:
        
        summa+=560
print ("yhteensä",summa,"keskipalkka",summa/maara)            