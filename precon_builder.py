import xml.etree.ElementTree as ET
import os
import fnmatch

xmlSetFileList = []
idNumberDict = {}
idNameDict = {}

for root, dir, files in os.walk("./055c536f-adba-4bc2-acbf-9aefb9756046/Sets/"):
        for file in files:
            if file.endswith('.xml'):
                xmlSetFileList.append(root + '/' + file)

for xmlFileSet in xmlSetFileList:
    root = ET.parse(xmlFileSet).getroot()
    cardSection = root.find('cards')
    cards = cardSection.findall('card')
    for card in cards:
        cardId = card.attrib['id']
        cardName = card.attrib['name']
        properties = card.findall('property')
        for property in properties:
            if 'name' in property.attrib and property.attrib['name'] == 'CardNumber':
                cardNumber = property.attrib['value']
        if cardId not in idNumberDict:
            idNumberDict[cardId] = cardNumber
            idNameDict[cardId] = cardName


fromFile = 'rocket-raccoon-precon-1.0.o8d'
tree = ET.parse(fromFile)

deck = tree.getroot()
section = deck.find('section')
cards = section.findall('card')
for card in cards:
    cardId = card.attrib['id']
    print('"{}": {},\t# {}'.format(idNumberDict[cardId], card.attrib['qty'], idNameDict[cardId]))
    pass