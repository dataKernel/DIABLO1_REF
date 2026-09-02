import game_data

statsData = game_data.stats

def     get_res(className=None):
    data = statsData[className]
    
    for elem in data:
        print(f"val: {elem}")
    
get_res('war')