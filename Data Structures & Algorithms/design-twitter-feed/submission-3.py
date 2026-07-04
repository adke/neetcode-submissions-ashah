class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(list)
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # this should be a list of tweetIds
        curr = []
        currFollowing = self.following[userId]

        if userId not in currFollowing:
            self.following[userId].append(userId)

        for followId in self.following[userId]:
            myTweets = self.tweets[followId]
            if len(myTweets) > 0:
                lastIndex = len(myTweets) - 1
                tweetC, tweetId = myTweets[lastIndex]
                curr.append([tweetC, tweetId, lastIndex, followId])
            else:
                continue

        heapq.heapify(curr)
        while curr and len(res) < 10:
            feedC, feedId, lIndex, fId = heapq.heappop(curr)
            res.append(feedId)
            lIndex -= 1
            if lIndex >= 0: # this means the fId still has more tweets we need to consider
                newC, newId = self.tweets[fId][lIndex]
                heapq.heappush(curr, [newC, newId, lIndex, fId])
            
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        currFollowing = self.following[followerId]
        if followeeId not in currFollowing:
            self.following[followerId].append(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        currFollowing = self.following[followerId]
        if followeeId in currFollowing:
            ind = currFollowing.index(followeeId)
            del currFollowing[ind]
            self.following[followerId] = currFollowing



        
