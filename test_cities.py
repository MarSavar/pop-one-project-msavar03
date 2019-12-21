import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert compute_total_distance(road_map1) == pytest.approx(9.386 + 18.496 + 10.646, 0.01)

    '''add your further tests'''


def test_compute_total_distance2():
    road_map1 = [("Maine", "Augusta", 44.323535, -69.765261),
                 ("Wisconsin", "Madison", 43.074722, -89.384444),
                 ("Florida", "Tallahassee", 30.4518, -84.27277),
                 ("New Jersey", "Trenton", 40.221741, -74.756138)]

    assert compute_total_distance(road_map1) == pytest.approx(19.658 + 13.618 + 13.638 + 6.46, 0.01)


def test_compute_total_distance3():
    road_map1 = [("Alabama", "Montgomery", 32.361538, -86.279118),
                 ("Iowa", "Des Moines",	41.590939, -93.620866)]

    assert compute_total_distance(road_map1) == pytest.approx(11.793 + 11.793, 0.01)


def test_compute_total_distance4():
    road_map1 = [("Michigan", "Lansing", 42.7335, -84.5467),
                 ("Wyoming", "Cheyenne", 41.145548, -104.802042),
                 ("Arkansas", "Little Rock", 34.736009, -92.331122),
                 ("Georgia", "Atlanta", 33.76, -84.39),
                 ("Pennsylvania", "Harrisburg", 40.269789, -76.875613)]

    assert compute_total_distance(road_map1) == pytest.approx(20.317 + 14.021 + 8 + 9.842 + 8.057, 0.01)


def test_compute_total_distance5():
    road_map1 = [("Utah", "Salt Lake City", 40.7547, -111.892622)]

    assert compute_total_distance(road_map1) == pytest.approx(0, 0.01)


def test_distance():
    assert distance(1, 2, 3, 4) == pytest.approx(2.828, 0.01)


def test_distance2():
    assert distance(-10, -20, 30, - 40) == pytest.approx(44.721, 0.01)


def test_distance3():
    assert distance(47.042418, -122.893077, 39.161921, -75.526755) == pytest.approx(48.017, 0.01)


def test_distance4():
    assert distance(30.266667, -97.75, 58.301935, -134.41974) == pytest.approx(46.158, 0.01)


def test_distance5():
    assert distance(44.931109, -123.029159, 45.464664, 9.18) == pytest.approx(132.21, 0.01)


def test_swap_cities1():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert swap_cities(road_map1, 0, 2) == ([("Minnesota", "Saint Paul", 44.95, -93.094),
                                             ("Delaware", "Dover", 39.161921, -75.526755),
                                             ("Kentucky", "Frankfort", 38.197274, -84.86311)],
                                            pytest.approx(18.496 + 9.386 + 10.646, 0.01))


def test_swap_cities2():
    road_map1 = [("Alabama", "Montgomery", 32.361538, -86.279118),
                 ("Iowa", "Des Moines",	41.590939, -93.620866)]

    assert swap_cities(road_map1, 0, 1) == ([("Iowa", "Des Moines",	41.590939, -93.620866),
                                             ("Alabama", "Montgomery", 32.361538, -86.279118)],
                                            pytest.approx(11.79 + 11.79, 0.01))


def test_swap_cities3():
    road_map1 = [("Michigan", "Lansing", 42.7335, -84.5467),
                 ("Wyoming", "Cheyenne", 41.145548, -104.802042),
                 ("Arkansas", "Little Rock", 34.736009, -92.331122),
                 ("Georgia", "Atlanta", 33.76, -84.39),
                 ("Pennsylvania", "Harrisburg", 40.269789, -76.875613)]

    assert swap_cities(road_map1, 3, 1) == ([("Michigan", "Lansing", 42.7335, -84.5467),
                                             ("Georgia", "Atlanta", 33.76, -84.39),
                                             ("Arkansas", "Little Rock", 34.736009, -92.331122),
                                             ("Wyoming", "Cheyenne", 41.145548, -104.802042),
                                             ("Pennsylvania", "Harrisburg", 40.269789, -76.875613)],
                                            pytest.approx(8.974 + 8 + 14.021 + 27.94 + 8.057, 0.01))


