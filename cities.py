import random
import math


def read_cities(file_name):
    """
    Reads in the cities from the given `file_name`, and returns
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

    This is the initial `road_map`, that is, the cycle

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    with open(file_name, "r") as parse_cities:
        all_cities = []
        for line in parse_cities.readlines():
            info = line.rstrip("\n").split("\t")
            state, city, latitude, longitude = info[0], info[1], float(info[2]), float(info[3])
            all_cities.append((state, city, latitude, longitude))
        return all_cities


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations.
    Prints only one or two digits after the decimal point.
    """
    print(f"{'-' * 70}")
    print(f"{'LIST OF CITIES':^70}")
    print(f"{'-' * 70}")
    print(f"| ## | STATE {' ' * 14} CITY {' ' * 16} COORDS")
    print(f"{'-' * 70}")

    for index, city in enumerate(road_map, 1):
        print(f"| {index:02} | {city[0]:<20} {city[1]:<20} ({city[2]:.2f}, {city[3]:.2f})")


def distance(x1, y1, x2, y2):
    """
    Calculates the Euclidean distance between two points.
    """
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. It's a cycle, so
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    length = len(road_map)
    total_distance = 0

    for i in range(length):
        total_distance += distance(road_map[i][3], road_map[i][2],
                                   road_map[(i + 1) % length][3], road_map[(i + 1) % length][2])

    return float(total_distance)


def generate_two_different_ints(road_map):
    """
    Generates two integer numbers that are always different,
    so that the same two numbers can never be passed to swap_cities()
    """
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
    """
    Takes the city at location `index` in the `road_map`, and the
    city at location `index2`, swaps their positions in the `road_map`,
    computes the new total distance, and returns the tuple
        (new_road_map, new_total_distance)
    """
    new_road_map = road_map[:]
    new_road_map[index1], new_road_map[index2] = new_road_map[index2], new_road_map[index1]

    return new_road_map, compute_total_distance(new_road_map)


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Returns the new road map.
    """
    new_road_map = road_map[:]
    return [new_road_map[-1]] + [new_road_map[city] for city in range(len(new_road_map) - 1)]


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`,
    tries `10000` swaps/shifts, and each time keeps the best cycle found so far.
    After `10000` swaps/shifts, returns the best cycle found so far.
    Uses randomly generated indices for swapping.
    """
    test = 1
    best_distance = compute_total_distance(road_map)
    best_cycle = road_map[:]

    while test <= 10000:

        if test % 2 == 0:
            indices = generate_two_different_ints(best_cycle)
            perform_swap = swap_cities(best_cycle, indices[0], indices[1])
            cycle, cycle_distance = perform_swap[0], perform_swap[1]

        else:
            cycle = shift_cities(best_cycle)
            cycle_distance = compute_total_distance(cycle)

        if cycle_distance < best_distance:
            best_distance = cycle_distance
            best_cycle = cycle[:]

        test += 1

    return best_cycle


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    length = len(road_map)
    print(f"{'-' * 85}")
    print(f"{'BEST CYCLE':^85}")
    print(f"{'-' * 85}")
    print(f"| ## | FROM {' ' * 33} TO {' ' * 27} COST")
    print(f"{'-' * 85}")

    for index, city in enumerate(range(length), 1):
        x1, y1 = road_map[city][3], road_map[city][2]
        x2, y2 = road_map[(city + 1) % length][3], road_map[(city + 1) % length][2]

        from_city_state = f"{road_map[city][1]}, {road_map[city][0]}"
        to_city_state = f"{road_map[(city + 1) % length][1]}, {road_map[(city + 1) % length][0]}"
        cost = distance(x1, y1, x2, y2)

        print(f"| {index:02} | {from_city_state:<30} ---->   {to_city_state:<30} {cost:.2f}")
        print(f"{'-' * 85}")

    print(f"{'>>> TOTAL COST':>75}: {compute_total_distance(road_map):.2f}")


def visualise(road_map):
    """
    Generates a grid of size max_long * max_lat, then maps all
    coordinates into a dictionary.
    Whenever the coordinates match a city, its position on the
    road map is printed out on the grid.
    """

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
                    print(f"{coords[latitude, i]:^4}", end="")
                else:
                    print(f"{'':^4}", end="")
            print()

            if latitude > min_lat:
                vertical_bar = f"{'|':^5}"
                print(f"\t {vertical_bar * abs(long_range + 1)}")

        plot_lat += 1


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    finished = False
    list_of_cities = input("Please type in the file to read: ")

    while not finished:
        if list_of_cities[-4:] == ".txt":
            try:
                road_map = read_cities(list_of_cities)
                finished = True
            except IOError as error:
                print(error)
                list_of_cities = input("Try again: ")
        else:
            print("Incorrect format, please try again.")
            list_of_cities = input("Try again: ")

    print_cities(road_map)
    best_cycle = find_best_cycle(road_map)
    print_map(best_cycle)
    print()
    visualise(best_cycle)


if __name__ == "__main__":  # keep this in
    main()