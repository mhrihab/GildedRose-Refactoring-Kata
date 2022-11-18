# -*- coding: utf-8 -*-
from app.config import InnItems

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        
    def update_aged_brie(self, item):
        if item.quality < InnItems.MAX_QUALITY.value:
            item.quality += 1
        if item.sell_in < 1 and item.quality < InnItems.MAX_QUALITY.value:
            item.quality += 1
        item.sell_in -= 1
    def update_sulfuras(self, item):
        pass
    def update_passes(self, item):
        if item.quality < InnItems.MAX_QUALITY.value:
            item.quality += 1
        if item.sell_in < 11 and item.quality < InnItems.MAX_QUALITY.value:
            item.quality += 1
        if item.sell_in < 6 and item.quality < InnItems.MAX_QUALITY.value:
            item.quality += 1
        if item.sell_in < 1:
            item.quality = 0
        item.sell_in -= 1
        
        
    def update_conjured(self, item):
        if item.quality > InnItems.MIN_QUALITY.value:
            item.quality = item.quality - 2

            if item.sell_in <= 0:
                item.quality = item.quality - 2

        if item.quality<InnItems.MIN_QUALITY.value:
            item.quality=InnItems.MIN_QUALITY.value

        item.sell_in = item.sell_in - 1
        
        
    def update_regular_items(self, item):
        if item.quality > InnItems.MIN_QUALITY.value:
            item.quality -= 1
        if item.sell_in < 1 and item.quality > InnItems.MIN_QUALITY.value:
            item.quality -= 1
        item.sell_in -= 1

    def update_quality(self):
        for item in self.items:
            if item.name == InnItems.SULFURAS.value:
                self.update_sulfuras(item)
            elif item.name == InnItems.CHEESE.value:
                self.update_aged_brie(item)
            elif item.name == InnItems.PASSES.value:
                self.update_passes(item)
            elif item.name==InnItems.CONJURED.value:
                self.update_conjured(item)
            else:
                self.update_regular_items(item)
