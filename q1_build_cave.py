def build_cave(data):
    """Takes a dictionary representing cave's information and returns a 2D grid
    representation of the cave based on the given cases or 'None' if the 
    dictionary contains a non-valid cave"""
    
    # append the locations in the node_list to check it's validity
    node_list = []
    for i in data.values():
        if type(i) is tuple:
            node_list.append(i)
        if type(i) is list:
            for j in i:
                node_list.append(j)
                
    # check if any node doesn't contain non-negative values 
    for node in node_list:
        if node[0]< 0 or node[0] > data['size'] - 1 or node[1]< 0 or \
            node[1] > data['size'] - 1:
            return None 
    
    # 2D representation of the empty cave when it doesn't have a feature
    cave = [['.' for j in range(data['size'])] for i in range(data['size'])]  
    
    # cave must contain a single entry and a single exit         
    if 'entrance' in data and 'exit' in data:  
        en = data['entrance']
        cave[en[0]][en[1]] ='@'
        ex = data['exit']
        cave[ex[0]][ex[1]] ='X'
    else:    
        return None
    
    # represent an existing sword in the cave if there is one    
    if 'sword' in data:
        sw = data['sword']
        cave[sw[0]][sw[1]] ='t'
        
    # represent the existing walls in the cave if there are any 
    if 'walls' in data:
        for wall in data['walls']:
            cave[wall[0]][wall[1]] ='#'
            
    # represent the treasures in the cave if there are 3 at most 
    if 'treasure' in data:
        if len(data['treasure']) > 3:
            return None
        else:
            for tr in data['treasure']:
                    cave[tr[0]][tr[1]] = '$'
                    
    # a dragon if exists can not be located adjacent to the entrance
    if 'dragon' in data:  
        dr = data['dragon']      
        if (((en[0]) == (dr[0])) or ((en[0]) == (dr[0]) + 1) or
            ((en[0]) == (dr[0]) - 1)) and (((en[1]) == (dr[1])) or 
             ((en[1]) == (dr[1]) + 1) or ((en[1]) == (dr[1] - 1))):
            return None
        else:
            cave[dr[0]][dr[1]] = 'W'
               
    return cave

