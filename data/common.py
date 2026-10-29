from typing import TypedDict

#------ STRUCT TYPED DICT -----------------------------------
#--- low layer definitions ---
class   colorsData(TypedDict):
    #-- CLASS --
    war: str
    rog: str
    sorc: str
    #-- BASE STATS --
    hp: str
    mana: str
    str: str
    dex: str
    magic: str
    vita: str
    res: str
    #-- RES --
    fire: str
    lightning: str
    #--------------------------
    reset: str

#------------------------ HASHMAP -----------------------
hashmap = {
    #-- CLASSES --
    'war': "Warrior",
    'rog': "Rogue",
    'sorc': "Sorcerer",
    'barb': "Barbarian",
    #-- BASE STATS --
    'hp': "Health",
    'mana': "Mana",
    'str': "Strength",
    'dex': "Dexterity",
    'magic': "Magic",
    'vita': "Vitality",
    #-- RESISTS --
    'fire': "\033[38;5;196mFire\033[0m",
    'lightning': "\033[38;5;226mLightning\033[0m",
    'magic': "\033[38;5;129mMagic\033[0m"
}

colors: colorsData = {
    #-- CLASSES --
    'war': "\033[38;5;130m",
    'rog': "\033[38;5;40m",
    'sorc': "\033[38;5;129m",

    #-- BASE STATS --
    'hp': "\033[38;5;196m",
    'mana': "\033[38;5;27m",
    'str': "\033[38;5;130m",
    'dex': "\033[38;5;40m",
    'magic': "\033[38;5;129m",
    'vita': "\033[38;5;208m",
    'res': "\033[38;5;129m",

    #-- RESISTS --
    'fire': "\033[38;5;196m",
    'lightning': "\033[38;5;226m",
    # /!\: on a la clef magic qui correspond à la même couleur pour la stat et la couleur

    #-- RESET --
    'reset': "\033[0m"
}

emojis = {
    'class':
    {
        'war': '⚔️',
        'rog': '🏹',
        'sorc': '🔮'
    },
    'stats':
    {
        'hp': '❤️',
        'mana': '💧',
        'str': '💪',
        'dex': '🎯',
        'magic': '✨',
        'vita': '🫀'
    },
    'resists':
    { 
        'fire': '🔥', 
        'lightning': '🔥', 
        'magic': '✨'
     },
}