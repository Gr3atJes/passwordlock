import unittest
import pyperclip
from credential import Credential

class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours

    Args:
        unittest.TestCase : Inherits the testCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credential("Github","user101","user101@email","QwerY23")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.platform,"Github")
        self.assertEqual(self.new_credential.username,"user101")
        self.assertEqual(self.new_credential.email,"user101@email")
        self.assertEqual(self.new_credential.password,"QwerY23")

    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saved into
        """
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credential.credential_list), 1)

    def tearDown(self):
        """
        tearDown method that cleans up after each test caase has run.
        """
        Credential.credential_list = []

    def test_save_multiple_contact(self):
        """
        test_save_multiple_credentials to check if we can save multiple credential objects to our credential list
        """
        