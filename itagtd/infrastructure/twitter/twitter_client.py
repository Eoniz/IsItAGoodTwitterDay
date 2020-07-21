import tweepy
from tweepy import OAuthHandler

from itagtd.domain.value_object.locations import Location
from itagtd.infrastructure.entity.twitter.trend import Trend
from itagtd.infrastructure.entity.twitter.tweet import Tweet


class TwitterClient(tweepy.API):
    def __init__(
            self, *,
            consumer_key: str,
            access_key: str,
            consumer_secret: str,
            access_secret: str,
            bearer: str) -> None:

        auth = OAuthHandler(consumer_key, consumer_secret)
        # auth.set_access_token(access_key, access_secret)

        super().__init__(auth)

    def get_tweets_for_top_trends(self):
        # twitter_client.search(q="#RCLGNT", lang="fr", result_type="popular")
        trends = [
            Trend(**trend)
            for trend in self.trends_place(id=Location.france.value)[0]["trends"]
        ]

        # {
        #    query: [ Tweet(), ... ]
        # }

        result = {}
        for trend in trends:
            result[trend.query] = list()

            tweets = self.search(q=trend.query, lang="fr", result_type="popular")
            for tweet in tweets:
                result[trend.query].append(Tweet.from_status(tweet))

        print(trends)