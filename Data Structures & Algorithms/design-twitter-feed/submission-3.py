class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.counter, tweetId))
        self.counter += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        people = [userId]
        people += self.following[userId]

        tweets = []

        for person in people: 
            if len(self.tweets[person]) > 0: 
                heapq.heappush(tweets, (-self.tweets[person][-1][0], self.tweets[person][-1][1], 1, person))
            
        feed = []
        while tweets and len(feed) < 10: 
            c, tweet, idx, person = heapq.heappop(tweets)
            idx+=1
            index = len(self.tweets[person])-idx
            if index >= 0: 
                heapq.heappush(tweets, (-self.tweets[person][index][0], self.tweets[person][index][1], idx, person))

            feed.append(tweet)

        return feed


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId: 

            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]: 
            self.following[followerId].remove(followeeId)
        
        
