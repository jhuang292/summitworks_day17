#Testing makes sure your code works properly under a given set of conditions
#Testing allows one to ensure that changes to the code did not break existing functionality
import unittest
from PrimeExample import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-7))
        
    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        self.assertFalse(is_prime(4), msg='Four is not prime!')
    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        #self.assertFalse(is_prime(-7))
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))
#     def test_negative_number(self):
#         """Is a negative number correctly determined not to be prime?"""
#         for index in range(-1, -10, -1):
#             self.assertFalse(is_prime(index), msg='{} should not be determined to be prime'.format(index))
if __name__ == '__main__':
    unittest.main()