import logging

logging.basicConfig(filename='example.log', level=logging.INFO )

def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with argements {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x,y):
    return x +y 

def sub(x,y):
    return x - y

def outer_func(msg):
    message = msg 
    def innner_func():
        print(message)
    return innner_func

add_logger = logger(add)
sub_loggger = logger(sub)

add_logger(6,3)
sub_loggger(9,4)

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hello_func()