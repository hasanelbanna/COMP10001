from reference import build_cave, shortest_path


def optimal_path(data):
    '''Return the length of the optimal path that 'solves' the cave defined by
    data; ie, collects all treasures and reaches the exit.'''
    # locations of interest
    locations = [data['exit']]
    if 'sword' in data:
        locations.append(data['sword'])
    if 'treasure' in data:
        locations += data['treasure']

    # state = (current_location, visited_locations, has_sword, treasure_count)
    initial_state = (data['entrance'], (), False, 0)

    # total number of treasures to collect
    treasure_max = len(data['treasure']) if 'treasure' in data else 0

    # queue: here a dictionary mapping state to path cost
    queue = {initial_state: 0}

    # while there are still states to be explored
    while queue:
        # get the lowest cost state, remove from the queue and unpack
        cur_state = min(queue, key=queue.get)
        cur_cost = queue.pop(cur_state)
        cur_loc, visited, has_sword, treasure_count = cur_state

        # if we've satisfied the goal conditions (all treasure collected
        # and at exit), return
        if cur_loc == data['exit'] and treasure_count == treasure_max:
            return cur_cost

        # otherwise, explore next locations
        for next_loc in locations:
            # don't revisit an already visited location
            if next_loc in visited:
                continue
            # generate the path to the next location
            cost = shortest_path(data, cur_loc, next_loc, has_sword)
            # continue if no path to the next location
            if cost is None:
                continue
            # otherwise, generate the next state, and add it to the queue
            # if either: (i) it doesn't yet exist; or (ii) it exists, but
            # this is a shorter path
            next_state = (next_loc, visited + (next_loc,),
                          has_sword or
                          ('sword' in data and next_loc == data['sword']),
                          treasure_count + (next_loc in data['treasure']
                                            if 'treasure' in data else 0))
            next_cost = cur_cost + cost
            if next_state not in queue or queue[next_state] > next_cost:
                queue[next_state] = next_cost

    # if queue is empty and we haven't reached goal state
    return None