# Disabled until a new feed provider is available
#
# """
# Test Feed Parser
# """
#
# import os.path
# import sys
# import unittest
#
# from sickchill.sickbeard.providers.binsearch import provider as binsearch
# import requests
#
#
# class FeedParserTests(unittest.TestCase):
#     """
#     Test feed parser
#     """
#     @unittest.skipIf(not requests.head(binsearch.urls['rss'], timeout=30).ok, 'BinSearch is unavailable')
#     def test_binsearch(self):
#         """
#         Test BinSearch
#         """
#         result = binsearch.cache.get_rss_feed(binsearch.urls['rss'], params={'max': 50, 'g': 'alt.binaries.hdtv'})
#         self.assertTrue('entries' in result)
#         self.assertTrue('feed' in result)
#         for item in result['entries'] or []:
#             title, url = binsearch._get_title_and_url(item)
#             self.assertTrue(title and url)
#
# if __name__ == "__main__":
#     print("==================")
#     print("STARTING - FEED PARSER TESTS")
#     print("==================")
#     print("######################################################################")
#     SUITE = unittest.TestLoader().loadTestsFromTestCase(FeedParserTests)
#     TEST_RESULTS = unittest.TextTestRunner(verbosity=2).run(SUITE)
#
#     # Return 0 if successful, 1 if there was a failure
#     sys.exit(not TEST_RESULTS.wasSuccessful())
