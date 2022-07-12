from collections import namedtuple

def can_take_order(driver, num_packages):
    return driver.car_capacity >= num_packages

def main():
    Driver = namedtuple("driver", ["name", "car_type", "car_capacity"])
    driver_one = Driver("Iris", "Toyota Prius", 7)
    driver_two = Driver("Mickie", "Hyundai Tucson", 15)
    driver_three = Driver("Witty", "Hummer", 26)
    print(driver_one)
    print(can_take_order(driver_three, 20))
    return

if __name__ == "__main__":
    main()