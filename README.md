### parse_seasons()
```
def parse_seasons(self, season_dict):
    """
    Create a string with info from season_dict
    season_dict: dictionary
        keys: strings - season names
        values: strings - season descriptions
    Returns: string with season names and descriptions and no spaces or
        other characters in between
    """
```
* Assign an empty string to variable named **string**
* use a for loop with loop variable called **season_names** to iterate over **input1**
      * concatenating string, season_names and value of season_names in the dictionary input1 and storing it in **string**
* removing all space characters in the string and assigning it to **result**
* Returns **result**

### update_inventory()
```
def update_inventory(self, inventory_dict, quantity_added):
    """
    Returns new dictionary with quantities for each item in inventory_dict
        increased by quantity-added
    inventory_dict: dictionary
        keys: strings - inventory item names
        values: int - inventory quantity of item
    Returns: dictionary
    """
```
* use a for loop with loop variable called **quantities** to iterate over **inventory_dict**
     * adding a quantity_added, to value of quantities in the dictionary inventory_dict
* assigning **inventory_dict** to **new_dictionary**
* Returns **new_dictionary**
