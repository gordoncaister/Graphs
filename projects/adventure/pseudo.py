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
"""