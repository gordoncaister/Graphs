import itertools
import random
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """

        
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        i=0
        while i < num_users:
            self.add_user(i+1)
            i += 1
        
        # Create friendships
        combinations = list(itertools.permutations(range(num_users),2))
        random.shuffle(combinations)
        j=0
        while j < (len(combinations)*(avg_friendships/(num_users)))/2:
            self.add_friendship(combinations[j][0]+1,combinations[j][1]+1)
            j+=1
            
            
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        allfriends = self.bft(user_id)
        for u in allfriends:
            visited[u] = self.bfs(user_id,u)
            
        return visited

    def bft(self,user_id):
        q = []
        vis = set()
        result = []
        q.append(user_id)
        while len(q) > 0:
            v = q.pop()
            if v not in vis:
                result.append(v)
                vis.add(v)
                for nv in self.friendships[v]:
                    q.append(nv)
        return result

    def bfs(self, starting_vertex, destination_vertex):
        q = []
        q.append([starting_vertex])
        visited = set()
        while len(q) > 0:
            p = q.pop()
            v = p[-1]
            if v not in visited:
                if v == destination_vertex:
                    return p
                visited.add(v)
                for nv in self.friendships[v]:
                    np  = list(p)
                    np.append(nv)
                    q.append(np)
    
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    connections = sg.get_all_social_paths(4)
    # print("Connections:",connections)
    print(len(connections))