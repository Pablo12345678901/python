
"""
babe = []
a = '1'
babe.append(a)
#b = "20"
b = '2'
babe.append(b)
print(f"len(babe) : {len(babe)}")
print(f"babe[0] : {babe[0]}")
print(f"babe[1] : {babe[1]}")

for i in range(len(babe)):
    print(f"{babe[i]},", end="")
print()
print("".join(babe))
"""
NIVEAU_DIFFICUTE = (
	{
		"titre": "Facile",
		"longueur_initiale": 3,
		"duree_memorisation": 4,
		"increment_sequence" : 2,
		"nombre_vies_restantes" : 3,
	},
# 1er niveau du dictionnaire
	{
		"titre": "Facile",
		"longueur_initiale": 3,
		"duree_memorisation": 4,
		"increment_sequence" : 2,
		"nombre_vies_restantes" : 3,
	},
# 2ème niveau du dictionnaire (...)
	)

print(f"{NIVEAU_DIFFICUTE[0]['titre']}")