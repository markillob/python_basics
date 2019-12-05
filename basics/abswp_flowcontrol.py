def if_statement ( name : str ) -> str :
    first_name = 'Alice'
    if name == first_name :
        print("%s its is my name" % first_name)
    else:    
        print ('Hi %s' % name)
    return name

#if_statement("marco")

def elif_statement(name: str, age : int) -> str :
    local_age = 3000
    if name == 'Alice':
        print('alice')
    elif age < 12 :
        print ('local age %d' % local_age)
    elif age > 200 :
        print ('Alice is not an undead')
    else:
        print('Hola Mundo')
    return 'Hola'

#elif_statement('Marco',6 )

def get_name(name: str) -> str :
    print(name)
    #truty falsey value
    #empty strins is falsey or 0 value
    name_local = input()
    if name_local:
        print("Thanks for entering a name %s" % name_local)
    else:
        print("Try again")
        return 
    return print("Your name is %s" % name_local)

#get_name('Enter your name')

def while_statement( age : int) -> int:
    born_age = 0
    while born_age <= age:
        print("You age like %d" %born_age)
        born_age+=1
    return age

#while_statement(10)
def guess_your_name_3_times( name : str) -> str :
    count = 0
    while True:
        print ("What is your name")
        local_name = input()
        if name == local_name or count >= 3:
            break
        else:
            count+=1
            print("Keep trying")
    return
#break statement jump out of the lopp
#continue reevaluates the loop condition
#guess_your_name_3_times('Marco')

def get_personal_data() -> list:    
    age = input("whats your age? \t")
    weight = input("Whats your weight \t")
    name = input("Whats your name \t ")
    personal_data = [age, weight, name]
    return personal_data

def print_personal_data() -> str:
    personal_data = get_personal_data()
    return print( "Your name is %s and you are %s and your weight is %s" % (personal_data[2],personal_data[0],personal_data[1]))

print_personal_data()
