stats = {
    'baseStats': ["Health", "Mana", "Strengh", "Dexterity", "Magic"],
    
    'barb': [100, 0, 42, 25, 0],
    'war': [100, 75, 25, 15, 5]
}

#création des "objets" vide
barbStats = {}
warStats = {}

baseStats = stats['baseStats']
#insertion des datas dans les objets
for i in range(len(stats['baseStats'])):
    barbStats[baseStats[i]] = stats['barb'][i]


print(f"barbStats: {barbStats}")
