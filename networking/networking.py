#!/bin/bash
import paramiko 
import re
import time

def send_cmd(conn, command):
    conn.send(command + "\n")
    time.sleep(1,0)
    return conn

def get_output(conn):
    return conn.recv(65535).decode("utf-8")


def main():
    conn_params = paramiko.SSHClient()
    conn_params.connect(
        hostname = "R1",
        username = "admin",
        password = "admin"
    )
    conn = conn.conn_params.invoke_shell()
    conn.send("show version\n")
    output = conn.recv(65535).decode("utf-8")

if __name__=="__main__":
    main()
#user admin:admin
# 10.100.24.202