#--- WARRIOR INFOS ---
# Beginning Stats
# Strength	30
# Magic	10
# Dexterity	20
# Vitality	25
# Life	70
# Mana	10

# General
# Life / Level	+2
# Life / Vitality	+2
# Mana / Level	+1
# Mana / Magic	+1

# Maximum Stats
# Strength	250
# Magic	50
# Dexterity	60
# Vitality	100


#perLvlUp est le nombre de points gagné par niveau (les resistances sont de 1% pour chacune d'entre elles)
stats = {
    'attributes': ["Strength", "Dexterity", "Vitality", "Magic"],
    'baseStats': ["Health", "Mana", "Strength", "Dexterity", "Vitality", "Magic"],
    'resistances': ["magic", "fire", "lightning"],
    
    'war': {
        'baseStats': {'hp': 70, 'mana': 10, 'str': 30, 'dex': 20, 'vita': 25, 'mag': 10},
        'maxStats': {'hp': 316, 'mana': 50, 'str': 250, 'dex': 60, 'vita': 100, 'mag': 99},
        'perLvlUp': {'hp': 2, 'mana': 1, 'res': 1},
        'perAttribute': {'vita': {'hp': 2}, 'magic': {'mana': 1}}
    },
    'barb': {
        'attributes': {'hp': 70, 'mana': 0, 'str': 40, 'dex': 20 , 'vita': 25, 'mag': 0},
        'maxStats': {'hp': 416, 'mana': 0, 'str': 255, 'dex': 55,'vita': 150, 'mag': 0},
        'perLvlUp': {'hp': 2, 'mana': 0, 'res': 1},
        'perAttribute': {'vita': 2}   
    },
}

classes = {
    'classes': ["Barbarian", "Warrior", "Rogue", "Sorcerer"],
    
    'war': {
        'stats':stats['war']
    }
}

print(f"check stats_class_war: {classes['war']['stats']}")