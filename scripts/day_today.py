#!/Users/mbarrera/scripts3/bin/python
import os
import subprocess
import shutil
from pprint import pprint

def get_working_directory() -> str:
    my_cwd = os.getcwd()
    return my_cwd

print(get_working_directory())
