#!/usr/bin/env python3

#Generate Python default directory layout for new projects

import os
import re
import argparse

standard_files = ['setup.cfg','setup.py','README.md','requirements.txt']


def get_local_folder() -> str :
    folder_name = os.getcwd().split('/')
    folder_name = folder_name[(len(folder_name))-1]
    return folder_name

def create_layout():
    #create directories
    path = os.getcwd()
    standard_dirs= ['docs']
    standard_dirs.append(get_local_folder())
    for i in standard_dirs:
        if not os.path.isdir(i):
            os.mkdir(i)
            if i == get_local_folder():
                local_file = path+'/'+i+'/'+'__init__.py'
                with open( local_file,'w') as fp:
                    pass
    #create files
    for i in standard_files:
        local_file = path+'/'+i
        if not os.path.isfile(local_file):
            with open( local_file,'w') as fp:
                pass
    print(os.listdir(path))

def main():
    # Run on project top level folder 
    create_layout()

if __name__=="__main__":
    main()




