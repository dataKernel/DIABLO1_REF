#perLvlUp est le nombre de points gagné par niveau (les resistances sont de 1% pour chacune d'entre elles)
stats = {
    #----------------------------------------------------
    'hash': {
        'war': "Warrior",
        'rog': "Rogue",
        'sorc': "Sorcerer",
        'barb': "Barbarian",
        'hp': "Health",
        'mana': "Mana",
        'str': "Strength",
        'dex': "Dexterity",
        'mag': "Magician",
        'vita': "Vitality"
    },
    #---------------- VANILLA CLASS ---------------------
    'war': {
        'baseStats': {
            'hp': {'min': 70, 'max': 316},
            'mana': {'min': 10, 'max': 50},
            'str': {'min': 30, 'max': 250},
            'dex': {'min': 20, 'max': 60},
            'mag': {'min': 10, 'max': 99},
            'vita': {'min': 25, 'max':100}
        },
        'res': {'fire': 1, 'lightning': 1, 'magic': 1},
        #-----------------------------------------------
        'perLvlUp': {'hp': 2, 'mana': 1, 'res': 1},
        'perAttribute': {
            'vita': {'hp': 2}, 
            'magic': {'mana': 1}
        }
    },
    'rogue': {
        'baseStats': {
            'hp': {'min': 45, 'max': 201},
            'mana': {'min': 22, 'max': 173},
            'str': {'min': 20, 'max': 55},
            'dex': {'min': 30, 'max': 250},
            'mag':{'min': 15, 'max': 70},
            'vita':{'min': 20, 'max':80}
        },
        'res': {'fire': 1, 'lightning': 1, 'magic': 1},
        #-----------------------------------------------
        'perLvlUp': {'hp': 2, 'mana':2, 'res': 1},
        'perAttribute': {
            'vita': {'hp': 1}, 
            'magic': {'mana': 1}
        }
    },
    'sorcerer': {
        'baseStats': {
            'hp': {'min': 30, 'max': 138},
            'mana': {'min': 70, 'max': 596},
            'str': {'min': 15, 'max': 45},
            'dex': {'min': 15, 'max': 85},
            'mag':{'min': 35, 'max': 250},  
            'vita':{'min': 20, 'max':80}
            },
            'res': {'fire': 1, 'lightning': 1, 'magic': 1},
            #-----------------------------------------------
            'perLvlUp': {'hp': 1, 'mana':2, 'res': 1},
            'perAttribute': {
                'vita': {'hp': 1}, 
                'magic': {'mana': 2}
            }},
    #-------------------- HELLFIRE CLASS --------------------
    #(a mettre à jour avec monk)
    'barb': {},
}

classes = {
    'classes': ["Barbarian", "Warrior", "Rogue", "Sorcerer"],
    
    'war': {
        'stats':stats['war']
    }
}
