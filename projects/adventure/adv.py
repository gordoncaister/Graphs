from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
"""
______________________________
Helper functions:
"""


"""
______________________________
World Initialisation:
"""
# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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


roomstack = []
roomstack.append(player.current_room.id)
visitedrooms = set()
while len(visitedrooms) != len(world.rooms):
    currentroom = roomstack[-1]
    visitedrooms.add(currentroom)
    queue = []
    neighbours = room_graph[currentroom][1]
    for room in neighbours.values():
        if room not in visitedrooms:
            print(room)
            queue.append(room)

    if len(queue) > 0:
        nex = queue[0]
        roomstack.append(nex)
    else:
        roomstack.pop()
        nex = roomstack[-1]
        
    for room in neighbours.items():
        if room[1] == nex:
            traversal_path.append(room[0])


print(traversal_path)
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


