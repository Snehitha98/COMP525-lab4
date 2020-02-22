"""
test_update_inventory.py
Snehitha Mamidi
February 22, 2020
"""

import unittest
from problems.practice_dictionaries import Practice

class TestUpdateInventory(unittest.TestCase):
    """
    Tests for update_inventory() method
    """
    def setUp(self):
        """
        Define attribute p to hold object of type Problems
        """
        self.p = Practice()

    def test_quantities_added(self):
        """
        Test case with short season descriptions
        """
        inventory_dict = {'books': 10,'pencils': 15,'erasers': 20,'pens': 25}
        quantity_added = 5
        actual_result = self.p.update_inventory(inventory_dict,quantity_added)
        expected_result = {'books': 15,'pencils': 20,'erasers': 25,'pens': 30}
        self.assertDictEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
