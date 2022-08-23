#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 100):
        if num % 15 is 0:
            print("FizzBuzz", end=" ")
        elif num % 3 is 0:
            print("Fizz", end=" ")
        elif num % 5 is 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
