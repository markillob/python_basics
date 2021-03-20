
#!/usr/bin/env python3
#
# Day by Day 
# 
#
#Given a string s, find the length of the longest substring without repeating characters.

def longest_substring ( cadena : str ) -> str :
    if len(cadena) == 0:
        return 0
    cont = 1
    temp_substring = ""
    substring = ""
    for i in range(len(cadena)-1):
        if cadena[cont-1]!= cadena[cont] and cadena[i] not in temp_substring and cont <= len(cadena):
            temp_substring = temp_substring + (cadena[i])
            cont += 1
        elif len(temp_substring) >= len(substring) and cont <= len(cadena):
                substring = temp_substring
                temp_substring =  cadena[cont -1]
                cont +=1
    if len(temp_substring)> len(substring):
        if cadena[-1] not in temp_substring:
            temp_substring = temp_substring + cadena[-1]
            return len(temp_substring)
        else:
            return len(temp_substring)
    else:
        if cadena[-1] not in substring:
            substring = substring + cadena[-1]
            return len(substring)
        else:
            return len(substring)

def main():
    print(longest_substring("abcabcdb"),"#4")
    print(longest_substring("hola"),"#4")
    print(longest_substring("bbbbb"),"#1")
    print(longest_substring("pwwkew"),"#3")
    print(longest_substring("asdgsetgaadef"),"")
    print(longest_substring("aab"),"#2")
    print(longest_substring("abcabcbb"),"#3")
    print(longest_substring("xzaxog"),"#4")


if __name__ == "__main__":
	main()


