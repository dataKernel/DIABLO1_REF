import  data.common 
import  data.stats

commonData = data.common
statsData = data.stats.stats

def     get_stats():
    pass

def     get_per_lvl_up(className=None):
    pass

def     get_per_attribute(className=None):
    pass

#---------------------- BASE_STATS FUNCTIONS -----------------
def     get_baseStatsClass(className):
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
    baseStatsList, valList = list(statsData['war']['baseStats'].keys()), [] #Create 2 lists to store 2D info in matrix before tuple conversion 
    
    print(f"baseStatList: {baseStatsList}")
    

#---------------------- RES FUNCTIONS ------------------------
def     get_res():
    matrix = []
    resList, valList = list(statsData['war']['res'].keys()), [] #Create 2 lists to store 2D info before tuple conversion
    
    for keyClass in statsData:
        #we add the className first to values
        valList.append(commonData.hashmap[keyClass])
        for valRes in statsData[keyClass]['res'].values():
            valList.append(valRes)
        matrix.append(tuple(valList))
        valList = [] #we reset the list
    matrix.insert(0, tuple(resList))
    
    return(matrix)

def     get_resClass(className):
    matrix = []
    resList, valList = [], [] #Create 2 lists to store 2D info before tuple conversion
    
    data = statsData[className]['res']
    for key, val in data.items():
        resList.append(key)
        valList.append(val)
    #list convvertion to tuples and add them to the matrix
    matrix.append(tuple(resList))
    matrix.append(tuple(valList))
        
    return(matrix)

print(get_res())