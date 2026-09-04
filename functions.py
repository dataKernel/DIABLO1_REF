import game_data

statsData = game_data.stats

def     get_stats():
    pass

def     get_base_stats(className=None):
    pass
def     get_per_lvl_up(className=None):
    pass

def     get_per_attribute(className=None):
    pass

def     get_res(className=None):
    matrix = []
    resList, valList = [], [] ## Create 2 lists to store 2D info before tuple conversion
    
    if className:
        data = statsData[className]['res']
        
        for key, val in data.items():
            resList.append(key)
            valList.append(val)
        #list convvertion to tuples and add them to the matrix
        matrix.append(tuple(resList))
        matrix.append(tuple(valList))
    else:
        #hashmap for elems display when we need them
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

get_res()