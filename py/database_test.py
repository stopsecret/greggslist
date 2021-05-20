import unittest
from .database import database
from .seller import seller
from .listing import listing

class test_database(unittest.TestCase):

    db = database("testdatabase")
    test_seller = seller("John Doe", "jdoe@doe.com", "lambdaPass312@", {})
    test_listing = listing(0, "Leather Couch", "", "", [], 0, 0)

    def test_adding_and_getting_seller(self):
        self.db.add_update_seller(self.test_seller)
        seller = self.db.get_seller("jdoe@doe.com")
        self.assertIsNotNone(seller)
        self.assertEqual(seller.name, "John Doe")

    def test_adding_and_updating_seller(self):
        self.db.add_update_seller(self.test_seller)
        seller = self.db.get_seller("jdoe@doe.com")
        seller.name = "John Grisham"
        self.db.add_update_seller(seller)
        self.assertEqual(self.db.get_seller("jdoe@doe.com").name, "John Grisham")

    def test_adding_and_removing_seller(self):
        self.db.add_update_seller(self.test_seller)
        seller = self.db.get_seller("jdoe@doe.com")
        self.assertIsNotNone(seller)
        self.db.remove_seller(seller.email)
        self.assertIsNone(self.db.get_seller("jdoe@doe.com"))

    def test_adding_and_getting_listing(self):
        self.db.add_update_listing(self.test_listing)
        listing = self.db.get_listing(0)
        self.assertIsNotNone(listing)
        self.assertEqual(listing.title, "Leather Couch")

    def test_adding_and_updating_listing(self):
        self.db.add_update_listing(self.test_listing)
        listing = self.db.get_listing(0)
        listing.title = "Used Couch"
        self.db.add_update_listing(listing)
        self.assertEqual(self.db.get_listing(0).title, "Used Couch")

    def test_adding_and_removing_listing(self):
        self.db.add_update_listing(self.test_listing)
        listing = self.db.get_listing(0)
        self.assertIsNotNone(listing)
        self.db.remove_listing(0)
        self.assertIsNone(self.db.get_listing(0))

    def test_saving_and_loading(self):
        self.db.load()
        self.db.add_update_listing(self.test_listing)
        listing = self.db.get_listing(0)
        listing.title = "Test A"
        self.db.add_update_listing(listing)
        self.db.save()
        listing.title = "Test B"
        self.db.add_update_listing(listing)
        self.db.load()
        listing = self.db.get_listing(0)
        print(listing)
        self.assertEqual(listing.title, "Test A")