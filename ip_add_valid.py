#!/usr/bin/env python3

def ip_add_check(ip_list):
    
    for ip in ip_list:
        octet_list = ip.split('.')
        

        # Check if the IP address has four octets

        if len(octet_list) == 4:

            # Check if the IP address is in valid unicast range (Loopback (127.X.X.X.), APIPA (169.254.X.X), Broadcast (224.X.X.X) addresses will not be accepted)

            if (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and  (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):

                print('{} is a valid host IP address'.format(ip))
                continue

            else:

                print('*{} is invalid host IP address. Please check the text file entry for the IP addresses'.format(ip))

        else:
            print('*{} is in invalid IP address format. Please check the text file entry for the IP addresses.'.format(ip))

        sys.exit()
