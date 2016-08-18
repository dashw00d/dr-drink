#!/usr/bin/python
import time

vodka = 2
oj = 4

screwdriver = {
    "vodka": 1.75,
    "oj": 3.50
}

long_island = {
    "vodka": 1.0,
    "gin": 1.0,
    "white rum": 1.0,
    "white twquila": 1.0,
    "tripple sec": 0.5,
    "lemon juice": 1,
    "cola": 4
}


def stopwatch(drink):
    vodka_seconds = input("How many seconds of vodka?: ")
    orange_juice_seconds = input("How many seconds of OJ?: ")
    start = time.time()
    time.clock()
    elapsed = 0

    while elapsed + 1 <= vodka_seconds:
        elapsed = time.time() - start
        print("--------------------")
        time.sleep(1)

    while elapsed + 1 < orange_juice_seconds + vodka_seconds:
        elapsed = time.time() - start
        print("~~~~~~~~~~~~~~~~~~~~")
        time.sleep(1)

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

stopwatch()


'''
Long Island Icea Tea

2 cups ice cubes

1 ounce vodka
1 ounce gin
1 ounce white rum
1 ounce white tequila
1/2 ounce Triple Sec
1 ounce lemon juice
4 ounces cola

'''
