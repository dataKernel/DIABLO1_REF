#perLvlUp est le nombre de points gagné par niveau (les resistances sont de 1% pour chacune d'entre elles)
stats = {
    'baseStats': ["Health", "Mana", "Strength", "Dexterity", "Vitality", "Magic"],
    'resistances': ["magic", "fire", "lightning"],
    
    'barb': {
        'stats': {'hp': 70, 'mana': 0, 'str': 40, 'dex': 20 , 'vit': 25, 'mag': 0},
        'maxStats': {'hp': 416, 'mana': 0, 'str': 255, 'dex': 55,'vit': 150, 'mag': 0},
        'perLvlUp': {'hp': 2, 'mana': 0,'resistances': 1},
        'perAttribute': {'vit': 2}
                
    }
}

classes = {
    'classes': ["Barbarian", "Warrior", "Rogue", "Sorcerer"],
    
    'barb': {
        'stats':stats['barb']
    }
}