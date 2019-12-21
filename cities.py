import random
import math


def read_cities(file_name):

    with open(file_name, "r") as parse_cities:
        all_cities = []
        for line in parse_cities.readlines():
            info = line.rstrip("\n").split("\t")
            state, city, latitude, longitude = info[0], info[1], float(info[2]), float(info[3])
            all_cities.append((state, city, latitude, longitude))
        return all_cities

    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, tht is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """


def print_cities(road_map):
    print(f"{'-' * 70}")
    print(f"{'LIST OF CITIES':^70}")
    print(f"{'-' * 70}")
    print(f"| ## | STATE {' ' * 14} CITY {' ' * 16} COORDS")
    print(f"{'-' * 70}")

    for index, city in enumerate(road_map, 1):
        print(f"| {index:02} | {city[0]:<20} {city[1]:<20} ({city[2]:.2f}, {city[3]:.2f})")
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """


def distance(x1, y1, x2, y2):
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)


def compute_total_distance(road_map):
    length = len(road_map)
    total_distance = 0

    for i in range(length):
        total_distance += distance(road_map[i][2], road_map[i][3],
                                   road_map[(i + 1) % length][2], road_map[(i + 1) % length][3])

    return float(total_distance)

    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """


def generate_two_different_ints(road_map):
    length = len(road_map) - 1
    random_index_1 = random.randint(0, length)
    random_index_2 = random.randint(0, length)

    different_ints = not (random_index_1 == random_index_2)

    while not different_ints:
        random_index_2 = random.randint(0, length)

        if random_index_1 != random_index_2:
            different_ints = True

    return random_index_1, random_index_2


def swap_cities(road_map, index1, index2):
    road_map[index1], road_map[index2] = road_map[index2], road_map[index1]

    return road_map, compute_total_distance(road_map)

    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    
    """


def shift_cities(road_map):
    return [road_map[-1]] + [road_map[city] for city in range(len(road_map) - 1)]

    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """


def find_best_cycle(road_map):
    test = 1
    best_distance = compute_total_distance(road_map)
    best_cycle = road_map[:]

    while test <= 10000:

        if test % 2 == 0:
            indices = generate_two_different_ints(road_map)
            perform_swap = swap_cities(road_map, indices[0], indices[1])
            cycle, cycle_distance = perform_swap[0], perform_swap[1]

        else:
            cycle = shift_cities(road_map)
            cycle_distance = compute_total_distance(cycle)

        if cycle_distance < best_distance:
            best_distance = cycle_distance
            best_cycle = cycle[:]

        test += 1

    return best_cycle

    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """


def print_map(road_map):
    length = len(road_map)
    print(f"{'-' * 85}")
    print(f"{'BEST CYCLE':^85}")
    print(f"{'-' * 85}")
    print(f"| ## | FROM {' ' * 34} TO {' ' * 27} COST")
    print(f"{'-' * 85}")

    for index, city in enumerate(range(length), 1):
        x1, y1 = road_map[city][2], road_map[city][3]
        x2, y2 = road_map[(city + 1) % length][2], road_map[(city + 1) % length][3]

        from_city_state = f"{road_map[city][1]}, {road_map[city][0]}"
        to_city_state = f"{road_map[(city + 1) % length][1]}, {road_map[(city + 1) % length][0]}"
        cost = distance(x1, y1, x2, y2)

        print(f"| {index:02} | {from_city_state:<30} ---->   {to_city_state:<30} {cost:.2f}")
        print(f"{'-' * 85}")

    print(f"{'TOTAL COST':>75}: {compute_total_distance(road_map):.2f}")

    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """


def visualise(road_map):

    all_latitudes, all_longitudes = [coords[2] for coords in road_map], [coords[3] for coords in road_map]

    min_lat, max_lat = int(min(all_latitudes)), int(max(all_latitudes))
    min_long, max_long = int(min(all_longitudes)), int(max(all_longitudes))

    coords = {(int(city[2]), int(city[3])): road_map.index(city) + 1 for city in road_map}

    plot_long = 0
    plot_lat = 0
    long_range = abs(max_long - min_long)

    print("\t ", end=" ")

    for latitude in range(max_lat + 3, min_lat - 1, -1):

        for longitude in range(min_long, max_long + 1):
            if plot_long <= long_range:
                print(f"{longitude:^4}", end=" ")
            elif plot_long == long_range + 1:
                vertical_bar = f"{'|':^5}"
                print(f"\n\t {vertical_bar * abs(long_range + 1)}")
            plot_long += 1

        if plot_lat > 2:

            print(latitude, end="\t ")
            for i in range(min_long, max_long + 1):
                print("-", end="")
                if (latitude, i) in coords.keys():
                    print(f"{coords[latitude, i]:^3}", end=" ")
                else:
                    print(f"{'':>3}", end=" ")
            print()
            if latitude > min_lat:
                vertical_bar = f"{'|':^5}"
                print(f"\t {vertical_bar * abs(long_range + 1)}")

        plot_lat += 1

        """
        Generates a grid of size max_long * max_lat, then maps all
        coordinates into a dictionary.
        Whenever the coordinates match a city, its position on the
        road map is printed out on the grid.
        """


def main():

    finished = False
    list_of_cities = input("Please type in the file to read: ")

    while not finished:
        try:
            if list_of_cities[-4:] == ".txt":
                road_map = read_cities(list_of_cities)
                finished = True
            else:
                print("Incorrect format, please try again.")
                list_of_cities = input("Try again: ")
        except IOError as error:
            print(error)
            list_of_cities = input("Try again: ")

    print_cities(road_map)
    best_cycle = find_best_cycle(road_map)
    print_map(best_cycle)
    print()
    visualise(best_cycle)


    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """


if __name__ == "__main__":  # keep this in
    main()