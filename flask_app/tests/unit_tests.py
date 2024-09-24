import unittest
import test_utils 

class TestPostgreSQL(unittest.TestCase):
    def test_fetch_articles(self):
        version = test_utils.post_rest_call(self, 'http://localhost:5000/manage/fetchData')
        self.assertEqual({"message": "Success"},version)