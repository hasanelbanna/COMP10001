from reference import build_cave

def check_path(data, path):
    '''A function that takes a data of a cave and a list of path and 
    returns the validity of that path based on the nine given cases'''
    
    # the function returns false if the given cave is invalid itself
    if build_cave(data):
        
        # pathgrid shows the nodes of Falcs's direction
        falca = list(data['entrance'])
        pathgrid = []
        pathgrid.append((falca[0], falca[1]))
        for elem in range(len(path)):
            i=0
            direction = path.pop(i)
            if direction == 'N':
                falca[0] = falca[0] - 1
                falca[1] = falca[1]
            if direction == 'S':
                falca[0] = falca[0] + 1
                falca[1] = falca[1]
            if direction == 'E':
                falca[0] = falca[0]
                falca[1] = falca[1] + 1
            if direction == 'W':
                falca[0] = falca[0]
                falca[1] = falca[1] - 1
            pathgrid.append((falca[0], falca[1]))
            i += 1
        
        # check if Falca only moves one location at a time
        x = []
        y = []
        for i in pathgrid:
            x.append(i[0])
            y.append(i[1])
        xdif = [x[i + 1] - x[i] for i in range(len(x) - 1)]
        ydif = [y[i + 1] - y[i] for i in range(len(y) - 1)]
        
        # Falca's moves are valid if the differece is between -1 and +1
        for num in xdif:
            if (-1 <= num <= 1) is False:
                return False
        for num in ydif:
            if (-1 <= num <= 1) is False:
                return False
        
        # Falca can not move into a wall
        if 'walls' in data: 
            for i in pathgrid:
                if i in data['walls']:
                    return False
                
        # publishing the features of the cave from the data on the pathgrid
        # features must correspond to the the nodes of the pathgrid
        if 'entrance' in data:
            if data['entrance'] not in pathgrid:
                return False
            else:
                en = data['entrance']
                i = pathgrid.index(en)
                pathgrid[i] = '@'
    
        if 'exit' in data:
            if data['exit'] not in pathgrid:
                return False
            else:
                ex = data['exit']
                i = pathgrid.index(ex)
                pathgrid[i] ='X'
    
        if 'sword' in data:
            if data['sword'] not in pathgrid:
                return False
            else:
                sw = data['sword']
                i = pathgrid.index(sw)
                pathgrid[i] ='t'
    
        if 'dragon' in data:
            if data['dragon'] not in pathgrid:
                return False
            else:
                dr = data['dragon']
                i = pathgrid.index(dr)
                pathgrid[i] = 'W'
   
        if 'treasure' in data:
            for i in pathgrid:
                if i in data['walls']:
                    return False
            for tr in data['treasure']:
                i = pathgrid.index(tr)
                pathgrid[i] = '$'         
    
        # Falca can only proceed to dragon or it's adjacent places when 
        # he has the sword
        if 'dragon' in data and 'sword' in data:
            if pathgrid.index('t') > pathgrid.index('W'):
                return False
            if (((sw[0]) == (dr[0])) or ((sw[0]) == (dr[0]) + 1) or
                ((sw[0]) == (dr[0]) - 1)) and (((sw[1]) == (dr[1])) or 
                 ((sw[1]) == (dr[1]) + 1) or ((sw[1]) == (dr[1] - 1))):
                return False
    
        # Falca must collect all the treasures before leaving the cave
        trlist = [i for i, x in enumerate(pathgrid) if x == '$']
        for pos in trlist:
            if pos > pathgrid.index('X'):
                return False
     
        return True
    else:
        return False
