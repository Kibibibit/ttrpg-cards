
import pandas as pd


frame = pd.read_csv("./DND Cards - Batch-1.csv", dtype={
    'AC':"str",
    'IdentifyNo':"str"
})


indexFile = None
templateFile = None
costFile = None
cssTemplate = None
cssRarityTemplate = None
cssCoinTemplate = None
cssBackTemplate = None

coins = ["CP","SP","EP","GP","PP"]
coinReplacements = ["LIGHT_COLOUR","MID_COLOUR","DARK_COLOUR"]
rarities = ["COMMON", "UNCOMMON", "RARE", "VERY_RARE","LEGENDARY", "UNIDENTIFIED", "CURSED"]
itemTypes = ["WEAPON","POTION","ARMOUR","ITEM"]

with open("./index-template.txt") as f:
    cssTemplate = f.read()
    f.close()

with open("./index-template.html") as f:
    indexFile = f.read()
    f.close()

with open("./item-card-template.html") as f:
    templateFile = f.read()
    f.close()

with open("./cost-template.html") as f:
    costFile = f.read()
    f.close()

with open("./index-rarities-template.txt") as f:
    cssRarityTemplate = f.read()
    f.close()

with open("./index-coins-template.txt") as f:
    cssCoinTemplate = f.read()
    f.close()

with open("./index-backs-template.txt") as f:
    cssBackTemplate = f.read()
    f.close()


replacements = {
    "${{DMG_AC}}":"Acid",
    "${{DMG_BL}}":"Bludgeoning",
    "${{DMG_CO}}":"Cold",
    "${{DMG_FI}}":"Fire",
    "${{DMG_FO}}":"Force",
    "${{DMG_LI}}":"Lightning",
    "${{DMG_NE}}":"Necrotic",
    "${{DMG_PI}}":"Piercing",
    "${{DMG_PO}}":"Poison",
    "${{DMG_PS}}":"Psychic",
    "${{DMG_RA}}":"Radiant",
    "${{DMG_SL}}":"Slashing",
    "${{DMG_TH}}":"Thunder",
    "${{FAERUN}}":"Faerûn",
}


coinColors = {
    "sheen":{
        "PP":"#f2f2f2",
        "GP":"#fffabf",
        "EP":"#e7f5d7",
        "SP":"#d0d3e5",
        "CP":"#ff9f4d",
    },
    "LIGHT_COLOUR":{
        "PP":"#cfdede",
        "GP":"#ffde54",
        "EP":"#b6d6a0",
        "SP":"#bfbfd4",
        "CP":"#d67622",
    },
    "MID_COLOUR":{
        "PP":"#a9bfc4",
        "GP":"#ffba47",
        "EP":"#9dba90",
        "SP":"#a7a7b7",
        "CP":"#ba4900",
    },
    "DARK_COLOUR":{
        "PP":"#9daeb2",
        "GP":"#db914c",
        "EP":"#879e80",
        "SP":"#9392a1",
        "CP":"#a33e17",
    }
}

rarityColours = {
    "COMMON":{
        "CARD_LIGHT_COLOUR":"#e6e6f0",
        "CARD_MID_COLOUR":  "#c6c7de",
        "CARD_DARK_COLOUR": "#9a99ba",

        "CARD_BODY_LIGHT_COLOUR":"#e6e6f0",
        "CARD_BODY_DARK_COLOUR": "#9a99ba",

        "CARD_BASE_COLOUR":"#454661"
    },
    "UNCOMMON":{
        "CARD_LIGHT_COLOUR":"#57cf93",
        "CARD_MID_COLOUR":  "#41a358",
        "CARD_DARK_COLOUR": "#3c6343",

        "CARD_BODY_LIGHT_COLOUR":"#d1ffeb",
        "CARD_BODY_DARK_COLOUR": "#41a358",

        "CARD_BASE_COLOUR":"#26402c"
    },
    "RARE":{
        "CARD_LIGHT_COLOUR":"#73f0e9",
        "CARD_MID_COLOUR":  "#41bfe8",
        "CARD_DARK_COLOUR": "#2889cc",

        "CARD_BODY_LIGHT_COLOUR":"#f2f2ff",
        "CARD_BODY_DARK_COLOUR": "#41bfe8",

        "CARD_BASE_COLOUR":"#1b2447"
    },
    "VERY_RARE":{
        "CARD_LIGHT_COLOUR":"#f5a1a6",
        "CARD_MID_COLOUR":  "#e37286",
        "CARD_DARK_COLOUR": "#b25365",

        "CARD_BODY_LIGHT_COLOUR":"#fcc7c7",
        "CARD_BODY_DARK_COLOUR": "#e37286",

        "CARD_BASE_COLOUR":"#472635"
    },
    "LEGENDARY":{
        "CARD_LIGHT_COLOUR":"#fca46f",
        "CARD_MID_COLOUR":  "#f2631f",
        "CARD_DARK_COLOUR": "#ba441e",

        "CARD_BODY_LIGHT_COLOUR":"#ffe0b8",
        "CARD_BODY_DARK_COLOUR": "#f2631f",

        "CARD_BASE_COLOUR":"#2e1c1f"
    },
    "UNIDENTIFIED":{
        "CARD_LIGHT_COLOUR":"#ceaaed",
        "CARD_MID_COLOUR":  "#9c8adb",
        "CARD_DARK_COLOUR": "#7966c7",

        "CARD_BODY_LIGHT_COLOUR":"#fad6ff",
        "CARD_BODY_DARK_COLOUR": "#9c8adb",

        "CARD_BASE_COLOUR":"#292547"
    },
    "CURSED":{
        "CARD_LIGHT_COLOUR":"#ceaaed",
        "CARD_MID_COLOUR":  "#9c8adb",
        "CARD_DARK_COLOUR": "#7966c7",

        "CARD_BODY_LIGHT_COLOUR":"#d1ffeb",
        "CARD_BODY_DARK_COLOUR": "#41a358",

        "CARD_BASE_COLOUR":"#292547"
    }
}

