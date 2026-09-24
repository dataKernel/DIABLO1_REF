# --data imports--
from data.stats import stats
# --global definition--

def     get_stats():
    pass

#-----------------PER_LEVEL & PER_ATTRIBUTE FUNCTIONS --------
def     get_stats_perAttribute_class(className:str) -> list[tuple]:
    data = stats[className]['perAttribute']
    matrix = []
    attributes, statsPerAttributes = tuple(data.keys()), tuple(data.values())
    # we iterate and add the real value of the key from hashmap
    matrix.append(tuple(attributes))
    matrix.append(statsPerAttributes)
   
    return(matrix)

def     get_stats_perAttribute() -> list[tuple]:
    matrix = []
    attributes, statsPerAttributes = tuple(stats['war']['perAttribute'].keys()), []
    
    matrix.append(attributes)
    #we iterate trough each classes to get datas
    for keyClass in stats:
        statsPerAttributes.append(keyClass)
        values = list(stats[keyClass]['perAttribute'].values())
        statsPerAttributes.extend(values)# we add the the values from attributes after the class Name
        matrix.append(tuple(statsPerAttributes))
        statsPerAttributes = []
    
    return(matrix)

def     get_stats_perLvlUp_class(className:str) -> list[tuple]:
    data = stats[className]['perLvlUp']
    matrix = []
    statsPerLvlUp, valStats = tuple(data.keys()), tuple(data.values())
    
    matrix.extend([statsPerLvlUp, valStats])
    
    return(matrix)

def     get_stats_perLvlUp() -> list[tuple]:
    matrix = []
    
    
    return(matrix)

#---------------------- BASE_STATS FUNCTIONS -----------------

def     get_baseStats() -> list[tuple]:
    matrix = []
    baseStatsList, valList = tuple(stats['war']['baseStats'].keys()), [] # Create 2 lists to store 2D info in matrix before tuple conversion 
    matrix.append(baseStatsList)
    for keyClass in stats:
        valList.append(keyClass)
        for valBaseStats in stats[keyClass]['baseStats'].values():
            val = f"min: {valBaseStats['min']}, max: {valBaseStats['max']}"
            valList.append(val)
        matrix.append(tuple(valList))
        valList = []# we reset the list
    #matrix.insert(0, baseStatsList)
    
    return(matrix)
    
def     get_baseStats_class(className:str) -> list[tuple]:
    data = stats[className]['baseStats']
    matrix = []
    # Create 3 lists to store 2D info before tuple conversion
    baseStatsList, minVal, maxVal = tuple(data.keys()), ["min"], ["max"] 
    
    for val in data.values():
        minVal.append(val['min'])
        maxVal.append(val['max'])
    # extend all lists at once for this function       
    matrix.extend([baseStatsList, tuple(minVal), tuple(maxVal)])
    
    return(matrix)
#---------------------- RES FUNCTIONS ------------------------
def     get_resists() -> list[tuple]:
    matrix = []
    # we get the resistances names (directly as tuple)
    resists = tuple(stats['war']['res'].keys())
    matrix.append(resists)# we add the resist list in the matrix
    for keyClass in stats:
        data = stats[keyClass]['res']
        
        valsResists = [keyClass]
        vals = list(data.values())# we get the resists values
        valsResists.extend(vals)
        matrix.append(tuple(valsResists))# tuple convertion
  
    return(matrix)

def     get_resists_class(className:str) -> list[tuple]:
    data = stats[className]['res']# we get the data for resistances
    matrix = []
    # Create 2 lists to store 2D infos
    resists, valResists = tuple(data.keys()), tuple(data.values())
    matrix.append(resists)
    matrix.append(valResists)
        
    return(matrix)

print(get_resists())