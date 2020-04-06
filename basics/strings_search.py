#!/usr/bin/python

def get_longest_substring ( full_string : str):
    counter = 0
    counter_temp = 0
    anchor_str_temp = ""
    i = 0
    anchor_str = ""
    if full_string == "" :
        return print("empty")
    while i < (len(full_string)-1): #7
        if full_string[i+1] != full_string[i] and full_string[i] not in anchor_str:
            anchor_str = anchor_str + (full_string[i])
            counter +=1
        elif i > 1 and i < (len(full_string)-2) and full_string[i] not in anchor_str:
            anchor_str_temp = anchor_str #ab
            anchor_str = ""
            counter_temp = counter # 2
            counter = 0
            i -=1
        elif i == 1  and full_string[i + 1] == full_string[i]:
            anchor_str = full_string[i]
        i +=1
    if full_string[i] not in anchor_str:
        anchor_str = anchor_str + (full_string[i])
        counter +=1
    elif full_string[i] not in anchor_str_temp:
        anchor_str_temp = anchor_str_temp + full_string[i]
        counter_temp +=1
    if counter_temp > counter:
        print( anchor_str_temp,counter_temp)
    else:
        print(anchor_str,counter)
    return 


def get_longest_substring_one ( full_string : str):
    counter = 0
    counter_temp = 0
    anchor_str_temp = ""
    i = 0
    anchor_str = ""
    while i < (len(full_string)-1): #7
        if  full_string[i+1] > len(str): 
            if full_string[i] not in anchor_str:
                anchor_str = anchor_str + (full_string[i])
                counter +=1
            elif full_string[i] not in anchor_str_temp:
                anchor_str_temp = anchor_str_temp + full_string[i]
                counter_temp +=1
        if fuull_string[i+1] != full_string[i] and full_string[i] not in anchor_str:
            anchor_str = anchor_str + (full_string[i])
            counter +=1
        elif i > 1 and i < (len(full_string)-2) and full_string[i] not in anchor_str:
            anchor_str_temp = anchor_str #ab
            anchor_str = ""
            counter_temp = counter # 2
            counter = 0
            i -=1
        elif i == 1  and full_string[i + 1] == full_string[i]:
            anchor_str = full_string[i]
        i +=1
    
    if counter_temp > counter:
        print( anchor_str_temp,counter_temp)
    else:
        print(anchor_str,counter)
    return 

def get_list_sum_numbers ( full_list : list):
    
    return list_temporar

def main ():
    get_longest_substring("dbdadb")

if __name__ =="__main__":
    main()
