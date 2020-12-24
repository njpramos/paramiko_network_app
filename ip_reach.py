#!/usr/bin/env python3

import subprocess

def icmp_request(ip_list):
    for ip in ip_list:
        # Using the subprocess module, excute the ping command and supress any other output in the command line

        ping_reply = subprocess.call('ping %s -c 2' %(ip), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL, shell = True)
        #subprocess.check_output(["ping", "-c", "1", "127.0.0.1"])
        
        # Check if the hosts is reachable

        # print(ping_reply)

        if ping_reply == 0:
            print('* {} is reachable !!!!!'.format(ip))
            continue
        else:
            print('{} is not reachable. Check the connectivity and try again\n'.format(ip))
            sys.exit()
