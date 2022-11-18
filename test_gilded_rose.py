from config_of_test import *
from gilded_rose import GildedRose
import unittest
import logging




class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)



    def test_update_aged_brie(self):
        real_tests=convert_items(cheese_test_values)
        gilded_rose = GildedRose(real_tests)
        gilded_rose.update_quality()
        for quality_values in range(len(expected_cheese_quality)):
            try:
                self.assertEqual(real_tests[quality_values].quality,expected_cheese_quality[quality_values])
            except Exception:
                logging.error("error in the " + str(quality_values) + " iteration of quality tests for aged brie")


        for sell_in_values in range(len(expected_cheese_sellin)):
            try:
                self.assertEqual(real_tests[sell_in_values].sell_in,expected_cheese_sellin[sell_in_values])
            except Exception:
                logging.error("error in the " + str(sell_in_values) + " iteration of sellIn tests for aged brie")


    def test_update_sulfuras(self):
        real_tests=convert_items(sulfuras_test_values)
        gilded_rose = GildedRose(real_tests)
        gilded_rose.update_quality()
        for quality_values in range(len(expected_sulfras_quality)):
            try:
                self.assertEqual(real_tests[quality_values].quality,expected_sulfras_quality[quality_values])
            except Exception:
                logging.error("error in the " + str(quality_values) + " iteration of quality tests of sulfuras")


        for sell_in_values in range(len(expected_sulfras_sellin)):
            try:
                self.assertEqual(real_tests[sell_in_values].sell_in,expected_sulfras_sellin[sell_in_values])
            except Exception:
                logging.error("error in the " + str(sell_in_values) + " iteration of sellIn tests of sulfuras")


    def test_update_passes(self):
        real_tests=convert_items(passes_test_values)
        gilded_rose = GildedRose(real_tests)
        gilded_rose.update_quality()
        for quality_values in range(len(expected_passes_quality)):
            try:
                self.assertEqual(real_tests[quality_values].quality,expected_passes_quality[quality_values])
            except Exception:
                logging.error("error in the " + str(quality_values) + " iteration of quality tests of passes")


        for sell_in_values in range(len(expected_passes_sellin)):
            try:
                self.assertEqual(real_tests[sell_in_values].sell_in,expected_passes_sellin[sell_in_values])
            except Exception:
                logging.error("error in the " + str(sell_in_values) + " iteration of sellIn tests of passes")

    def test_update_conjured(self):
        real_tests=convert_items(conjured_test_values)
        gilded_rose = GildedRose(real_tests)
        gilded_rose.update_quality()
        for quality_values in range(len(expected_conjured_quality)):
            try:
                self.assertEqual(real_tests[quality_values].quality,expected_conjured_quality[quality_values])
            except Exception:
                logging.error("error in the " + str(quality_values) + " iteration of quality tests of conjured")


        for sell_in_values in range(len(expected_conjured_sellin)):
            try:
                self.assertEqual(real_tests[sell_in_values].sell_in,expected_conjured_sellin[sell_in_values])
            except Exception:
                logging.error("error in the " + str(sell_in_values) + " iteration of sellIn tests of conjured")

    def test_update_regular_items(self):

        real_tests=convert_items(regular_test_values)
        gilded_rose = GildedRose(real_tests)
        gilded_rose.update_quality()
        for quality_values in range(len(expected_regular_quality)):
            try:
                self.assertEqual(real_tests[quality_values].quality,expected_regular_quality[quality_values])
            except Exception:
                logging.error("error in the " + str(quality_values) + " iteration of quality tests of regular items")


        for sell_in_values in range(len(expected_regular_sellin)):
            try:
                self.assertEqual(real_tests[sell_in_values].sell_in,expected_regular_sellin[sell_in_values])
            except Exception:
                logging.error("error in the " + str(sell_in_values) + " iteration of sellIn tests of regular items")



if __name__ == '__main__':
    unittest.main()
