from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
"""
______________________________
Helper functions:
"""
def bfs(vertex, destination_vertex):
    
    q = []
    q.append([vertex])
    visited = set()
    while len(q) > 0:
        p = q.pop()
        v = p[-1]
        if v not in visited:
            if v == destination_vertex:
                
                p.remove(vertex)
                return p
            visited.add(v)
            for nv in all_neighbours[v]:
                np = list(p)
                np.append(nv)
                q.append(np)

def closest_unexplored(vertex,shortest_paths):
    
    currlength = 1
    for key in shortest_paths[vertex]:
        if len(shortest_paths[vertex][key]) <= currlength:
            if "?" in explored_directions[key[1]].values():
                    return shortest_paths[vertex][key]
        currlength += 1

def steps_for_traversal(currentroom, path):
    result = []
    for i in range(len(path)):
        for d in possible_directions[currentroom]:
            if possible_directions[currentroom][d] == path[i]:
                result.append(d)
        currentroom = path[i]
    return result

"""
______________________________
World Initialisation:
"""
# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# Print an ASCII map
world.print_rooms()
player = Player(world.starting_room)


"""
______________________________
Variables
"""
traversal_path = []
possible_directions = {}
explored_directions = {}
shortest_paths = {}
all_neighbours = {}
fully_explored = {}
currdir = "n"
currroom = 0
changedirection = {"n":"w", "w":"e", "e":"s", "s":"n"}
oppdirection = {"n":"s", "w":"e", "e":"w", "s":"n"}

"""
______________________________
build out direction and neighbour graphs
"""
for r in room_graph:
    all_neighbours[r] = set()
    possible_directions[r] = room_graph[r][1]
    explored_directions[r] = {}
    for d in room_graph[r][1]:
        all_neighbours[r].add(room_graph[r][1][d])
        explored_directions[r][d] = "?"
# print(possible_directions)
# print(explored_directions)
# print(all_neighbours)


# print(explored_directions[player.current_room.id])
# print("?" in explored_directions[player.current_room.id])
"""
______________________________
build out all shortest paths
"""
for vertex in all_neighbours:
    shortest_paths[vertex] = {}
    for destination_vertex in all_neighbours:
        if vertex != destination_vertex:
            shortest_path = bfs(vertex,destination_vertex)
            shortest_paths[vertex][(vertex, destination_vertex)] = shortest_path

# print("Here:",closest_unexplored(0,shortest_paths))

"""
______________________________
main logic
"""
# print(steps_for_traversal(8,[7, 0, 1, 2]))
# while len(fully_explored) < len(possible_directions):
for i in range(20):
    print(currroom,currdir,possible_directions[currroom])
    if not "?" in explored_directions[currroom].values():
                fully_explored[currroom] = True
    if currdir in possible_directions[currroom]:
        if not possible_directions[currroom][currdir] in fully_explored:
            explored_directions[currroom][currdir] = possible_directions[currroom][currdir]
            explored_directions[possible_directions[currroom][currdir]][oppdirection[currdir]] = currroom
            
            currroom = possible_directions[currroom][currdir]
            traversal_path.append(currdir)
        else:
            closest = closest_unexplored(currroom,shortest_paths)
            steps = steps_for_traversal(currroom,closest)
            for step in steps:
                traversal_path.append(step)
    else:
        currdir = changedirection[currdir]


"""
______________________________

Operating code, existed already
______________________________
"""

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


