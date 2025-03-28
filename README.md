# IP-NINJA
A simple Python tool for calculating and analyzing IPv4 subnets, providing details like network ID, broadcast ID, and usable IP range.
# IP Subnet Calculator

This Python script is designed to help users understand and calculate essential networking information about IPv4 addresses. It provides a comprehensive analysis of the given IP address, including its class, subnet mask, network ID, broadcast ID, usable IP range, and the number of available hosts. The script also handles the validation of the IP address format and checks for private or loopback IP ranges.

The goal of this tool is to make subnetting and IP address management easier, especially for network administrators, students, or anyone interested in learning more about networking concepts.

## Features

- **IPv4 Address Validation**: The script checks if the input IP address is valid and falls within the correct range for each octet (0-255).
- **IP Class Identification**: It automatically determines the class of the IP address (Class A, B, C, D, or E) based on the first octet of the IP address.
- **Subnet Mask Calculation**: The script calculates the default subnet mask based on the IP class and allows users to specify their own subnet mask.
- **Network and Broadcast ID Calculation**: It calculates the network ID and broadcast ID for a given IP address, helping you understand the structure of the network.
- **Usable IP Range**: The script provides the range of IP addresses that can be assigned to hosts in the given network, excluding network and broadcast addresses.
- **Number of Hosts**: It calculates how many hosts can be supported in the given network based on the subnet mask.
- **CIDR Notation Conversion**: The script can convert the CIDR subnet format into the corresponding dotted decimal subnet mask for easier understanding.

## How to Use

1. Clone the repository or download the Python script.
2. Open the script in your preferred Python environment.
3. Run the script and input an IPv4 address when prompted.
4. The script will output detailed information, including the IP class, subnet mask, network and broadcast IDs, usable IP range, and the number of hosts available in the network.

Example output:
IPv4 ADDRESS : 10.93.3.3
** IP Subnet Analysis Results for 10.93.3.3 ( Private )**
  Class:               Class A
  Subnet Mask (CIDR):  255.0.0.0 /8
  Network ID:          10.0.0.0
  Broadcast ID:        10.255.255.255
  Usable IP Range:     10.0.0.1 - 10.255.255.254
  Usable Hosts:        16777214

## License

No License - Feel free to use, modify, and share the code as needed. This project is open for collaboration and improvements.
