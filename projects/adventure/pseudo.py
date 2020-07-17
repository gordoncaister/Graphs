"""
#####
#                                        #
#      017       002       014           #
#       |         |         |            #
#       |         |         |            #
#      016--015--001--012--013           #
#                 |                      #
#                 |                      #
#      008--007--000--003--004           #
#       |         |                      #
#       |         |                      #
#      009       005                     #
#       |         |                      #
#       |         |                      #
#      010--011--006                     #
#                                        #

write logic directly in adv.py, using a while loop.

travel in a single direction for as long as possible.
Once you reach the maximum distance, travel in a different direction



Map the whole graph. Get every possible edge, and every possible path between two numbers. Store in dictionary

travel in a direction, marking that direction as travelled for that vertex in a dictionary. once you can no longer travel any more. Look for the closest vertex that has a missing direction. travel in that missing direction for as long as possible. rinse and repeat. 


get list of all possible directions from each node: {0: {'n': 1, 's': 5, 'e': 3, 'w': 7},}
build an unexplored list of every possible node: {0: {'n': '?', 's': '?', 'e': '?', 'w': '?'}}
build a graph with all connections being two way: {0, [(0,1),(0,3),(0,5),(0,7)],}
build a list of all possible routes from each number to each number

start at 0:
go north until you can't go anymore.
turn around go back to the closest vertex that has an unexplored direction, head in that direction until you can't anymore
repeat until you've visited every vertex


 - add_friendship
 - add_user
 - populate_graph

 - get_all_social_paths:
    Takes a rooms's room.id as an argument

    Returns a dictionary containing every room in that room's
    extended network with the shortest friendship path between them.

    The key is the friend's ID and the value is the path.
    for each vertex in all_neighbours:
        for destination_vertex in all_neighbours:
            if vertex != destination_vertex: 
                find the shortest path from vertex to destination_vertex
                add to dictionary of dictionaries.
                Key is vertex, value is : key is destination_vertex value is shortest path
            
    
 - bft
 - bfs
visited = {}
possible_directions: {0: {'n': 1, 's': 5, 'e': 3, 'w': 7}, 1: {'s': 0, 'n': 2}, 2: {'s': 1}, 3: {'w': 0, 'e': 4}, 4: {'w': 3}, 5: {'n': 0, 's': 6}, 6: {'n': 5}, 7: {'w': 8, 'e': 0}, 8: {'e': 7}}
explored_directions: {0: {'n': '?', 's': '?', 'e': '?', 'w': '?'}, 1: {'s': '?', 'n': '?'}, 2: {'s': '?'}, 3: {'w': '?', 'e': '?'}, 4: {'w': '?'}, 5: {'n': '?', 's': '?'}, 6: {'n': '?'}, 7: {'w': '?', 'e': '?'}, 8: {'e': '?'}}
all_neighbours: {0: {1, 3, 5, 7}, 1: {0, 2}, 2: {1}, 3: {0, 4}, 4: {3}, 5: {0, 6}, 6: {5}, 7: {8, 0}, 8: {7}}
shortest_paths: {(0, 1): [0, 1], (0, 2): [0, 1, 2], (0, 3): [0, 3], (0, 4): [0, 3, 4], (0, 5): [0, 5], (0, 6): [0, 5, 6], (0, 7): [0, 7], (0, 8): [0, 7, 8], (1, 0): [1, 0], (1, 2): [1, 2], (1, 3): [1, 0, 3], (1, 4): [1, 0, 3, 4], (1, 5): [1, 0, 5], (1, 6): [1, 0, 5, 6], (1, 7): [1, 0, 7], (1, 8): [1, 0, 7, 8], (2, 0): [2, 1, 0], (2, 1): [2, 1], (2, 3): [2, 1, 0, 3], (2, 4): [2, 1, 0, 3, 4], (2, 5): [2, 1, 0, 5], (2, 6): [2, 1, 0, 5, 6], (2, 7): [2, 1, 0, 7], (2, 8): [2, 1, 0, 7, 8], (3, 
0): [3, 0], (3, 1): [3, 0, 1], (3, 2): [3, 0, 1, 2], (3, 4): [3, 4], (3, 5): [3, 0, 5], (3, 6): [3, 0, 5, 6], (3, 7): [3, 0, 7], (3, 8): [3, 0, 7, 8], (4, 0): [4, 3, 0], (4, 1): [4, 3, 0, 1], (4, 2): [4, 3, 0, 1, 2], (4, 3): [4, 3], (4, 5): [4, 3, 0, 5], (4, 6): [4, 3, 0, 5, 6], (4, 7): [4, 3, 0, 7], (4, 8): [4, 3, 0, 7, 8], (5, 0): [5, 0], (5, 1): [5, 0, 1], (5, 2): [5, 0, 1, 2], (5, 3): [5, 0, 3], (5, 4): [5, 0, 3, 4], (5, 6): [5, 6], (5, 7): [5, 0, 7], (5, 8): [5, 0, 7, 8], (6, 0): [6, 5, 0], (6, 1): [6, 5, 0, 1], (6, 2): [6, 5, 0, 1, 2], (6, 3): [6, 5, 0, 3], (6, 4): [6, 5, 0, 3, 4], (6, 5): [6, 5], (6, 7): [6, 5, 0, 7], (6, 8): [6, 5, 0, 7, 8], (7, 0): [7, 0], (7, 1): [7, 0, 1], (7, 2): [7, 0, 1, 2], (7, 3): [7, 0, 3], (7, 4): [7, 0, 3, 4], (7, 5): [7, 0, 5], (7, 6): [7, 0, 5, 6], (7, 8): [7, 8], (8, 0): [8, 7, 0], (8, 1): [8, 7, 0, 1], (8, 2): [8, 7, 0, 1, 2], (8, 3): [8, 7, 0, 3], (8, 4): [8, 7, 0, 3, 4], (8, 5): [8, 7, 0, 5], (8, 
6): [8, 7, 0, 5, 6], (8, 7): [8, 7]}
traversal_path = []
changedirection = {"n":"w", "w":"e", "e":"s", "s":"n"}
start at 0
start going n

while length of visited is less than length of possible directions or world_graph:
    if explored_directions[currentroom][current direction] == ?:
        travel in current direction
        add current direction to traversal path

    if explored_directions[currentroom].values() contains "?":
        if explored_directions[currentroom][changedirection[currentdir]] == "?":
            currdir = changedirection[currentdir]
    else:
        find closest vertex with a "?"




closest unexplored vertex (vertex, shortest_paths):
    curr_length: 1:
    for each key in shortest_paths[vertex]:
        if length of shortest_paths[vertex][key] less than or = current length:
            if explored_directions[key].values() contains ?:
                move from current position to explored_directions[key]
    increase current_length

(8): [7, 0, 1, 2]

steps for traversal(currroom,path):
    result = []
    for index in range(len(path)):
        for direction in possible_directions[currroom]:
            if possible_directions[currroom][direction] == path[i]:
                result.append(direction)
    return result
        
        



while the length of the fully explored is length than the possible directions:
    if explored_directions[currroom] does not contain ?:
        fully_explored[currroom] = True
    if the currroom has a room in the currentdirection:
        if that room is not in the fully_explored list:
            update the explored_directions for the current room with the room in current direction
            move to that room
        else:
            find the closest unexplored room from the current room
            steps_to_traversal(curroom, bfs(currroom, closest_unexplored))
    else: 
        change currentdirection

*** Everytime I make a step I need to add the previous room to the new rooms list of directions as well as the new room to the previous rooms.
"""