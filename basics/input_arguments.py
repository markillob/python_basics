from sys import argv
def validate_3_arguments() -> bool:
    if len(argv) < 3 or len(argv) > 3:
        print("I need just 3 arguments")
    else:
        scrip_name, name, age = argv
        print ("1 argument %s , 2nd argument %s" % (name, age )) 
        return True
    return False 

script, filename = argv 
txt_file = open(filename)
print( "Here is your filename %s" % filename )
print (txt_file.read())
txt_file.close()
'''
print ("Type the file name again: ")
file_again = input()
txt_file_again = open(file_again)
print("\n")
print(txt_file_again.read())
txt_file_again.close()
'''
