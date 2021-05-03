#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program checks if a rectangle is a square based off
#   the length and width inputs from the user


def main():
    # this function checks if a rectangle with inputted dimensions is a square

    # input
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # process & output
    if length == width:
        print("\nThis rectangle is a square.")
    else:
        print("\nThis rectangle is not a square.")
    print("\nDone.")


if __name__ == "__main__":
    main()
