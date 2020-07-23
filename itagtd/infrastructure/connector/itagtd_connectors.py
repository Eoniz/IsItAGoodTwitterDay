from typing import Optional

from itagtd.infrastructure.configuration.configuration import Configuration, get_configuration
from itagtd.infrastructure.connector.twitter_connector import TwitterConnector


class ITAGTDConnectors:
    def __init__(self):
        config: Configuration = get_configuration()

        self.twitter: TwitterConnector = TwitterConnector(
            consumer_key=config.secrets.twitter.consumer_key,
            access_key=config.secrets.twitter.access_key,
            consumer_secret=config.secrets.twitter.consumer_secret,
            access_secret=config.secrets.twitter.access_secret,
            bearer="",
        )


__connectors: Optional[ITAGTDConnectors] = None


def init_connectors() -> ITAGTDConnectors:
    global __connectors
    if __connectors is not None:
        raise ValueError("Duplicate instanciation ! Please use get_connectors() function.")

    __connectors = ITAGTDConnectors()
    return __connectors


def get_connectors() -> ITAGTDConnectors:
    global __connectors
    if __connectors is None:
        raise ValueError("Connectors is not instanciated. Please use init_connectors() before calling this function.")

    return __connectors
