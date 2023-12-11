#!/usr/bin/python3

def analyse(item: str) -> int:
    return 0

def main(data: str):
    data_list:list[str] = data.split("\n")
    results:list[int] = []
    for item in data_list:
        results.append(analyse(item))
    return sum(results)

if __name__ == "__main__":
    with open("sample.txt") as f:
        data = f.read()
        print(main(data))
