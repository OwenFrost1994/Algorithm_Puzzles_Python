from collections import defaultdict
from heapq import nlargest
class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_follows = defaultdict(set)
        self.time = 1
        self.tweets = defaultdict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append(tweetId)
        self.tweets[tweetId] = self.time
 
    def getNewsFeed(self, userId: int):
        follower = self.user_follows[userId].copy()
        follower.add(userId)
        tweets = [self.user_tweets[user][::-1][:10] for user in follower]
        tweets = sum(tweets, [])
        return nlargest(10, tweets, key = lambda tweet: self.tweets[tweet])

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)

twitter = Twitter()
twitter.postTweet(1, 5) # User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1) # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2) # User 1 follows user 2.
twitter.postTweet(2, 6) # User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1) # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2) # User 1 unfollows user 2.
twitter.getNewsFeed(1) # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 