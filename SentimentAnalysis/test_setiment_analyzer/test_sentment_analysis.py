from SentimentAnalysis.sentiment_analyzer import sentiment_analysis

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analysis(self):
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL') 

    unittest.main()