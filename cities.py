import random
import math

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
        print(city[1]+",",
              city[0]+":",
              round(city[2],2),
              round(city[3],2))
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
def distance(x1,y1,x2,y2):

    return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

def compute_total_distance(road_map):

    last = len(road_map)-1
    total_distance = 0


    for city in range(len(road_map)):
        if city != last:
            total_distance += distance(road_map[city][2],road_map[city][3],road_map[city+1][2],road_map[city+1][3])
        else:
            total_distance += distance(road_map[city][2],road_map[city][3],road_map[0][2],road_map[0][3])

    return total_distance


    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """

def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__": #keep this in
    main()

    print(compute_total_distance(read_cities("city-data.txt")))