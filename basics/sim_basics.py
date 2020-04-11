#!/usr/bin/python

import re
import sys 

def get_palindromo( word_var : str ) -> str: # O(N) 
    n = len(word_var) -1 
    for k in range(int(n/2)):
        if word_var[k] == word_var[n]:
            n -=1
        else:
            return print("no es palindromo")
    return print(" {} is palindromo".format(word_var))

def is_anagrama( word_var : str , second_word_var : str) -> str:
    # aaz , zza
    word_count_one = [0]*256
    word_count_two = [0]*256
    n = len(word_var) 
    if len(word_var) == len(second_word_var): 
        for ch in word_var: # a , a , z # O(N)
            word_count_one[ord(ch)] += 1 # ord('a') = 97, word_count_one[97] = 2, ord('z') = 122,  word_count_one[122] =1
        for ch in second_word_var: # z ,z,a O(N)
            word_count_two[ord(ch)] +=1 #ord('z') =122, word_count_two[122] = 2, ord('a') = 97 word_count_one[97] = 1
        for k in range(256):   #O(1) + o(n) + O(N) = O(N + N +1) = O(2N + 1) = O(N)
            if word_count_one[k] != word_count_two[k]:
                return False
        return True    

#aaz zza --->   [97, 97, 122]

#"mississippi"
#"issip"
# ord('a')

def get_needle_haystack( haystack : str, needle : str ) -> str:
    if needle:
        if len(haystack) > len(needle):
            needle_index = 0
            size_needle = len(needle) -1
            index_list = []
            for index_hs in range(len(haystack)):
                if haystack[index_hs] == needle[needle_index]:
                    int_hay_in = index_hs
                    for index in range(len(needle)):
                        if haystack[int_hay_in] == needle[index]:
                            index_list.append(int_hay_in) 
                            int_hay_in +=1 
                            if index == size_needle:
                                return index_list[0]
                        else:
                            index_list = [] 
                            needle_index = 0
            return(-1)
        elif haystack == needle:
            return 0
        else:
            return(-1)
    else:
        return 0



def main():
    #word_var = input()
    #word_var = "anitalavalatina"
    #get_palindromo(word_var)
    #is_anagrama("bb", "alomph")
    print(get_needle_haystack("sissippi","issipi"))
    #print(get_needle_haystack("aavbbbaaaaabb","bb"))
    #print(get_needle_haystack("aaaab","b"))
    #print(get_needle_haystack("hello","ll"))
    #print(get_needle_haystack("marxxxco","marco"))
    #get_indexpairs("thestoryofleetcodeandme",["story","fleet","leetcode"])

#def get_indexpairs( full_string : str , list_of_words: list) -> list:
#    list_temp = list_of_words
#    for i in range(len(list_temp)):
#         
#   return print(list_temp[0])

if __name__ =="__main__":
    main()


#arrays
#
#
# 
#td_list = [1,1,5,0,0,2,1]
# k=0
# output[0,0] 
#set =[1,2,3]
#Input: haystack = "hello", needle = "ll"
#Output: 2
#https://leetcode.com/problems/implement-strstr/
#palindromo oso --> oso -> True
#anagrama   atotonilco -- colitonato ->
#histograma de caracteres
#https://leetcode.com/problems/index-pairs-of-a-string/
#
# A-Z, 0-9 
# ASCII
#string_search 
# clases y objectos
# 
# invariant 
# slicing window
# timepo constante 0(1)
# Olog(N) logaritmico
# O(N) tiempo lineal
# O(NlogN) linearitmico 
# O(n^2)  cuadratico 
# O(n^3) 
# O(n^4) 