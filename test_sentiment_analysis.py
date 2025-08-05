from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestAssertions(unittest.TestCase):
    def test_statementAnalysis(self):
        label , score = sentiment_analyzer("I love working with Python")
        self.assertEqual(label, "SENT_POSITIVE")

        def test_statementAnalysis(self):
            label , score = sentiment_analyzer("I hate working with Python")
            self.assertEqual(label, "SENT_NEGATIVE")

        def test_statementAnalysis(self):
            label , score = sentiment_analyzer("I am neutral on Python")
            self.assertEqual(label, "SENT_NEUTRAL")


if __name__ == '__main__':
    unittest.main()


