#!/usr/bin/python3

import re

class ColourCount:
    def __init__(self, red=0, blue=0, green=0):
        self.red=red
        self.blue=blue
        self.green=green

def get_colour_count(item: str) -> ColourCount:
    games = item.split(";")

    max_red = 0
    max_blue = 0
    max_green = 0

    for game in games:
        result = re.findall(r"(\d+) (blue|red|green)", game)

        red = 0
        blue = 0
        green = 0

        for item in result:
            if item[1] == "green":
                green += int(item[0])
            elif item[1] == "blue":
                blue += int(item[0])
            elif item[1] == "red":
               red+= int(item[0])

        if red > max_red:
            max_red = red

        if blue > max_blue:
            max_blue = blue

        if green > max_green:
            max_green = green

    return ColourCount(max_red,max_blue,max_green)


def analyse(item: str) -> int:
    GameIndex = 0
    if item[6] == ":":
        GameIndex = int(item[5])
    elif item[7] == ":":
        GameIndex = int(str(item[5] + item[6]))
    elif item[8] == ":":
        GameIndex = int(str(item[5] + item[6] + item[7]))
    elif item[9] == ":":
        GameIndex = int(str(item[5] + item[6] + item[7] + item[8]))

    if GameIndex == 0:
        print(item)
        print("ERROR GAME INDEX IS 0")
        exit(0)

    colours:ColourCount = get_colour_count(item)
    
    possible = True
    if colours.red > 12:
        possible = False
    if colours.blue > 14:
        possible = False
    if colours.green > 13:
        possible = False

    if possible:
        return GameIndex
    else:
        return 0

def main(data: str):
    data_list:list[str] = data.split("\n")[:-1]
    results:list[int] = []
    for item in data_list:
        results.append(analyse(item))
    return sum(results)

if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read()
        print(main(data))
