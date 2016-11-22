import unittest
from unhash import unHash
from webCrawler import getRespKeyword
from webCrawler import getRespPgNum

class PrimesTestCase(unittest.TestCase):
    """Tests for `unhash.py`."""

    def test_unHash_forOutput1(self):
        """Is five successfully determined to be prime?"""
        num = 24590208964559
        expected = "acgilmwu"
        self.assertEqual(expected, unHash(num)) 

    def test_unHash_forOutput2(self):
        num = 930846109532517
        expected = "lawnmower"
        self.assertEqual(expected, unHash(num)) 

    def test_getRespKeyword_forKnownKeyword(self):
        keyword = "TV"
        expected = 1066
        self.assertEqual(expected, getRespKeyword(keyword))

    def test_getRespKeyword_forUnknownKeywword(self):
        keyword ="bdfsjbad"
        expected = -1
        self.assertEqual(expected,getRespKeyword(keyword))

    def test_getRespPgNum_forKnownPgNum(self):
        keyword = 'TV'
        pgNum= 5
        expected = 7
        actual = getRespPgNum(keyword,pgNum)
        self.assertEqual(expected, actual)
    

    def test_getRespPgNum_forZeroPgNum(self):
        keyword ='TV'
        pgNum =0
        expected = -1
        actual = getRespPgNum(keyword,pgNum)
        self.assertEqual(expected,actual)
        #assert 0

    def test_getRespPgNum_forOutOfRangePgNum(self):
        keyword = 'TV'
        pgNum = 100
        expected =-1
        actual = getRespPgNum(keyword, pgNum)
        self.assertEqual(expected, actual)
        #assert 0

    def test_getRespPgNum_forNANPgNum(self):
        keyword = 'TV'
        pgNum= 9.0877
        expected = -1
        actual = getRespPgNum(keyword, pgNum)
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
