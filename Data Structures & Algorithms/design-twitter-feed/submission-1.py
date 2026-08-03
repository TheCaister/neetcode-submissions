# for follow, could be hashmap user to hashset for quick addition and removal...?
# are tweet IDs strictly increasing? seems like it
# so the follow actually plays a role. We need to pull from a pool that contains user tweets and
# follower tweets. can't we just use a stack, and get the highest tweet id when building up
# the list?

class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append(tweetId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        heapq.heapify(maxHeap)
        eligibleTweetUsers = [userId, *self.followMap[userId]]
        tweetPool = []

        # print(self.followMap[userId])

        # add frontier of self, then add frontier of all followers
        # id first, then follower ID, then index to get to the next ID
        for user in eligibleTweetUsers:
            if user in self.tweetMap:
                userTweets = self.tweetMap[user]
                tweetPool.append(userTweets)
                heapq.heappush(maxHeap, (-userTweets[-1], user, len(userTweets) - 1))

        while maxHeap and len(res) < 10:
            latestTweetId, latestTweetUser, latestTweetIndex = heapq.heappop(maxHeap)
            newTweetIndex = latestTweetIndex - 1

            if newTweetIndex >= 0:
                nextTweet = self.tweetMap[latestTweetUser][newTweetIndex]
                heapq.heappush(maxHeap, (-nextTweet, latestTweetUser, newTweetIndex))
            
            res.append(-latestTweetId)
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
