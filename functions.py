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
    data = statsData[className]['res']
    
    matrix = []
    elems, values = [], [] ## Create 2 lists to store 2D info before tuple conversion
    for key, val in data.items():
        elems.append(key)
        values.append(val)
    #list convvertion to tuples and add them to the matrix
    matrix.append(tuple(elems))
    matrix.append(tuple(values))
    
    return(matrix)

m = get_res('war')
print(m)