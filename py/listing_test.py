import unittest
from listing import listing

class test_listing_validation(unittest.TestCase):
    def can_create(self):
        new_listing = listing()

class test_listing_properties(unittest.TestCase):
    listing = listing( \
        title = "Used $5,000 Ford Escape", \
        description = "Haven't used this much since I got some new wheels", \
        sellerId = "1003", \
        photos = ["img1.jpg", "img2.jpg", "img3.jpg"])

    def test_properties_correct(self):
        self.assertEqual("Used $5,000 Ford Escape", self.listing.title)
        self.assertEqual("Haven't used this much since I got some new wheels", self.listing.description)
        self.assertEqual(3, len(self.listing.photos))
        self.assertEqual("img1.jpg", self.listing.photos[0])
        self.assertEqual("1003", self.listing.sellerId)

    

