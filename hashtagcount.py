message = "#japan #japanese #japantravel #traveller #traveling #travelblog #japantrip #asiatravel #asiatrip #japanstyle #travelblogger #travelphotography #photography #photographer #travelasia #visitjapan #wanderlust"

print(hello)

count = {}

for in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1

print(pprint.pformat(count))