def test_swap_cities4():
    road_map1 = [("Maine", "Augusta", 44.323535, -69.765261),
                 ("Wisconsin", "Madison", 43.074722, -89.384444),
                 ("Florida", "Tallahassee", 30.4518, -84.27277),
                 ("New Jersey", "Trenton", 40.221741, -74.756138)]

    assert swap_cities(road_map1, 0, 3) == ([("New Jersey", "Trenton", 40.221741, -74.756138),
                                             ("Wisconsin", "Madison", 43.074722, -89.384444),
                                             ("Florida", "Tallahassee", 30.4518, -84.27277),
                                             ("Maine", "Augusta", 44.323535, -69.765261)],
                                            pytest.approx(14.903 + 13.618 + 20.072 + 6.46, 0.01))


def test_swap_cities5():
    road_map1 = [("Florida", "Tallahassee", 30.4518, -84.27277),
                 ("Oklahoma", "Oklahoma City", 35.482309, -97.534994),
                 ("Idaho", "Boise", 43.613739, -116.237651),
                 ("New Jersey", "Trenton", 40.221741, -74.756138),
                 ("Maryland", "Annapolis", 38.972945, -76.501157)]

    assert swap_cities(road_map1, 3, 4) == ([("Florida", "Tallahassee", 30.4518, -84.27277),
                                             ("Oklahoma", "Oklahoma City", 35.482309, -97.534994),
                                             ("Idaho", "Boise", 43.613739, -116.237651),
                                             ("Maryland", "Annapolis", 38.972945, -76.501157),
                                             ("New Jersey", "Trenton", 40.221741, -74.756138)],
                                            pytest.approx(14.184 + 20.393 + 40.006 + 2.145 + 13.638, 0.01))


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
    road_map1 = [("Florida", "Tallahassee", 30.4518, -84.27277),
                 ("Oklahoma", "Oklahoma City", 35.482309, -97.534994),
                 ("Idaho", "Boise", 43.613739, -116.237651),
                 ("Maryland", "Annapolis", 38.972945, -76.501157),
                 ("New Jersey", "Trenton", 40.221741, -74.756138)]

    assert shift_cities(road_map1) == [("New Jersey", "Trenton", 40.221741, -74.756138),
                                       ("Florida", "Tallahassee", 30.4518, -84.27277),
                                       ("Oklahoma", "Oklahoma City", 35.482309, -97.534994),
                                       ("Idaho", "Boise", 43.613739, -116.237651),
                                       ("Maryland", "Annapolis", 38.972945, -76.501157)]


def test_shift_cities3():
    road_map1 = [("Maine", "Augusta", 44.323535, -69.765261),
                 ("Wisconsin", "Madison", 43.074722, -89.384444),
                 ("Florida", "Tallahassee", 30.4518, -84.27277),
                 ("New Jersey", "Trenton", 40.221741, -74.756138)]

    assert shift_cities(road_map1) == [("New Jersey", "Trenton", 40.221741, -74.756138),
                                       ("Maine", "Augusta", 44.323535, -69.765261),
                                       ("Wisconsin", "Madison", 43.074722, -89.384444),
                                       ("Florida", "Tallahassee", 30.4518, -84.27277)]


def test_shift_cities4():
    road_map1 = [("Michigan", "Lansing", 42.7335, -84.5467),
                 ("Wyoming", "Cheyenne", 41.145548, -104.802042),
                 ("Arkansas", "Little Rock", 34.736009, -92.331122),
                 ("Georgia", "Atlanta", 33.76, -84.39),
                 ("Pennsylvania", "Harrisburg", 40.269789, -76.875613)]

    assert shift_cities(road_map1) == [("Pennsylvania", "Harrisburg", 40.269789, -76.875613),
                                       ("Michigan", "Lansing", 42.7335, -84.5467),
                                       ("Wyoming", "Cheyenne", 41.145548, -104.802042),
                                       ("Arkansas", "Little Rock", 34.736009, -92.331122),
                                       ("Georgia", "Atlanta", 33.76, -84.39)]


def test_shift_cities5():
    road_map1 = [("Alabama", "Montgomery", 32.361538, -86.279118),
                 ("Iowa", "Des Moines", 41.590939, -93.620866)]

    assert shift_cities(road_map1) == [("Iowa", "Des Moines", 41.590939, -93.620866),
                                       ("Alabama", "Montgomery", 32.361538, -86.279118)]
