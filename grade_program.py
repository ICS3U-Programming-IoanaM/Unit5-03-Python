#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Dec. 4, 2022
# a program that calculates a mark as a percentage with a given level


# calculates the mark based on the level entered
def calc_mark(level):
    # level entered is 4+
    if level == "4+":
        return "The mark is between 95% - 100%."

    # level entered is 4
    elif level == "4":
        return "The mark is between 87% - 94%."

    # level entered is 4-
    elif level == "4-":
        return "The mark is between 80% - 86%."

    # level entered is 3+
    elif level == "3+":
        return "The mark is between 77% - 79%."

    # level entered is 3
    elif level == "3":
        return "The mark is between 73% - 76%."

    # level entered is 3-
    elif level == "3-":
        return "The mark is between 70% - 72%."

    # level entered is 2+
    elif level == "2+":
        return "The mark is between 67% - 69%."

    # level entered is 2
    elif level == "2":
        return "The mark is between 63% - 66%."

    # level entered is 2-
    elif level == "2-":
        return "The mark is between 60% - 62%."

    # level entered is 1+
    elif level == "1+":
        return "The mark is between 57% - 59%."

    # level entered is 1
    elif level == "1":
        return "The mark is between 53% - 56%."

    # level entered is 1-
    elif level == "1-":
        return "The mark is between 50% - 52%."

    # level entered is R
    elif level == "R":
        return "The mark is less than 50%."

    # level entered is invalid
    else:
        return "Invalid input! Please enter a valid level."


def main():
    # getting user input for the level
    user_level = input("Please enter the level (ex. 3+): ")

    # calls function to calculate the mark
    display_mark = calc_mark(user_level)

    # prints results
    print(display_mark)


if __name__ == "__main__":
    main()
