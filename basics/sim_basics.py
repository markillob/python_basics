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

# aaa a, 
# 0,haystack[0]=m,needle[0] i  = ,# 1,haystack[1]=i,needle[0] i,< 4 [i] # 2,haystack[2]=s,needle[1] s,<= 4 index_neddle[1] 2 -1 =1, index_neddle[1,2]
## 3,haystack[3]=s,needle[2]=s 2 <= 4,index_neddle [1,2] 3 -2 = 1 ,index_neddle = [1,2,3] 5 ==3,
# 4,haystack[4]=i,needle[3]=i, 3 <=4  ,n =4 - 3 = 1 , index_neddle = [1,2,3,4] 5 ==4 Faslse, wc 4 in_pr = 4
# 5,haystack[5]=s,needle[4]=p,2 4 <= 4, wc = 0  index_neddle  = [] , n = ind_need[nc]
# 6,haystack[4]=i,needle[0]=i, wc = 0 index_neddle  = []
# 7,haystack[7]=O,needle[4]=O, 4<=4 , 7 - 6 ==1 index_neddle  = [3,4,5,6,7] < 4
# 8,haystack[8]=z,needle[4]=O, index_neddle  = [3,4,5,6,7] < 4

def get_needle_haystack( haystack : str, needle : str ) -> str:
    if needle or len(haystack) < len(needle):
        if haystack == needle:
            return 0
        else:
            needle_length = len(needle) - 1
            index_neddle = []
            word_count_needle = 0
            index_needle_previous = 0
            for n in range(len(haystack)):
                print(n)
                if haystack[n] == needle[word_count_needle] and word_count_needle <= needle_length: 
                    if index_neddle:
                        if n - index_neddle[word_count_needle -1] == 1:
                            index_neddle.append(n)
                            word_count_needle+=1
                            index_needle_previous = n
                            #print(index_needle_previous,"s")
                            if len(index_neddle) == len(needle):
                                return index_neddle[0]
                        else:
                            index_neddle = []
                    else:
                        index_neddle.append(n)
                        if needle_length == word_count_needle:
                            return 0
                        else:
                            word_count_needle+=1
                else:
                    word_count_needle = 0
                    index_neddle = []
                    n = index_needle_previous
                    #print(n)
            return -1
    else:
        return 0



def main():
    #word_var = input()
    #word_var = "anitalavalatina"
    #get_palindromo(word_var)
    #is_anagrama("bb", "alomph")
    print(get_needle_haystack("mississippi","issip"))
    #get_needle_haystack("aamacoa","")
    #get_needle_haystack("helloll","ll")
    #get_needle_haystack("marxxxco","marco")
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