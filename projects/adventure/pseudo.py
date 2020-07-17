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




"""