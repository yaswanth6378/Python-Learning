import sys


def main():
    coordinates_tuple = (46.37, 7.59)
    coordinate_list = [46.37, 7.59]
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")


main()
