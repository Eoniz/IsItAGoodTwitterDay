from typing import List

from fastapi import APIRouter

from itagtd.domain.entity.trend_tweets import TrendTweets
from itagtd.domain.entity.trends_feeling import TrendsFeeling
from itagtd.domain.service.twitter.twitter import TwitterServices

router = APIRouter()


@router.get("/trends/", response_model=List[TrendTweets])
async def get_trends():
    return TwitterServices.get_trends()


@router.get("/feeling/", response_model=List[TrendsFeeling])
async def get_trends_feeling():
    return TwitterServices.get_trends_feeling()