itemTypeColors = {
    "WEAPON": {
        "BASE_COLOUR":coinColors["DARK_COLOUR"]["PP"],
        "LIGHT_COLOUR":coinColors["MID_COLOUR"]["PP"],
        "MID_COLOUR": coinColors["LIGHT_COLOUR"]["PP"],
        "DARK_COLOUR": coinColors["MID_COLOUR"]["PP"]
    },
    "POTION":{
        "BASE_COLOUR":coinColors["DARK_COLOUR"]["EP"],
        "LIGHT_COLOUR":coinColors["MID_COLOUR"]["EP"],
        "MID_COLOUR": coinColors["LIGHT_COLOUR"]["EP"],
        "DARK_COLOUR": coinColors["MID_COLOUR"]["EP"]
    },
    "ARMOUR": {
        "BASE_COLOUR":coinColors["DARK_COLOUR"]["CP"],
        "LIGHT_COLOUR":coinColors["MID_COLOUR"]["CP"],
        "MID_COLOUR": coinColors["LIGHT_COLOUR"]["CP"],
        "DARK_COLOUR": coinColors["MID_COLOUR"]["CP"]
    },
    "ITEM": {
        "BASE_COLOUR":coinColors["DARK_COLOUR"]["GP"],
        "LIGHT_COLOUR":coinColors["MID_COLOUR"]["GP"],
        "MID_COLOUR": coinColors["LIGHT_COLOUR"]["GP"],
        "DARK_COLOUR": coinColors["MID_COLOUR"]["GP"]
    }
}

itemTypeIconPaths = {
    "WEAPON":"./svg-icons/sword.svg",
    "ARMOUR":"./svg-icons/shield.svg",
    "POTION":"./svg-icons/potion.svg",
    "ITEM":"./svg-icons/item.svg"
}

itemTypeIcons = {
}

for itemType in itemTypes:
    with open(itemTypeIconPaths[itemType]) as f:
        svg = f.read()
        while "200mm" in svg:
            svg = svg.replace("200mm", "30mm")
        while "#000000" in svg:
            svg = svg.replace("#000000", itemTypeColors[itemType]["DARK_COLOUR"])
        svg = svg.replace("<svg","<svg class=\"card-back-icon\"")
        itemTypeIcons[itemType] = svg
        f.close()

attributeList = [
    "Damage",
    "Range",
    "Charges",
    "Ammo",
    "Healing",
    "AC"
]

propertiesList = {
    "Focus","Attuned","Light","Versatile","Two‑Handed","Thrown","Finesse","Loading","Heavy","Reach"
}

outText = ""

