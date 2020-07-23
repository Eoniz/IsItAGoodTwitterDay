from typing import List

from textblob_fr import PatternAnalyzer, PatternTagger, positive, polarity


from itagtd.domain.entity.trend_tweets import TrendTweets
from itagtd.domain.entity.trends_feeling import TrendsFeeling
from itagtd.domain.logic.clean_tweet import clean_tweet
from itagtd.domain.value_object.feeling import Feeling
from itagtd.infrastructure.connector.itagtd_connectors import get_connectors


class TwitterServices:
    @classmethod
    def get_trends(cls) -> List[TrendTweets]:
        connectors = get_connectors()
        return connectors.twitter.get_tweets_for_top_trends()

    @classmethod
    def get_trends_feeling(cls) -> List[TrendsFeeling]:
        connectors = get_connectors()

        trends_tweets = connectors.twitter.get_tweets_for_top_trends()
        results = []
        for trend in trends_tweets:
            if len(trend.tweets):
                polarities = []
                tweets = []
                for tweet in trend.tweets:
                    polarities.append(polarity(clean_tweet(tweet.text)))
                    tweets.append(clean_tweet(tweet.text))

                mean = sum(polarities) / len(polarities)

                if mean > 0:
                    feeling = Feeling.happy
                elif mean < 0:
                    feeling = Feeling.unhappy
                else:
                    feeling = Feeling.neutral

                results.append(TrendsFeeling(
                    trend=trend.trend,
                    feeling=feeling,
                    polarities=polarities,
                    tweets=tweets
                ))

        return results
