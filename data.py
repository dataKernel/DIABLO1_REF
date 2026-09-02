#perLvlUp est le nombre de points gagné par niveau (les resistances sont de 1% pour chacune d'entre elles)
stats = {
    'war': {
        'baseStats': { 
            'hp': {'min': 70, 'max': 316},
            'mana': {'min': 10, 'max': 50},
            'str': {'min': 30, 'max': 250},
            'dex': {'min': 20, 'max': 60},
            'vita': {'min': 25, 'max':100},
            'mag': {'min': 10, 'max': 99}
        },
        'res': {'fire': 1, 'lightning': 1, 'magic': 1},
        
        'perLvlUp': {'hp': 2, 'mana': 1, 'res': 1},
        'perAttribute': {
            'vita': {'hp': 2}, 
            'magic': {'mana': 1}
        }
    },
    'rogue': {
        'baseStats': {'hp': 45, 'mana': 22, 'str': 20, 'dex': 30, 'vita': 20, 'mag': 15},
        'maxStats': {'hp': 201, 'mana': 173, 'str': 55, 'dex': 250, 'vita': 80, 'mag': 70},
        'perLvlUp': {'hp': 2, 'mana':2, 'res': 1},
        'perAttribute': {'vita': {'hp': 1}, 'magic': {'mana': 1}}
    },
    'sorcerer': {},
    #--- HELLFIRE CLASS ---
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


def displayStatsTable(title, dataDict):
    """Affiche un tableau propre qui s'adapte à la taille du dictionnaire fourni"""
    print(f"\n{'=' * 10} {title.upper()} {'=' * 10}")
    
    for key, value in dataDict.items():
        # Si la valeur est elle-même un dictionnaire (ex: toutes les catégories)
        if isinstance(value, dict):
            print(f"\n[ {key.upper()} ]")
            for subKey, subValue in value.items():
                print(f"  {subKey.capitalize():<12} : {subValue}")
        else:
            # Affichage plat classique (aligné à gauche sur 12 caractères)
            print(f"{key.capitalize():<12} : {value}")
            
    print("=" * (22 + len(title)))

