import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_analyzer(self):
        self.assertEqual(sentiment_analyzer("I love working with Python")[0],"SENT_POSITIVE") # positive
        self.assertEqual(sentiment_analyzer("I hate working with Python")[0],"SENT_NEGATIVE") # negative
        self.assertEqual(sentiment_analyzer("I am neutral on Python")[0],"SENT_NEUTRAL") # neutral

unittest.main()