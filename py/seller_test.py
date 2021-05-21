import unittest
from .seller import seller
from copy import deepcopy

class test_seller_validation(unittest.TestCase):

    def test_can_create(self):
        seller("John Doe", "jdoe@doe.com", "lambdaPass312@", {})

    def test_cannot_create_empty_username(self):
        self.assertRaises(Exception, 
        lambda: seller("", "jdoe@doe.com", "lambdaPass312@", {}))

    def test_cannot_create_no_username(self):
        self.assertRaises(Exception, 
        lambda: seller(None, "jdoe@doe.com", "lambdaPass312@", {}))
    
    def test_cannot_create_empty_password(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", "", {}))

    def test_cannot_create_no_password(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", None, {}))

    def test_cannot_contain_common_passwords(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", "Qwerty", {}))
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", "Test123", {}))
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", "passwordJonnyBoy", {}))

    def test_password_cannot_be_too_short(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", "Q#1", {}))

    def test_password_must_have_number(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", "lambdaPass@", {}))

    def test_password_must_have_special_character(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", "lambdaPass312", {}))

    def test_cannot_contain_common_passwords(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", "Qwerty", {}))
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", "Test123", {}))
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "jdoe@doe.com", "passwordJonnyBoy", {}))
        
    def test_password_was_hashed(self):
        new_seller = seller("John Doe", "jdoe@doe.com", "lambdaPass312@", {})
        self.assertNotEqual(new_seller.password, "lambdaPass312@")

    def test_cannot_create_empty_email(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "", "", {}))

    def test_cannot_create_no_email(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe", None, "", {}))

    def test_cannot_create_name_too_long(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe Really Long Naming Test John Doe Really Long Naming Test", "jdoe@doe.com", "", {}))

    def test_cannot_create_email_not_valid(self):
        self.assertRaises(Exception, 
        lambda: seller("John Doe", "@jdoedoecom.", "", {}))

class test_seller_properties(unittest.TestCase):
    new_seller = seller(
        "John Doe", 
        "jdoe@example.com", 
        "thisShouldBeHashed1@", 
        {"someone1@example.com":3, 
         "someone2@example.com":8, 
         "someone3@example.com":10}
        )

    def test_fields(self):
            self.assertEqual(self.new_seller.name, "John Doe")
            self.assertEqual(self.new_seller.email, "jdoe@example.com")
            self.assertTrue(self.new_seller.check_password("thisShouldBeHashed1@", self.new_seller.password))

    def test_rating(self):
            self.assertEqual(self.new_seller.get_rating(), 7)
        
    def test_adding_rating(self):
            rating_seller = deepcopy(self.new_seller)
            rating_seller.add_update_rating("someone4@example.com", 3)
            self.assertEqual(rating_seller.get_rating(), 6)

    def test_updating_rating(self):
        rating_seller = deepcopy(self.new_seller)
        rating_seller.add_update_rating("someone1@example.com", 9)
        self.assertEqual(rating_seller.get_rating(), 9)