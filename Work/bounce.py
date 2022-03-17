# bounce.py
#
# Exercise 1.5

height = 100  # meters


def print_bounces(height, num):
    while num < 11:
        height = height * 0.6
        print(round(height, 4))
        num = num + 1


print_bounces(100, 1)
