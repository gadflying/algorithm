EMPTY_SET = set()

class FriendshipService:
    def __init__(self):
        self.followers = {}
        self.followings = {}

    def get_followers(self, user_id):
        return self.getFollowers(user_id)
    def get_followings(self, user_id):
        return self.getFollowings(user_id)

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    def getFollowers(self, user_id):
        return [
            id for id in sorted(self.followers[user_id])
        ] if user_id in self.followers else []

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    def getFollowings(self, user_id):
        return [
            id for id in sorted(self.followings[user_id])
        ] if user_id in self.followings else []

    """
    @param: to_user_id: An integer
    @param: from_user_id: An integer
    @return: nothing
    """
    def follow(self, to_user_id, from_user_id):
        if from_user_id not in self.followings:
            self.followings[from_user_id] = set()
        self.followings[from_user_id].add(to_user_id)
        if to_user_id not in self.followers:
            self.followers[to_user_id] = set()
        self.followers[to_user_id].add(from_user_id)

    """
    @param: to_user_id: An integer
    @param: from_user_id: An integer
    @return: nothing
    """
    def unfollow(self, to_user_id, from_user_id):
        if to_user_id in self.followings.get(from_user_id, EMPTY_SET):
            self.followings[from_user_id].remove(to_user_id)
        if from_user_id in self.followers.get(to_user_id, EMPTY_SET):
            self.followers[to_user_id].remove(from_user_id)