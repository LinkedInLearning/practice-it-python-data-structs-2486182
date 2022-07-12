from collections import Counter 

def main():
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    sales_this_week = Counter(STA001=5, SAL002=3,ENT004=3)
    inventory = inventory - sales_this_week
    print(inventory)
    inventory_in = {"STA001":9, "SAL002": 1}
    inventory.update(inventory_in)
    print(inventory) 

if __name__ == "__main__":
    main()