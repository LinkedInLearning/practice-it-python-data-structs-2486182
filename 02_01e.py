from collections import deque
def main():
    foods = deque(maxlen=5)
    foods.append("STA001") # we can append one at a time
    ordered_foods = ["DES003", "STA002", "ENT004", "ENT001"]
    foods.extend(ordered_foods) # we can extend multiple
    print(foods)
    foods.append("DES002")
    print(foods)
    foods.appendleft("DES005")
    print(foods)
    return

if __name__ == "__main__":
    main()