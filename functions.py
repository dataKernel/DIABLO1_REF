import game_data

statsData = game_data.stats

def     get_stats():
    pass


def     get_per_lvl_up(className=None):
    pass

def     get_per_attribute(className=None):
    pass

#---------------------- BASE_STATS FUNCTIONS -----------------
def     get_baseStatsClass(className):
    matrix = []
    baseStatList, minVal, maxVal = [], ["min"], ["max"] ## Create 3 lists to store 2D info before tuple conversion
    
    data = statsData[className]['baseStats']
    
    for key, val in data.items():
        # affichage pour recheck les infos: print(f"key:{key} -- data:{val}")
        baseStatList.append(key)
        minVal.append(val['min'])
        maxVal.append(val['max'])   
    matrix.extend([tuple(baseStatList), tuple(minVal), tuple(maxVal)])
    
    return(matrix)

def     get_baseStats():
    pass


#---------------------- RES FUNCTIONS ------------------------
def     get_res(): #faudra refactoriser cte func sans le parcours dynamique de clefs sauf si on est sur que on a énormément de type de res à ajouter
    matrix = []
    resList, valList = [], [] ## Create 2 lists to store 2D info before tuple conversion
    
    check = False
    for keyClass in statsData:
        if keyClass != "hashMap":
            #we add the className first to values
            valList.append(statsData['hashMap'][keyClass])
            for keyRes, valRes in statsData[keyClass]['res'].items():
                if not check:
                    resList.append(keyRes)
                valList.append(valRes)
            check = True
            matrix.append(tuple(valList))
            valList = [] #we reset the list
    matrix.insert(0, tuple(resList))
    
    return(matrix)

def     get_resClass(className):
    matrix = []
    resList, valList = [], [] ## Create 2 lists to store 2D info before tuple conversion
    
    data = statsData[className]['res']
    for key, val in data.items():
        resList.append(key)
        valList.append(val)
    #list convvertion to tuples and add them to the matrix
    matrix.append(tuple(resList))
    matrix.append(tuple(valList))
        
    return(matrix)

print(get_baseStatsClass("war"))