print("Generating cards")
for index, row in frame.iterrows():

    cardHtml = templateFile

    name = row["Name"]
    cardType = row["Type"]
    cardRarity = row["Rarity"]
    cost = row["Cost"]
    coin = row["Coin"]
    cardDesc = row["Desc"]
    itemType = row["Back"]

    cardHtml = cardHtml.replace("${{CARD_TITLE}}",name)
    cardHtml = cardHtml.replace("${{CARD_TYPE}}",cardType)
    cardHtml = cardHtml.replace("${{CARD_NUMBER}}",str(index))
    cardHtml = cardHtml.replace("${{CARD_BODY}}", cardDesc)

    cardHtml = cardHtml.replace("${{CARD_BASE_COLOUR}}", "card-base-"+cardRarity.lower())
    cardHtml = cardHtml.replace("${{CARD_HEADER_COLOUR}}", "card-header-"+cardRarity.lower())
    cardHtml = cardHtml.replace("${{CARD_TITLE_COLOUR}}", "card-title-"+cardRarity.lower())
    cardHtml = cardHtml.replace("${{CARD_FOOTER_COLOUR}}", "card-footer-"+cardRarity.lower())
    cardHtml = cardHtml.replace("${{CARD_BODY_COLOUR}}", "card-body-"+cardRarity.lower())

    if (str(cost) != "nan"):
        costHtml = costFile
        costHtml = costHtml.replace("${{CARD_COST}}", str(int(cost)))
        costHtml = costHtml.replace("${{CARD_COIN}}", str(coin))
        costHtml = costHtml.replace("${{COIN_COLOUR_CLASS}}", "coin-colour-"+coin.lower())
        costHtml = costHtml.replace("${{COIN_SHEEN}}", coinColors['sheen'][coin]).replace("${{COIN_SHEEN}}", coinColors['sheen'][coin])
        cardHtml = cardHtml.replace("${{CARD_COST}}", costHtml)
    else:
        cardHtml = cardHtml.replace("${{CARD_COST}}", "")

    attributeHtml = ""
    propertyString = ""

    if (row["IndentifyNo"] != None):
        if (str(row["IndentifyNo"]) != "nan"):
            if (row["IndentifyNo"] != ""):
                propertyString = "#"+str(int(row["IndentifyNo"]))

    for property in propertiesList:
        if (row[property] != None):
            if (row[property] == "T"):
                if (len(propertyString) == 0):
                    propertyString = property
                else:
                    propertyString += ", "+property

    cardHtml = cardHtml.replace("${{CARD_PROPERTIES}}",propertyString)
    

    for attribute in attributeList:
        if (row[attribute] != None):
            if (str(row[attribute]) != "nan"):
                rowValue = row[attribute]
                if (type(rowValue) == float):
                    rowValue = int(rowValue)
                
                rowValue = str(rowValue)

                newAttributeHtml = '<div class="card-attribute ${{ATTRIBUTE_COLOUR}}"><div class="card-attribute-name">${{ATTRIBUTE_NAME}}:</div><div class="card-attribute-value">${{ATTRIBUTE_VALUE}}</div></div>'
                newAttributeHtml = newAttributeHtml.replace("${{ATTRIBUTE_NAME}}",attribute)
                newAttributeHtml = newAttributeHtml.replace("${{ATTRIBUTE_VALUE}}", rowValue)
                newAttributeHtml = newAttributeHtml.replace("${{ATTRIBUTE_COLOUR}}","card-attribute-"+cardRarity.lower())
                attributeHtml += newAttributeHtml
    cardHtml = cardHtml.replace("${{ATTRIBUTES}}", attributeHtml)

    cardHtml = cardHtml.replace("${{CARD_BACK_TYPE}}", "card-type-"+itemType.lower())
    cardHtml = cardHtml.replace("${{CARD_BACK_ICON}}", itemTypeIcons[itemType])
    cardHtml = cardHtml.replace("${{CARD_BACK_CIRCLE}}", "card-type-circle-"+itemType.lower())

    outText += "\n"
    outText += cardHtml

for key in replacements.keys():
    while (key in outText):
        outText = outText.replace(key, replacements[key])

indexFile = indexFile.replace("${{REPLACE_ME}}", outText)


with open("./index.html", "w") as f:
    f.write(indexFile)
    f.close()


print("Done")

cssText = cssTemplate




print("Generating CSS")

for rarity in rarities:
    rarityCss = cssRarityTemplate

    while "${{rarity}}" in rarityCss:
        rarityCss = rarityCss.replace("${{rarity}}", rarity.lower())
    while "${{RARITY}}" in rarityCss:
        rarityCss = rarityCss.replace("${{RARITY}}", rarity)
    
    cssText += "\n" + rarityCss

for coin in coins:
    coinCss = cssCoinTemplate

    while "${{coin}}" in coinCss:
        coinCss = coinCss.replace("${{coin}}", coin.lower())
    while "${{COIN}}" in coinCss:
        coinCss = coinCss.replace("${{COIN}}", coin)
    
    cssText += "\n" + coinCss

for itemType in itemTypes:
    backCss = cssBackTemplate
    while "${{type}}" in backCss:
        backCss = backCss.replace("${{type}}", itemType.lower())
    while "${{TYPE}}" in backCss:
        backCss = backCss.replace("${{TYPE}}", itemType)
    
    cssText += "\n" + backCss


for coin in coins:
    for coinReplacement in coinReplacements:
        key = "${{"+coin+"_"+coinReplacement+"}}"

        while key in cssText:
            cssText = cssText.replace(key, coinColors[coinReplacement][coin])


for itemType in itemTypes:
    for colour in itemTypeColors[itemType]:
        key = '${{'+itemType+"_"+colour+"}}"
        print(key)
        while key in cssText:
            cssText = cssText.replace(key, itemTypeColors[itemType][colour])


for rarity in rarities:
    for colour in rarityColours[rarity]:
        key = '${{'+rarity+"_"+colour+'}}'
        
        while key in cssText:
            cssText = cssText.replace(key, rarityColours[rarity][colour])




with open("./index.css", "w") as f:
    f.write(cssText)
    f.close()

print("Done")