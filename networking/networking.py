#!/bin/bash
import paramiko 
import re
import time

def send_cmd(conn, command):
    conn.send(command +"\n")
    time.sleep(3.0)
    return conn

def get_output(conn):
    return conn.recv(65535).decode("utf-8")

def main():
    host_dict = {"devwr1" : " show ip int brief | e una", "devwr2" : " show ip int brief | e una"}
    
    for hostname, dict_commands in host_dict.items():
        conn_params = paramiko.SSHClient()
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn_params.connect( hostname = hostname, username = "mbarrera", password = "1keyes", look_for_keys=False,allow_agent=False,)
        conn = conn_params.invoke_shell()
        time.sleep(3.0)
        print(f"Logged in to { get_output(conn).strip()} successfully")
        commands = ["terminal length 0", "show version | include Software,",dict_commands ]
        concat_output = ""
        for command in commands:
            send_cmd(conn,command)
            concat_output += get_output(conn)
        conn.close()
        print(f"Writing {hostname}, facts to file ")
        with open(f"{hostname}_facts.txt", "w") as handle:
            handle.write(concat_output)
        print(concat_output)

if __name__=="__main__":
    main()
#user admin:admin
# 10.100.24.202
#breakpoint()
# step | s 
# n or e
#c  run the lopp until another breakpoint is found 
#locals, will show all local variables
#PDB to explore python in a deeper level
