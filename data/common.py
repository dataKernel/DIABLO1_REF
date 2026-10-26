from typing import TypedDict

#------ STRUCT TYPED DICT -----------------------------------
#--- low layer definitions ---
class   colorsData(TypedDict):
    war: str
    rog: str
    sorc: str
    fire: str
    lightning: str
    magic: str
    hp: str
    mana: str
    str: str
    dex: str
    magic: str
    vita: str
    reset: str

#------------------------ HASHMAP -----------------------
hashmap = {
    #-- CLASSES --
    'war': "Warrior",
    'rog': "Rogue",
    'sorc': "Sorcerer",
    'barb': "\033[38;5;124mBarbarian\033[0m",
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
    'rog': "\033[38;5;34m",
    'sorc': "\033[38;5;27m",
    #-- RESISTS --
    'fire': "\033[38;5;196m",
    'lightning': "\033[38;5;226m",
    'magic': "\033[38;5;129m",
    #-- BASE STATS --
    'hp': "\033[38;5;196m",
    'mana': "\033[38;5;39m",
    'str': "\033[38;5;130m",
    'dex': "\033[38;5;46m",
    'magic': "\033[38;5;201m",
    'vita': "\033[38;5;220m",
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