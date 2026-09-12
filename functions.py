# --data imports--
import  data.common as commonData
from data.stats import stats as statsData
# --global definition--




def     get_stats():
    pass

#---------------------- PER_LEVEL & PER_ATTRIBUTE FUNCTIONS -----------------
def     get_perAttribute_class(className:str):
   data = statsData[className]['perAttribute']
   
   attributes, stats = [], []

def     get_perLvl(className:str):
    pass


#---------------------- BASE_STATS FUNCTIONS -----------------
def     get_baseStats_class(className:str) -> list[tuple]:
    matrix = []
    baseStatsList, minVal, maxVal = [], ["min"], ["max"] # Create 3 lists to store 2D info before tuple conversion
    data = statsData[className]['baseStats']
    
    for key, val in data.items():
        # affichage pour recheck les infos: print(f"key:{key} -- data:{val}")
        baseStatsList.append(key)
        minVal.append(val['min'])
        maxVal.append(val['max'])   
    matrix.extend([tuple(baseStatsList), tuple(minVal), tuple(maxVal)])
    
    return(matrix)

def     get_baseStats():
    matrix = []
    baseStatsList, valList = list(statsData['war']['baseStats'].keys()), [] # Create 2 lists to store 2D info in matrix before tuple conversion 
    for keyClass in statsData:
        valList.append(commonData.hashmap[keyClass])
        for valBaseStats in statsData[keyClass]['baseStats'].values():
            val = f"min: {valBaseStats['min']}, max: {valBaseStats['max']}"
            valList.append(val)
        matrix.append(tuple(valList))
        valList = []# we reset the list
    matrix.insert(0, tuple(baseStatsList))
    
    return(matrix)
    

#---------------------- RES FUNCTIONS ------------------------
def     get_res():
    matrix = []
    resList, valList = list(statsData['war']['res'].keys()), [] # Create 2 lists to store 2D info before tuple conversion
    
    for keyClass in statsData:
        # we add the className first to values
        valList.append(commonData.hashmap[keyClass])
        for valRes in statsData[keyClass]['res'].values():
            valList.append(valRes)
        matrix.append(tuple(valList))
        valList = [] #we reset the list
    matrix.insert(0, tuple(resList))
    
    return(matrix)

def     get_res_class(className):
    resData = statsData[className]['res']# we get the data for resistances
    matrix = []
    # Create 2 lists to store 2D info before tuple conversion
    resList, valList = tuple(resData.keys()), tuple(resData.values())
    matrix.append(resList)
    matrix.append(valList)
        
    return(matrix)

# get_perAttribute_class("war")
print(get_res_class("war"))
