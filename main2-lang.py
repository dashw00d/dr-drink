#!/usr/bin/python
import time
import json
from pprint import pprint


with open('recipes.json') as data_file:
    json_data = json.load(data_file)
print(json_data["long_island"]["vodka"])


class PoorDrink:

    def __init__(self, drink):
        self.drink = drink
        self.total_oz = 0
        self.target_oz = 0
        self.elapsed = 0
        self.user_poor = {}

    def timer(self):
        start = time.time()
        time.clock()  # starts measuring process time
        for key in self.user_poor:
            self.total_oz += self.user_poor[key]
            self.target_oz += self.drink[key]

            while self.elapsed <= self.total_oz:
                self.elapsed = time.time() - start
                print(json_data["drink_parts"][key])
                time.sleep(.5)
        # return self.total_oz

        print("Total Ounces:", self.total_oz)
        print("Target Ounces:", self.target_oz)
        self.score()

    def menu(self):

        for key in self.drink:
            amount = float(input("How much {}?: ".format(key)))
            self.user_poor[key] = amount
        pprint(self.user_poor)
        self.timer()

    def score(self):
        comb = 0
        for key in self.drink:
            user = 100 * float(self.user_poor[key]) / float(self.target_oz)
            source = 100 * float(self.drink[key]) / float(self.target_oz)
            comb += abs(user - source)

        print("Score:", 100 - comb)

if __name__ == "__main__":
    test = PoorDrink(json_data["long_island"])
    test.menu()
