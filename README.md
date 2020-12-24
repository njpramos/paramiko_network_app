# Reading/Writing Cisco IOS Device Configuration using Paramiko in Linux OS

This app uses Paramiko via Python3 scripting and implements SSH protocol to read, extract and write Cisco IOS configuration commands to Cisco Switches (IOSV-L2 image) in GNS3.

### Network Topology

![network topology](/network_topology.png)

#### IP Address Scheme

This based on 10.10.10.0/24 subnet

* R1: 10.10.10.1 
* SW1: 10.10.10.2
* SW2: 10.10.10.3
* SW3: 10.10.10.4
* PC1: 10.10.10.100
* PC2: 10.10.10.200

_Note: The devices were pre-configured with base configurations and SSH enabled_

### Usage

```
root@PC1~/network_app# python3 main.py

```

The program will excecute the following tasks sequentially:

* Read the IP address of the hosts in the `ip_address.txt` text file.
* Check the validity of the host IP addresses using the `ip_add_check()` function in the `ip_add_valid` module.
* Verify the connectivity of each hosts from the PC1 using `icmp_request()` function in the `ip_reach` module.
* Connect to each device using SSH and create threads for simultaneous sending of configuration commands.
* The `create_threading()` function will run and pass the arguments to `ssh_connect()` function to allow SSH connection and send the IOS commands listed in `config.txt`

### Sample Output

![sample output](/sample_output.png)

_Note: After the all IP addresses were checked and validated. The program will prompt the user to enter the SSH username and password to push the configuration commands to each devices_
