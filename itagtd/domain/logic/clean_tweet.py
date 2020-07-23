import re


def clean_tweet(tweet: str) -> str:
    return ' '.join(
        re.sub(
            r"(@[A-Za-z0-9]+)"
            r"|([^0-9A-Za-zÀÁÂÄÅÃÆŒÇÉÈÊËÍÌÎÏÑÓÒÔÖØÕOEÚÙÛÜÝYàâäçéèêëîïôöùûüÿæœ'.,;:!? \t])"
            r"|(\w+:\ / \ / \S+)"
            r"|(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?",
            " ",
            tweet
        ).split()
    )