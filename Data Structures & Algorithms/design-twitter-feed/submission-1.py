class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []

        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                currCount, currTweet = self.tweetMap[followee][index]
                maxHeap.append([currCount, currTweet, followee, index - 1])

        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            count, tweet, followeeID, index = heapq.heappop(maxHeap)
            res.append(tweet)

            if index >= 0:
                currCount, currTweet = self.tweetMap[followeeID][index]
                heapq.heappush(maxHeap, [currCount, currTweet, followeeID, index - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
