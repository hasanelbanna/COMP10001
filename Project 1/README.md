## Foundations of Computing (UniMelb COMP10001) Final Project

# Introduction

We often use computers to discover efficient solutions to problems. Artificial intelligence provides a range of techniques for solving a wide variety of problems. In this project, you will implement two techniques for solving a search problem.

Often when developing and demonstrating AI techniques, we use "toy worlds": simplified problems for which a concise, exact definition is possible. This is in contrast to "real world" problems, which are often much messier.

The "toy world" scenario that we will use for this project is as follows:

# Bring me the treasure!

Falca (a lesser known cousin of Frodo) has ventured into a cave to collect the treasure that lies therein. This cave can be represented as a two-dimensional grid, completely enclosed by stone walls. Falca arrives at the entrance to the cave, and must locate all of the treasure it contains (a known quantity) before departing from the cave exit (a separate location to the entrance).

Unfortunately, the cave is occupied by a dragon, who will not allow Falca to pass unless armed with a sword. Falca hasn't come prepared with a sword, but there is usually one to be found somewhere in the cave.

We want to help Falca discover the most efficient route from entrance to exit that collects all the treasure along the way.

Note that this is similar to the type of problem a navigation application might need to solve in order to provide efficient directions to a destination, or that a delivery company might need to solve in order to deliver parcels efficiently. Hopefully, it is also a little bit entertaining!

## Toy world

The overall problem to solve is to identify the shortest path through an arbitrary cave that will enable Falca to collect all of the treasure and escape from the exit.

We will break this down into several tasks.

    Creating a representation of the cave
    Checking whether a given path is a valid solution to the problem
    Identifying the shortest path between two points in the cave
    Identifying the optimal (best) path that solves the whole problem


## Question 1: Build Cave

A valid cave satisfies the following requirements:

    There will only ever be (at most) a single feature (entrance, exit, wall, sword, dragon or treasure) in any given location in the cave.

    There will always be a single entrance and a single exit in the cave.

    There may be (at most) a single sword in the cave.

    There may be (at most) a single dragon in the cave.

    There may be (at most) three treasures in a cave.

    There may be multiple walls in a cave.

    A dragon, if one is present, will never be located in one of the locations (up to eight) adjacent to the entrance.

Note that a valid cave may contain no sword, dragon, treasures and/or walls.

A cave is specified via a dictionary with the following structure:


data = {
  'size': 4,  # the size of the cave
  'entrance': (0, 0),  # the location of the entrance (a row-column tuple)
  'exit': (2, 1),  # the location of the exit
  'dragon': (0, 2),  # the location of the dragon
  'sword': (3, 3),  # the location of the sword
  'treasure': [(1, 3)],  # a list of treasure locations
  'walls': [(1, 1), (1, 2), (2, 2), (2, 3)]  # a list of wall locations
}

The different types of location in the cave are identified with different symbols.

    'empty 'is denoted by '.';
    'wall' is denoted by '#';
    'entrance 'is denoted by '@';
    'exit 'is denoted by 'X';
    'treasure' is denoted by a '$';
    'sword' is denoted by 't'; and
    'dragon' is denoted by 'W'.


## Question 2: Check Path

Your next task is to determine whether a given path is a valid solution to the problem. Note that, at this stage, you don't need to determine whether the path is shortest possible path, simply that it doesn't break any of the following rules:

    Falca begins at the entrance.

    Falca can only move one location at a time; eg, from (0, 0) to (1, 0).

    Falca can only move North (up), South (down), West (left) or East (right); ie, diagonal moves are not allowed.

    Falca can never move off the edge of the size-by-size grid constituting the cave.

    Falca can never move into a location containing a cave wall ('#').

    Falca cannot move into a location containing a dragon ('W') or any of the eight locations adjacent to a dragon (ie, including diagonally adjacent) unless carrying the sword ('t'), in which case it is considered equivalent to an empty location.

    Falca must end at the exit ('X'), after having collected all of the the treasures ('$') in the cave. Until all of the treasures have been collected, the exit location is equivalent to an empty location ('.'); ie, Falca may freely move into and out of it.

    For Question 2, any item (treasure or sword) in the location currently occupied by Falca is considered to be collected, and no items are ever dropped.

    Note that if the sword is in one of the (up to) eight locations adjacent to a dragon, then it cannot be collected, as Falca may not move into a location adjacent to a dragon unless already carrying the sword!

For example a valid path through the cave shown in Question 1 would be ['S', 'S', 'S', 'E', 'E', 'E', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E', 'E', 'S', 'N', 'W', 'W', 'W', 'S', 'S', 'E']. 

## Question 3: Shortest Path

Your next problem is to identify the length of the shortest valid path between two locations in a cave. The solution will be the minimum number of valid moves required to move form the start location to the end location. We will formulate this problem as a search problem and solve it using an algorithm known as breadth-first search.

A search process is often visualised as a tree structure: we begin at the root node of our tree, corresponding to the the initial state of the problem, with Falca at the start location. We then add branches corresponding to each of the possible moves from the entrance. Each of these child nodes then corresponds to the new state of the problem after that move has been executed. We are trying to identify a path to the node corresponding to the goal of the problem, with Falca at the end location.

For example, if our root node corresponds to the state of Falca just having entered the cave at (0, 0), there are only two possible moves that can be executed: South or East, resulting in new child nodes corresponding to the state of Falca having moved to (1, 0) or (0, 1) respectively. The next set of child nodes can then be created based on the valid moves available from that location.