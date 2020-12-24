#!/usr/bin/env python3

import threading
import getpass

# Creating threads for each SSH connection

def create_threading(ip_list, function):

    username = input('Enter your SSH username: ' )
    password = getpass.getpass()
    threads = []

    for ip in ip_list:
        th = threading.Thread(target = function, args = (ip, username, password))
        th.start()
        threads.append(th)
        #print(th)

        for th in threads:
            th.join()

