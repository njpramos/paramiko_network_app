#!/usr/bin/env python3

def ip_file_open():
    ip_address_list = []
    # Opening the text file containing the IP addresses of the hosts
    with open('ip_address.txt') as f:
        ip_address = f.read().split()

    for ip in ip_address:
        ip_address_list.append(ip)
   
    return ip_address_list
