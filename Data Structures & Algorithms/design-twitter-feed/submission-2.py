class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweet = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # first get the most recent tweets from all the followee's of the user
        # this also includes the user itself
        # then initialize heap and add tweets to the res 
        minHeap = []
        res = []

        self.follows[userId].add(userId)
        for followee in self.follows[userId]:
            if followee in self.tweet:
                index = len(self.tweet[followee]) - 1
                curCount, curTweet = self.tweet[followee][index]
                minHeap.append([curCount, curTweet, followee, index - 1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            heapCount, heapTweet, heapFollowee, heapIndex = heapq.heappop(minHeap)
            res.append(heapTweet) 

            if heapIndex >= 0:
                nextCount, nextTweet = self.tweet[heapFollowee][heapIndex]
                heapq.heappush(minHeap, [nextCount, nextTweet, heapFollowee, heapIndex - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        else:
            return None
