import json

with open("recensioni.json", "r") as file:
    contenuto = json.load(file)

recensioni_medie = []
for ristorante in contenuto:
    if ristorante["recensioni"]:
        somma = 0
        for voto in ristorante["recensioni"]:
            somma += voto
        media = somma / len(ristorante["recensioni"])
    else:
        media = 0.0
    recensioni_medie.append({
        "nome": ristorante["nome"],
        "media": media
    })

for i in range(len(recensioni_medie)):
    for j in range(i+1, len(recensioni_medie)): 
        if recensioni_medie[i]["media"] < recensioni_medie[j]["media"]:
            recensioni_medie[i], recensioni_medie[j] = recensioni_medie[j], recensioni_medie[i]

with open("recensioni_medie.json", "w") as file:
    json.dump(recensioni_medie, file, indent=4)
