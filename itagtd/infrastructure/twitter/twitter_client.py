from typing import Dict, List, Any

import tweepy
from tweepy import OAuthHandler

from itagtd.domain.entity.trend_tweets import TrendTweets
from itagtd.domain.value_object.locations import Location
from itagtd.infrastructure.entity.twitter.trend import Trend
from itagtd.infrastructure.entity.twitter.tweet import Tweet
from itagtd.infrastructure.utils.cache.cache import cache


def _get_tweets_for_top_trends_from_json(json: Any) -> List[TrendTweets]:
    return [
        TrendTweets(**data)
        for data in json
    ]


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

    @cache(cls=_get_tweets_for_top_trends_from_json)
    def get_tweets_for_top_trends(self) -> List[TrendTweets]:
        # twitter_client.search(q="#RCLGNT", lang="fr", result_type="popular")
        trends = [
            Trend(**trend)
            for trend in self.trends_place(id=Location.france.value)[0]["trends"]
        ]

        results = []
        for trend in trends[:2]:
            tweets = self.search(q=trend.query, lang="fr", result_type="popular")
            trend_tweets = []

            for tweet in tweets[:2]:
                trend_tweets.append(Tweet.from_status(tweet))

            results.append(TrendTweets(trend=trend.query, tweets=trend_tweets))

        return results
