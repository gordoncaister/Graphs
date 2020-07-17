from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()
changedirection = {"n":"w", "w":"e", "e":"s", "s":"n"}

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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

possible_directions = {}
explored_directions = {}
shortest_paths = {}
all_neighbours = {}
for r in room_graph:
    all_neighbours[r] = []
    possible_directions[r] = room_graph[r][1]
    explored_directions[r] = {}
    for d in room_graph[r][1]:
        all_neighbours[r].append(room_graph[r][1][d])
        explored_directions[r][d] = "?"
print(possible_directions)
print(explored_directions)
print(all_neighbours)

visited = {}
currdir = "n"
print(explored_directions[player.current_room.id])
print("?" in explored_directions[player.current_room.id])
while len(visited) < len(room_graph):
    explored_directions[player.current_room.id][currdir] = "explored"
    if not possible_directions[player.current_room.id][currdir] is None:
        
    for direction in explored_directions[player.current_room.id]:
        if explored_directions[player.current_room.id][direction] == "?":

    visited[player.current_room.id] = all_neighbours[player.current_room.id]

    player.travel(currdir)     
            
# visited = {}
# currdir = "n"
# while len(visited) < len(room_graph):
#     visited[player.current_room.id] = player.current_room.get_exits()
#     if currdir in player.current_room.get_exits():
#         player.travel(currdir)
#     else:
#         break


   




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


# print(len(world.rooms))


        
# print("VISITED:",visited)