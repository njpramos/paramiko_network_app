#!/usr/bin/env python3

import paramiko
import os.path
import threading
import time
import sys
import re
import getpass

#Establishing SSH connection to the hosts

def ssh_connect(ip, username, password):

    with open('config.txt') as f:
        configs = f.readlines()

    try:

        # Logging into the host
        session = paramiko.SSHClient()

        # FOR TESTING PURPOSE: This allows auto-accepting of unknown host jeys
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device using the username and password
        #for ip in ip_list:
        session.connect(ip.rstrip('\n'), username = username, password = password)

            # Start the connection to the host switch or router
        connection = session.invoke_shell()

            # Send commands to the host
        connection.send('en\n')
        connection.send('terminal length 0\n')

        with open('config.txt') as f:
            configs = f.readlines()

        for line in configs:
            connection.send(line + '\n')
            time.sleep(1)

        #connection.send('end\n')
        #connection.send('sh vlan br\n')
        #time.sleep(1)

	#Checking command output for IOS syntax error
        output = connection.recv(65535)

        if re.search(b'% Invalid input', output):
            print("There was at least one IOS syntax error on host {} :".format(ip))
        else:
            print("The host {} has been properly configured.".format(ip))

        # Print out the output of command sent to the device
        #print(str(output))

        # Closing the connection
        session.close()

    except paramiko.AuthenticationException:
         print("Invalid username or password.")
    except paramiko.SSHException:
        print("SSH connection error. Please make sure that the SSH was enabled in the device")
