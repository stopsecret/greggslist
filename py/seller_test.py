import unittest

class test_seller(unittest.TestCase):
    def test_rating(self):
            ratings = self.listing.ratings
            value = 0
            for rating in ratings:
                value += ratings[rating]
            value = value/len(ratings)
            actual_value = self.listing.get_rating()
            self.assertEqual(value, actual_value)