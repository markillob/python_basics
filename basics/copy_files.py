from sys import argv
from os.path import exists
script_name, source_file, destination_file = argv
def copy_two_txt_files( file_one: str , file_two : str ) -> str:
    print("Copy from %s file  to %s file" % ( source_file, destination_file))
    source_file_data = open(source_file,'r')
    raw_data = source_file_data.read()
    print("The following data will be transfered")
    print(source_file_data.read())
    print("Does the destination file exist ? %r" % exists(destination_file))
    destination_file_data = open(destination_file,'w')
    destination_file_data.write(raw_data)
    source_file_data.close()
    destination_file_data.close()
    final_file_data = open(destination_file)
    print(final_file_data.read())
    final_file_data.close()
    return 

copy_two_txt_files(source_file, destination_file)
