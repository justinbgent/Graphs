class User:
    def __init__(self, name):
        self.name = name

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

import random 

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
        # Write a for loop that calls create user the right amount
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        #To create N random friendships, you could create a list with all possible friendship combinations, shuffle
        #the list, then grab the first N elements from the list. You will need to import random to get shuffle.

        #stuff
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id +1, self.last_id +1):
                possible_friendships.append((user_id, friend_id))
      
        random.shuffle(possible_friendships)

        #friendships = possible_friendships[:]
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for id in self.users:
            connection = self.bfs(user_id, id)
            if connection:
                visited[id] = connection
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create a queue
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            # Check if it's been visited
            # If it hasn't been visited...
                # Mark it as visited
                # CHECK IF IT'S THE TARGET
                    # IF SO, RETURN THE PATH
                # Enqueue A PATH TO all it's neighbors
                    # MAKE A COPY OF THE PATH
                    # ENQUEUE THE COPY
            if path[-1] not in visited:
                visited.add(path[-1])
                if path[-1] == destination_vertex:
                    return path
                for friend in self.friendships[path[-1]]:
                    new_path = list(path)
                    new_path.append(friend)
                    q.enqueue(new_path)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
