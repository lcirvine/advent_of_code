import os

module_list = [int(line.rstrip('\n')) for line in open(os.path.join(os.getcwd(), 'day1_input.txt'))]


def fuel_req(mass):
    fuel = (mass // 3) - 2
    return fuel


total_fuel = 0
for module in module_list:
    module_fuel = fuel_req(module)
    # part 2
    # total_fuel += module_fuel
    while module_fuel >= 0:
        total_fuel += module_fuel
        module_fuel = fuel_req(module_fuel)

print(total_fuel)
