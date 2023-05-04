def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    list = input()
    list = list.split(", ")  # split string
    for i in list:
        list[list.index(i)] = float(i)  # replace each string with float?
    return list  # list of floats


def calc_average(list):
    # print("calc_average")
    total = 0.0
    for i in list:
        total += i
    return total / len(list)  # float


def sort_temperature(list):
    return sorted(list)  # list of floats in ascending order. .sort displays "None"


def find_min_max(list):
    list = sort_temperature(list)
    calc = []
    calc.insert(0, list[0])
    calc.insert(1, list[-1])
    return calc  # list of floats [min_temp, max_temp]


def calc_median_temperature(list):
    # list = list.median()
    list = sort_temperature(list)
    if len(list) % 2 == 1:
        print("Odd list")
        list = list[int(len(list)/2 - 0.5)]  # 0, 1, [2], 3, 4
    else:
        print("Even list")
        list = (list[int(len(list)/2)] + list[int(len(list)/2 - 1)])/2  # 0, 1, [2, 3], 4, 5
    return list  # Float


def calc_average_temperature(list):  # Identical to average
    total = 0.0
    for i in list:
        total += i
    return total/len(list)  # Float


def calc_min_max_temperature(list):  # Identical to min/max
    list = sort_temperature(list)
    calc = []
    calc.insert(0, min(list))
    calc.insert(1, max(list))
    return calc  # Float


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    while True:
        display_main_menu()
        num_list = get_user_input()
        print("\nAverage =", calc_average(num_list))
        print("Min =", find_min_max(num_list)[0], "\nMax =", find_min_max(num_list)[1])

        temp_list = sort_temperature(num_list)
        print("Sorted list:", temp_list)
        print("Median:", calc_median_temperature(temp_list))
        print("\n")
    # Test numbers: 2, 3, 1, 15, 3.5, 0.2, -5, 10


if __name__ == "__main__":
    main()
