# --data imports--
import  data.common as commonData
from data.stats import stats as statsData
# --global definition--

def     get_stats():
    pass

#-----------------PER_LEVEL & PER_ATTRIBUTE FUNCTIONS --------
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
def     get_res() -> list[tuple]:
    matrix = []
    #we add the resistances names in the matrix first
    resList = tuple(statsData['war']['res'].keys())
    matrix.append(resList)
    for keyClass in statsData:
        data = statsData[keyClass]['res']
        valList = list(data.values())
        # we add the className at the begining of valList
        valList.insert(0, commonData.hashmap[keyClass])
        # we add the valList to matrix
        matrix.append(tuple(valList))
    return(matrix)

def     get_res_class(className:str) -> list[tuple]:
    resData = statsData[className]['res']# we get the data for resistances
    matrix = []
    # Create 2 lists to store 2D infos
    resList, valList = tuple(resData.keys()), tuple(resData.values())
    matrix.append(resList)
    matrix.append(valList)
        
    return(matrix)

# get_perAttribute_class("war")
print(get_res())