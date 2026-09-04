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
        for key in statsData:
            if key != "hashMap":
                #we add the className first to values
                valList.append(statsData['hashMap'][key])
                for res in statsData[key]['res']:
                    if not check:
                        resList.append(res)
                    valList.append(statsData[key]['res'][res])
            check = True
            
        print(f"elems: {resList}")
        print(f"values: {valList}")
        
    return(matrix)

get_res()