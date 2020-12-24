#!/usr/bin/env python3

import sys
from ip_file_read import ip_file_open
from ip_add_valid import ip_add_check
from ip_reach import icmp_request
from ssh_connection import ssh_connect
from create_threads import create_threading

# Reading the IP addresses in the text file

ip_list = ip_file_open()

# Verifying the validity of each IP address of the hosts

try:
    print('Checking the host IP address validity...')
    ip_add_check(ip_list)

except KeyboardInterrupt:
    print('Process aborted by the user. Closing tthe program...')
    sys.exit()

# Checking the connectivity of each IP address of the hosts via ICMP request

try:
    print('Checking the host IP address connectivity...')
    icmp_request(ip_list)

except KeyboardIntrerrupt:
    print('Process aborted by the user. Closing tthe program...')
    sys.exit()

# Connect to each device using SSH and create threads for the simultaneous sending of commands

create_threading(ip_list, ssh_connect)
