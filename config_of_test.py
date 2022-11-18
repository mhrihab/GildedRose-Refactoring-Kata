from item import Item
from config import InnItems


def convert_items(test_values: dict) -> list:
    """
    Converts a dictionary into list of Item objects
    :param test_values: Item class
    :return: list of Item objects
    """
    items = []
    for i in range(len(test_values["quality"])):
        if len(test_values["name"]) == 1:
            items.append(Item(name=test_values["name"][0], sell_in=test_values["sell_in"][i],
                              quality=test_values["quality"][i]))
        else:
            items.append(Item(name=test_values["name"][i], sell_in=test_values["sell_in"][i],
                              quality=test_values["quality"][i]))

    return items


cheese_test_values = {
    "name": [InnItems.CHEESE.value],
    "sell_in": [0, -1, 10, 5],
    "quality": [20, 30, 50, 49]

}

sulfuras_test_values = {
    "name": [InnItems.SULFURAS.value],
    "sell_in": [0, -1, 5],
    "quality": [80, 80, 80]

}
conjured_test_values = {
    "name": [InnItems.CONJURED.value],
    "sell_in": [3, -1, 10, 5],
    "quality": [6, 30, 50, 49]

}
passes_test_values = {
    "name": [InnItems.PASSES.value],
    "sell_in": [0, -1, 10, 3, 5, 6, 15, 16, 10, 13],
    "quality": [5, 5, 50, 5, 5, 49, 5, 5, 5, 5]

}

regular_test_values = {
    "name": ["Elixir of the Mongoose", "+5 Dexterity Vest", "Potion", "Spell"],
    "sell_in": [3, -1, 10, 5],
    "quality": [6, 30, 50, 49]

}

expected_cheese_sellin = [-1, -2, 9, 4]
expected_cheese_quality = [22, 32, 50, 50]

expected_passes_quality = [0, 0, 50, 8, 8, 50, 6, 6, 7, 6]
expected_passes_sellin = [-1, -2, 9, 2, 4, 5, 14, 15, 9, 12]

expected_sulfras_quality = [80, 80, 80]
expected_sulfras_sellin = [0, -1, 5]

expected_conjured_quality = [4, 26, 48, 47]
expected_conjured_sellin = [2, -2, 9, 4]

expected_regular_quality = [5, 28, 49, 48]
expected_regular_sellin = [2, -2, 9, 4]

