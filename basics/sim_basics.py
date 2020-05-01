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
    if needle: #si existe
        if len(haystack) > len(needle): # si needed es mayor que haystack
            ni = []
            n_start = needle[0]
            hs_length = len(haystack)
            for index in range(len(haystack)):
                if haystack[index] == n_start:
                    ni.append(index)
            if len(ni) == 0:
                return -1
            elif len(needle) == 1:
                return ni[0]         
            else:
                needle_index = list(filter(lambda x: x + len(needle) <= hs_length,ni))
                result=[]
                for index in range(len(haystack)):
                    if index in needle_index:
                        local_index = index
                        for k in range(len(needle)):
                            if needle[k] == haystack[local_index]:
                                result.append(local_index)
                                local_index+=1
                        if len(result) == len(needle):
                            return result[0]
                        else:
                            result = []
                return -1
        elif haystack == needle:
            return 0
        else:
            return -1
    else:
        return 0

    #1 <= text.length <= 100
    #1 <= words.length <= 20
    #1 <= words[i].length <= 50
    #Input: text = "ababa", words = ["aba","ab"]
    #Output: [[0,1],[0,2],[2,3],[2,4]]
    
def get_indexpairs( cadena : str, lista : list) -> tuple:
    list_length = []
    valid_index = []
    valid_words = []
    results = []
    for item in lista:
        if item in cadena:
            valid_words.append(item)
    for item in valid_words:
        for index in range(len(cadena)):
            if item[0] == cadena[index] and (index + len(item)) <= len(cadena):
                list_length.append(index)
        valid_index.append(list_length)
        list_length = []
    word_index = {}
    count = 0
    for words in valid_words:
        word_index[words] = valid_index[count]
        count+=1
    for k,v in word_index.items():
        local_list = []
        for index in v:
            local_list2=[]
            if cadena[index:len(k)+index] == k:
                for z in range(len(k)):
                    local_list2.append(z+index)
            if local_list2:
                local_list.append(local_list2)                    
        results.append(local_list)
    final_results=[]
    for items in results:
        for index in items:
            local_index = [index[0],index[len(index)-1]]
            final_results.append(local_index) 
    return sorted(final_results)        

def main():
    print(get_indexpairs("ababa",["aba","ab"]))
    print(get_indexpairs("baabaaa",["b","a","ba","bb","aa"]))
    print(get_indexpairs("thestoryofleetcodeandme",["story","fleet","leetcode"]))
    print(get_indexpairs("baababbabaababbbbbbb",["bba","aba","abb","aa","ba"])) 
    #[[0,1],[1,2],[2,4],[3,4],[4,6],[5,7],[6,7],[7,9],[8,9],[9,10],[10,12],[11,12],[12,14]]
    # #word_var = input()
    #word_var = "anitalavalatina"
    #get_palindromo(word_var)
    #is_anagrama("bb", "alomph")
    #print(get_needle_haystack("ississippi","issip"))
    #print(get_needle_haystack("aavbbbaaaaabb","bb"))
    #print(get_needle_haystack("aaaab","b"))
    #print(get_needle_haystack("mississipi","pi"))
    #print(get_needle_haystack("hello","ll"))
    #print(get_needle_haystack("marxxxco","marco"))
    #print(get_indexpairs("thestoryofleetcodeandme",["story","fleet","leetcode"]))

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