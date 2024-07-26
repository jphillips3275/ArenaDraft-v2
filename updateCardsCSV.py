import requests
import csv

url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/cards"
headers = {
	"X-RapidAPI-Key": "5a98dbfd38msh6e3366d4d39e439p1376e2jsn7ea5e6dbf043",
	"X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com"
}

response = requests.get(url)
query = {"collectible":"1"}

print("Talking to the API...")
response = requests.get(url, headers=headers, params=query)
dictionary = response.json()
print("Response: ", response.status_code)

keys = ['cardId', 'dbfId', 'name', 'cardSet', 'type', 'faction', 'rarity', 'cost', 'runeCost', 'attack', 'health', 'durability', 'spellSchool', 'text', 'flavor', 'artist', 'collectible', 'elite', 'race', 'img', 'imgGold', 'locale']
skip = ['Missions', 'Demo', 'System', 'Debug', 'Promo', 'Credits', 'Hero Skins', 'Tavern Brawl', 'Taverns of Time', 'Wild Event', 'Battlegrounds', 'Mercenaries', 'Unknown', 'Caverns of Time', 'Tutorial']

print("Writing to CSV file...")
with open('cards.csv', 'w', newline="") as file:
    writer = csv.DictWriter(file, keys, extrasaction='ignore')
    writer.writeheader()
    for set in dictionary:
        if set not in skip:
            print("Writing ", set, "...", sep='')
            for card in dictionary[set]:
                try:
                    writer.writerow(card)
                except:
                    print("An error has occured while writing")
                    continue