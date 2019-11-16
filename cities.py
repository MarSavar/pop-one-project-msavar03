import random
import math
import copy

def read_cities(file_name):

    parse_cities = open(file_name, "r")
    all_cities = []

    for element in parse_cities.readlines():
        sub = element.rstrip("\n").split("\t")
        state,city,latitude,longitude = sub[0],sub[1],float(sub[2]),float(sub[3])
        all_cities.append((state,city,latitude,longitude))

    parse_cities.close()

    return all_cities
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, tht is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
  
def print_cities(road_map):
    for city in road_map:
        print(f"{city[1]}, {city[0]} ({city[2]:.2f}, {city[3]:.2f})")
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
def distance(x1,y1,x2,y2):

    return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

def compute_total_distance(road_map):

    length = len(road_map)
    total_distance = 0

    for i in range(len(road_map)):
        total_distance += distance(road_map[i][2],road_map[i][3],
                                   road_map[(i+1) % length][2],road_map[(i+1) % length][3])

    return total_distance

    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """


def swap_cities(road_map, index1, index2):

    if index1 == index2:
        pass
    else:
        road_map[index1],road_map[index2] = road_map[index2],road_map[index1]
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

    new_road_map = [road_map[-1]]

    for city in range(len(road_map)-1):
        new_road_map.append(road_map[city])

    return new_road_map
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """

def find_best_cycle(road_map):

    test = 1
    best_distance = compute_total_distance(road_map)
    best_cycle = copy.deepcopy(road_map)

    while test <= 10000:

        swap_or_shift = random.randint(1, 2)

        if swap_or_shift == 1:
            random_index_1 = random.randint(0, len(road_map)-1)
            random_index_2 = random.randint(0, len(road_map)-1)
            swap_cities(road_map,random_index_1,random_index_2)

        else:
            shift_cities(road_map)

        cycle_distance = compute_total_distance(road_map)

        if cycle_distance < best_distance:
            best_distance = cycle_distance
            best_cycle = copy.deepcopy(road_map)

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
    total_distance = 0

    for i in range(len(road_map)):
        total_distance += distance(road_map[i][2], road_map[i][3], road_map[(i + 1)%length][2], road_map[(i + 1)%length][3])
        print(f"{road_map[i][1]}, {road_map[i][0]} -> {road_map[(i + 1)%length][1]}, {road_map[(i + 1)%length][0]}:"
              f" {distance(road_map[i][2], road_map[i][3], road_map[(i + 1)%length][2], road_map[(i + 1)%length][3]):.2f}")

    print("Total cost ",round(compute_total_distance(road_map),2))

    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """

def main():

    print_cities(read_cities("city-data.txt"))
    print("-"*40)
    print_map(find_best_cycle(read_cities("city-data.txt")))

    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """

if __name__ == "__main__": #keep this in
    main()
