# --data imports--
from data.common import hashmap
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
    resList = tuple(stats['war']['res'].keys())
    for keyClass in stats:
        data = stats[keyClass]['res']# we get the class resist datas
        valList = list(data.values())
        # we add the className at the begining of valList
        valList.insert(0, keyClass)
        # we add the elems and vals to matrix
        matrix.append(tuple(valList))
    matrix.insert(0, resList)
    
    return(matrix)

def     get_resists_class(className:str) -> list[tuple]:
    resData = stats[className]['res']# we get the data for resistances
    matrix = []
    # Create 2 lists to store 2D infos
    resList, valList = tuple(resData.keys()), tuple(resData.values())
    matrix.append(resList)
    matrix.append(valList)
        
    return(matrix)

print(get_baseStats())