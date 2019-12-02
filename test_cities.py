import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert compute_total_distance(road_map1) == \
           pytest.approx(9.386 + 18.496 + 10.646, 0.01)

    '''add your further tests'''


def test_compute_total_distance2():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]


def test_distance():
    assert distance(1, 2, 3, 4) == pytest.approx(2.828, 0.01)


def test_distance2():
    assert distance(-10, -20, 30, - 40) == pytest.approx(44.721, 0.01)


def test_swap_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert swap_cities(road_map1, 0, 2) == ([("Minnesota", "Saint Paul", 44.95, -93.094),
                                             ("Delaware", "Dover", 39.161921, -75.526755),
                                             ("Kentucky", "Frankfort", 38.197274, -84.86311)],
                                            pytest.approx(18.496 + 9.386 + 10.646, 0.01))


def test_shift_cities():
    road_map1 = [("City 1", "State 1", 1, 2),
                 ("City 2", "State 2", -2, 3),
                 ("City 3", "State 3", 25, 52),
                 ("City 4", "State 4", 33, -1)]

    assert shift_cities(road_map1) == [("City 4", "State 4", 33, -1),
                                       ("City 1", "State 1", 1, 2),
                                       ("City 2", "State 2", -2, 3),
                                       ("City 3", "State 3", 25, 52)]


def test_shift_cities2():

    road_map1 = [("City 1", "State 1", 8, 9),
                 ("City 2", "State 2", 12, -52)]

    assert shift_cities(road_map1) == [("City 2", "State 2", 12, -52),
                                       ("City 1", "State 1", 8, 9)]
