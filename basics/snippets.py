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

class Spotify_user :
    def __init__(self, name, email,premium):
        self.name = name
        self.email = email
        self.premium = premium

    def isPremium(self):
        if self.premium:
            print("{} is a premium user".format(self.name))
        else:
            print("{} is not a premium user".format(self.name))    

def get_list_info( list_info : list ):
    for info in list_info:
        print(info)
    for info in enumerate(list_info):
        print(type(info))
    for index , value in enumerate(list_info,start=1):
        print("{} is {}".format(index, value))
    return

def get_list_reversed( list_data : list):
    for items in reversed(list_data):
        print(items)
    return

def get_list_sorted( list_data : list):
    for items in sorted(list_data):
        print(items)
    return


def get_dict_info ( dict_info ):
    for info in dict_info.items():
        print(type(info))
    return

def get_dict_info_tuples ( dict_info ):
    for k,v in dict_info.items():
        print("{} {}".format(k,v))
    for v in dict_info.values():
        print("{} just values".format(v))
    return

def get_dict_sorted( )


def main():
    #tuples
    dt_tuples = (0,1)
    dt_dictionary= { "name": "foo", "last_name": "foo_last"}
    dt_list = [0,1,2,3,4,5,6,7,8]
    dt_tuples1 = ("hello","hello_1")
    numbers = ["one", "two","three","four"]
    print(dt_tuples[-1])
    print(add_together([(2,3),(4,6),(3,2)]))
    user_1 = Spotify_user("hola",'tests@tests.com', True)
    user_2 = Spotify_user('foo2','tests2@tests.com', False)
    print(user_1.name)
    print(user_2.name)
    user_1.isPremium()
    user_2.isPremium()
    print(type(dt_tuples1))
    print(type(dt_dictionary))
    print(type(dt_list))
    print(type(numbers))
    get_list_info(numbers)
    get_dict_info(dt_dictionary)
    get_dict_info_tuples(dt_dictionary)
    get_list_reversed(dt_list)
    get_list_sorted(dt_list)

if __name__ == "__main__":
    main()



