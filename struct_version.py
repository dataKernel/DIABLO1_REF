struct_stats = {
    'baseStats': ["Health", "Mana", "Strengh", "Dexterity", "Magic"]
}

data_stats = {
    #pas besoin d'avoir les noms exacts pour ces clefs (usage dev)
    'barb': [100, 0, 42, 25, 0],
    'war': [100, 75, 25, 15, 5]
}
#création des "objets" vide
barbStats = {}
warStats = {}

baseStats = struct_stats['baseStats']
#insertion des datas dans les objets
for i in range(len(struct_stats['baseStats'])):
    barbStats[baseStats[i]] = data_stats['barb'][i]


print(f"barbStats: {barbStats}")
