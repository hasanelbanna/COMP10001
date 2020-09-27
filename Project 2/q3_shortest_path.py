def next_to_dragon(node, data):
    ''' A function that determines if a node in a grid is adjacent to dragon
      and returns true when the condition is true otherwise returns false'''
    
    dr = data['dragon']
    return (((node[0]) == (dr[0])) or ((node[0]) == (dr[0]) + 1) or
            ((node[0]) == (dr[0]) - 1)) and (((node[1]) == (dr[1])) or 
             ((node[1]) == (dr[1]) + 1) or ((node[1]) == (dr[1] - 1)))

def next_nodes(node, data, explored):
    '''A function that returns all the possible adjacent nodes for a given
      node in the event of it is not in the explored list'''
    
    # 2D grid representation of the cave
    cave = [(x, y) for x in range(data['size']) for y in range(data['size'])]
    
    wall = data['walls']
    valid_node = []
    
    # add the north/south/east/west direction to the valid_node when it's 
    # in the cave and not a wall 
    n = (node[0] - 1, node[1])
    if n in cave and n not in wall:
        valid_node.append(n)    
        
    s = (node[0] + 1, node[1])
    if s in cave and s not in wall:
        valid_node.append(s)   
        
    e = (node[0], node[1] + 1)
    if e in cave and e not in wall:
        valid_node.append(e)     
        
    w = (node[0], node[1] - 1)
    if w in cave and w not in wall:
        valid_node.append(w)   
    # if any position is already been explored, it becomes invalid    
    for i in valid_node:
        if i in explored: 
            valid_node.remove(i)   
            
    return valid_node

def shortest_path(data, start, end, has_sword):
    '''a function that determines the length of the shortest valid path 
        between two locations in a cave'''
    
    # queue will held all the possible nodes to explore 
    # move determines the path-length from the start
    move = 0
    queue = [(start, move)]
    explored = []   
    
    while queue:
        # the first value from the queue is taken to test if it's the end        
        grid, move = queue.pop()        
        if grid == end:
            return move    
        
        # add that node to the explored list as Falca has visited that place
        explored.append(grid)
        
        # all possible neighbour nodes of the first value of the queue
        neigh = next_nodes(grid, data, explored)
        for i in neigh:
            # Falca can only proceed to dragon or it's adjacent places when 
            # he has the sword
            if i not in queue and i not in explored and \
                ((has_sword is True) or not next_to_dragon(i, data)):
                queue.append((i, move + 1))                        
    return None      