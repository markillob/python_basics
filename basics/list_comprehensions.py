#decorators 
#closures
#first class functions
def square(x):
    return x *x 
def cube(z):
    return z * z * z
def my_map(func,my_list):
    result = []
    for i in my_list:
        result.append(func(i))
    return(result)

print(square(5))
f = square
print(f(5))
print(my_map(square,[1,2,3,4,5]))

#higher order function 
#closures
#closures
#codepath.io 



#
print('hola')
nums = [1,2,3,4,5]
abcs = ['a','b','c','d','e']
my_list = []
my_list = [ n*n for n in nums]
my_list = [ n*n for n in nums]
#double for loop
my_list = [ n for n in nums if n%2 == 0]
my_list = [(letter,num)for letter in 'abcd' for num in range(len('abcd'))]
print(my_list)
my_dict = {}
for num,abc in zip(nums,abcs):
    my_dict[num] = abc
print(my_dict)
my_dict = { num: abc for num,abc in zip(nums,abcs)}
print(my_dict)
my_set = set() 
set_nums = [1,2,3,4,5,1,2,3,4,5,5,3,4]
my_set = { n for n in set_nums}
print(my_set)
#generator Expressions 
my_gen = ( n *  n for  n in nums)
for i in my_gen:
    print(i)
