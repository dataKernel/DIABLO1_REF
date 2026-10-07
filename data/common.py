from typing import TypedDict
#------------------------ HASHMAP -----------------------
hashmap = {
    #-- CLASSES --
    'war': "Warrior",
    'rog': "Rogue",
    'sorc': "\033[38;5;27mSorcerer\033[0m",
    'barb': "\033[38;5;124mBarbarian\033[0m",
    #-- BASE STATS --
    'hp': "Health",
    'mana': "Mana",
    'str': "Strength",
    'dex': "Dexterity",
    'vita': "Vitality",
    #-- RESISTS --
    'fire': "\033[38;5;196mFire\033[0m",
    'lightning': "\033[38;5;226mLightning\033[0m",
    'magic': "\033[38;5;129mMagic\033[0m"
}

colors = {
    'war': "\033[38;5;130m",
    'rog': "\033[38;5;34m",
    
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