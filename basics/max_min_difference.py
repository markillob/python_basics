
def sort_list_get_max_number(local_list):
    max_number = local_list[0]
    for i in local_list:
        if max_number <= i:
            max_number = i
    return max_number
def sort_list_get_min_number(local_list):
    min_number = local_list[0]
    for i in local_list:
        if min_number >= i:
            min_number = i
    return min_number

def difference_max_min(list):
    difference = sort_list_get_max_number(list) - sort_list_get_min_number(list)
    return difference

number_sequence = [1,45,6,7]
print(difference_max_min(number_sequence))










