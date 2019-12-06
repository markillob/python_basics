from sys import argv
def get_ip_adddres( ) :
    script_name, filename, ips_to_check , access_type = argv
    #python little_text_editor.py  test.txt  4 append| truncate
    print("We are going to erase the content of  %s" % filename)
    print("Hit enter to continue")
    input("?")
    print("Opennning a file")
    target_file = open(filename, access_type)
    print("Truncating the file...")
    target_file.truncate()
    #print("Provide the ip address to verify")
    total_ips = int(ips_to_check) 
    for i in range(total_ips):
        ip_address = input("IP: \t > ") 
        target_file.write(ip_address)
        if i == range(total_ips):
            break
        else:
            target_file.write("\n")
    target_file.close()
    read_file = open(filename)
    print(read_file.read())
    read_file.close()
    return filename
get_ip_adddres()

'''
ip_address_one = input("ip_address_one\t > ")
ip_address_two = input("ip_address_two \t> ")
ip_address_three = input("ip_address_three\t > ")
target_file.write(ip_address_one)
target_file.write("\n")
target_file.write(ip_address_two)
target_file.write("\n")
target_file.write(ip_address_three)
target_file.write("\n")
target_file.close()
'''
