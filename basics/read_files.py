from sys import argv
import re 
script_name , input_file , ip_address_search = argv
def print_all(file_name) :
    print (file_name.read())

def rewind(file_name) :
    file_name.seek(0)
    return

def print_a_line(line_count : int , file_name):
    print (line_count, file_name.readline(), end=""),
    return

def search_ip_address( ip_address_search : str, file_name ) -> str :
    line_with_ip = ''
    for line in file_name:
        if re.search(ip_address_search, line ):
            line_with_ip += line
            break
    return line_with_ip

'''
print("Lets print the the whole file")
current_file = open(input_file)
count = 0
for i in current_file:
    print_a_line(i,current_file)
'''
current_file = open(input_file)
rewind(current_file)
#print(search_ip_address(ip_address_search,current_file),end="")
line_with_ip = search_ip_address(ip_address_search, current_file)
print(len(line_with_ip))
for i in line_with_ip:
    print(i,end="")
current_file.close()
