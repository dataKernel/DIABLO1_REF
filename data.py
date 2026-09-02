#perLvlUp est le nombre de points gagné par niveau (les resistances sont de 1% pour chacune d'entre elles)
stats = {
    #---------------- VANILLA CLASS ---------------------
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
            'vita':{'min': 20, 'max':80},
            'mag':{'min': 15, 'max': 70}
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
            'vita':{'min': 20, 'max':80},
            'mag':{'min': 35, 'max': 250}  
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

