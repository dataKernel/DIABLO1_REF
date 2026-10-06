from typing import TypedDict

#------------------------ HASHMAP -----------------------
hashmap = {
    'classes': 
    {
        'war': '\033[31mWarrior\033[0m',
        'rog': '\033[33mRogue\033[0m',
        'sorc': '\033[35mSorcerer\033[0m',
        'barb': '\033[34mBarbarian\033[0m'
    },
    'stats':
    {    
        'hp': "Health",
        'mana': "Mana",
        'str': "Strength",
        'dex': "Dexterity",
        'vita': "Vitality"
    }
    ,
    'resists':
    {
        'fire': "\033[31mFire\033[0m",
        'lightning': '\033[33mLightning\033[0m',
        'magic': '\033[35mMagic\033[0m'
    }
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