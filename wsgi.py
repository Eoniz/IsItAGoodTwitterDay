# from textblob import TextBlob# from textblob_fr import PatternAnalyzer, PatternTagger, positive, polarity## text_english = '''What a good morning'''## text = u"Quelle belle matinée"# blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())# blob_english = TextBlob(text_english)## print(positive(text))from os.path import dirnamefrom itagtd.infrastructure.configuration.configuration import init_configurationfrom itagtd.infrastructure.twitter.twitter_client import TwitterClientroot_dir = dirname(__file__)config = init_configuration(root=root_dir)twitter_client = TwitterClient(    consumer_key=config.secrets.twitter.consumer_key,    access_key=config.secrets.twitter.access_key,    consumer_secret=config.secrets.twitter.consumer_secret,    access_secret=config.secrets.twitter.access_secret,    bearer="",)a = twitter_client.get_tweets_for_top_trends()print(a)b = twitter_client.get_tweets_for_top_trends()print(b)