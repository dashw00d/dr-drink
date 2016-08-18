#!/usr/bin/python
import time
import json


with open('recipes.json') as data_file:
    json_data = json.load(data_file)
print(json_data["long_island"]["vodka"])


class PoorDrink:

    def __init__(self, drink):
        self.drink = drink
        self.total_oz = 0
        self.elapsed = 0

    def timer(self):
        start = time.time()
        time.clock()  # starts measuring process time
        for key in self.drink:
            self.total_oz += self.drink[key]

            while self.elapsed <= self.total_oz:
                self.elapsed = time.time() - start
                print(json_data["drink_parts"][key] * 5)
                time.sleep(.5)

        print("Total Ounces:", self.total_oz)
'''
    def score(self):

        denominator = vodka + oj
        drink1 = 100 * float(vodka_seconds) / float(denominator)
        drink2 = 100 * float(orange_juice_seconds) / float(denominator)
        vodkad = 100 * float(vodka) / float(denominator)
        ojd = 100 * float(oj) / float(denominator)
        comb = abs(drink1 - vodkad) + abs(drink2 - ojd)
        score = 100 - comb

        print("Denominator", denominator)
        print("vodka", drink1)
        print("oj", drink2)
        print("taget vodka", vodkad)
        print("target oj", ojd)
        print("Percent Wrong Vodka: ", abs(drink1 - vodkad))
        print("Percent Wrong OJ: ", abs(drink2 - ojd))
        print("Score: ", score)
'''

if __name__ == "__main__":
    test = PoorDrink(json_data["long_island"])
    test.timer()
