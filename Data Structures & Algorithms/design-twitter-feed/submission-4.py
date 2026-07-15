class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.social = defaultdict(list)
        self.c = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.c -= 1
        self.tweets[userId].append([self.c, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        # we will add all the most recent tweets from each followee to a heap
        # we will add the userId to the followee list as well 
        if userId not in self.social[userId]:
            self.social[userId].append(userId)
        followees = self.social[userId]
        # we need the tweets of the followees since
        # these are the people the user is following
        heapp = []
        self.remaining = 10
        res = []
        for followee in followees:
            if self.tweets[followee]:
                lastIndex = len(self.tweets[followee]) - 1
                currCount, lastTweet = self.tweets[followee][lastIndex]
                heapp.append([currCount, lastTweet, lastIndex, followee])

        heapq.heapify(heapp)

        while self.remaining != 0 and heapp:
            _, tweetId, lIndex, person = heapq.heappop(heapp)
            res.append(tweetId)
            lIndex -= 1
            if lIndex >= 0:
                newC, newTweet = self.tweets[person][lIndex]
                heapq.heappush(heapp, [newC, newTweet, lIndex, person])
            self.remaining -= 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.social and followeeId in self.social[followerId]:
            return None
        else:
            self.social[followerId].append(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.social and followeeId in self.social[followerId]:
            self.social[followerId].remove(followeeId)
        else:
            return None
        
