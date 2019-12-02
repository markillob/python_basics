import sys
mesage_one = "Hola"
message_two = "Mundo"
#Print a variable without spaces
print("Hola %s" % message_two)
#print multuple variables annotations and return values
def hello_message( mesage_one: str, message_two: str) -> str :
    return print("Primer %s %s " %( mesage_one , message_two ))

hello_message(mesage_one,message_two)

#debug message %r raw format for debugging
def debug_variable_message( part1 : str , part2 : str) -> str:
    whole_message = "This is again %s %s" % ( part1 , part2)
    return print("And again %r" % whole_message)

debug_variable_message(mesage_one, message_two)