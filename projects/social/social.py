import random
from statistics import mean


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

        possible_friendships = []
        for _ in range(num_users):
            self.add_user(self.last_id + 1)
            for j in range(self.last_id, num_users):
                possible_friendships.append((self.last_id, j + 1, ))
        random.shuffle(possible_friendships)

        # To create 100 users with an average of 10 friends each, you would
        # have to call add_friendship() 500 times; a friendship links two
        # people, so the calculation is the number of users times the average
        # number of friends divided by two.
        number_of_friendships = ((avg_friendships * num_users) // 2)

        for friendship in possible_friendships[:number_of_friendships]:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        visited[user_id] = [user_id]
        finished = []
        remaining = []
        while True:
            remaining = [key for key in visited.keys() if key not in finished]
            if len(remaining) == 0:
                break
            for user in remaining:
                for friend in self.friendships[user]:
                    if friend not in visited:
                        visited[friend] = visited[user] + [friend]
                finished.append(user)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    # Looks like about 99% of users are in a particular user's extended social
    # network, and that the average degree of separation between a user and
    # those in his or her extended social network is less than 6.
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    connections = sg.get_all_social_paths(500)
    print(len(connections))
    print(mean([len(connections[key]) for key in connections]))
