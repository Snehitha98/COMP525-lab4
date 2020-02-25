"""
practice_dictionaries.py
Snehitha Mamidi
February 22, 2020
"""


class Practice(object):
    """
    Illustrate methods that transform an input dictionary into some output
    """

    def parse_seasons(self, input1):
        """
        Create a string with info from season_dict
        season_dict: dictionary
            keys: strings - season names
            values: strings - season descriptions
        Returns: string with season names and descriptions and no spaces or
            other characters in between
        """
        string = ""
        for season_names in input1:
            string = string + season_names + input1[season_names]
        result = string.replace(" ","")
        return result

    def update_inventory(self, inventory_dict, quantity_added):
        """
        Returns new dictionary with quanties for each itmem in inventory_dict
            increased by quantity-added
        inventory_dict: dictionary
            keys: strings - inventory item names
            values: int - inventory quantity of item
        Returns: dictionary
        """
        for quantities in inventory_dict:
            inventory_dict[quantities] += quantity_added
        new_dictionary = inventory_dict
        return new_dictionary

if __name__ == '__main__':
    p = Practice()
    input1 = {
        'spring': 'warm',
        'summer': 'hot',
        'fall': 'just right',
        'winter': 'cold'
    }
    result = p.parse_seasons(input1)
    print(f'parse_seasons({input1}) returns {result}')
# Testing for one season
    p = Practice()
    input1 = {
        'Rainy': 'Full of water'
    }
    result = p.parse_seasons(input1)
    print(f'parse_seasons({input1}) returns {result}')


# Testing update_inventory()
    p = Practice()
    inventory_dict = {'books': 10,'pencils': 15,'erasers': 20,'pens': 25}
    quantity_added = 5
    result = p.update_inventory(inventory_dict,quantity_added)
    inventory_dict = {'books': 10,'pencils': 15,'erasers': 20,'pens': 25}
    print(f'update_inventory({inventory_dict},{quantity_added}) returns {result}')

# Testcase for update_inventory()
    p = Practice()
    inventory_dict = {'milkybar': 3,'kitkat': 17}
    quantity_added = 7
    result = p.update_inventory(inventory_dict,quantity_added)
    inventory_dict = {'milkybar': 3,'kitkat': 17}
    print(f'update_inventory({inventory_dict},{quantity_added}) returns {result}')
