//Need to manipulate json data before writing to csv

let data = {
    "\"Ach! Hans, Run!\"": {
        "colorIdentity": [
            "G",
            "R"
        ],
        "colors": [
            "G",
            "R"
        ],
        "convertedManaCost": 6.0,
        "foreignData": [],
        "layout": "normal",
        "legalities": {},
        "manaCost": "{2}{R}{R}{G}{G}",
        "name": "\"Ach! Hans, Run!\"",
        "printings": [
            "UNH"
        ],
        "rulings": [],
        "scryfallId": "84f2c8f5-8e11-4639-b7de-00e4a2cbabee",
        "subtypes": [],
        "supertypes": [],
        "tcgplayerProductId": 37816,
        "tcgplayerPurchaseUrl": "https://mtgjson.com/links/85b366724beadefd",
        "text": "At the beginning of your upkeep, you may say \"Ach Hans, run It\'s the . . .\" and the name of a creature card. If you do, search your library for a card with that name, put it onto the battlefield, then shuffle your library. That creature gains haste. Exile it at the beginning of the next end step.",
        "type": "Enchantment",
        "types": [
            "Enchantment"
        ],
        "uuid": "d4492969-dc3a-5617-bc14-4f15afc12b2b"
    }
}
let jsonKeys = Object.keys(data)

let revisedData = []

jsonKeys.map(key => {
    let newDataFormat = {}
    newDataFormat.name = data[key]['name']
    newDataFormat.manaCost = data[key]['manaCost']
    newDataFormat.CMC = data[key]['convertedManaCost']
    newDataFormat.types = data[key]['types']
    newDataFormat.subtypes = data[key]['subtypes']
    newDataFormat.power = data[key]['power']
    newDataFormat.toughness = data[key]['toughness']
    newDataFormat.printings = data[key]['printings']

    console.log(newDataFormat)
})