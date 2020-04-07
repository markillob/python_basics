#!/usr/bin/python

import re
import sys 

def get_palindromo( word_var : str ) -> str:
    counter = len(word_var) -1 
    word_var_decrease = word_var
    for k in range(counter):
        if word_var[k] == word_var_decrease[counter]:
            counter -=1
        else:
            return print("no es palindromo")
    return print(" {} is palindromo".format(word_var))

def is_anagrama( word_var : str , second_word_var : str) -> str:
    if len(word_var) == len(second_word_var):
        for k in range(len(word_var)):
            if second_word_var[k] not in word_var:
                print ("not anagrama")
        return print("anagrama")
    else:
        return print("no es un anagrama")

def get_needle_haystack( haystack : str, needle : str ) -> str:
    needle_limit = len(needle) -1
    needle_index = 0
    index_list = []
    for k in range(len(haystack)):
        if haystack[k] == needle[needle_index] and needle_index< needle_limit:
            index_list.append (k)
            if len(index_list) > 1:
                if index_list[needle_index] - index_list[needle_index-1] > 1 :
                    return(print("-1"))
            needle_index+=1
    return print (index_list[0])

def main():
    #word_var = input()
    #word_var = "anitalavalatina"
    #get_palindromo(word_var)
    #is_anagrama("bb", "alomph")
    get_needle_haystack("aamacoa","maco")
    get_needle_haystack("helloll","ll")
    get_needle_haystack("marxxxco","marco")
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
# O(N) tiempo lineal 
# Olog(N) logaritmico
# O(NlogN) linearitmico 
# O(n^2)  cuadratico 
# O(n^3) 
# O(n^4) 