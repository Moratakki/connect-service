import json

with open('swears.txt', 'r', encoding='utf-8') as swears:
    swearList = []
    for i in swears:
        swear = i.lower().strip()
        if swear != '':
            swearList.append(swear)

with open('swears.json', 'w', encoding='utf-8') as swears:
    json.dump(swearList, swears)
