#!/usr/bin/env python3
import os 
import sys 

def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner


@decorator_list
def add_together ( a, b):
    return a + b 


def main():
    #tuples
    dt_tuples = (0,1)
    print(dt_tuples[-1])
    print(add_together([(2,3),(4,6),(3,2)]))

if __name__ == "__main__":
    main()



