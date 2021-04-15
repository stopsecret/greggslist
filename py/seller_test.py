import unittest
from seller import seller

class test_seller_validation(unittest.TestCase):
    def test_can_create(self):
        seller("", "", "", [], False, "", "")

class test_seller_properties(unittest.TestCase):
    new_seller = seller("John Doe", "jdoe@doe.com", "", [], False, "", "")
    def test_rating(self):
            ratings = self.listing.ratings
            value = 0
            for rating in ratings:
                value += ratings[rating]
            value = value/len(ratings)
            actual_value = self.listing.get_rating()
            self.assertEqual(value, actual_value)