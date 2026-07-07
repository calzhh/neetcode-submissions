import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.heap = []
        self.counter = 0
        heapq.heapify(self.heap)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.counter, tweetId])
        self.counter += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.heap.clear()
        res = []
        followingAndSelf = [userId]
        if userId in self.followMap:
            for element in self.followMap[userId]:
                followingAndSelf.append(element)
        for user in list(set(followingAndSelf)):
            for element in self.tweetMap[user]:
                heapq.heappush(self.heap, element)
        while len(self.heap) > 10:
            heapq.heappop(self.heap)
        while len(self.heap) > 0:
            res.append(heapq.heappop(self.heap)[1])
        print(followingAndSelf)
        return res[::-1]
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
#["follow", [8, 7], "follow", [8, 7], "unfollow", [8, 7], "unfollow", [8, 7],]
