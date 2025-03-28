# The first few functions are the helper function for the main subnet calculator fucntions so that it will be easier for me and for us to  understand

def ip_info(ip_address):  # This function does alot of thing actually finding teh class of the given ip, the type of address , and also the subnet mask

    parts = ip_address.split(".")  # Spliting teh ipaddress in to its 4 octates


    #This part is for the error handling if an idiot user does not know the proper format of ipv4 it will raise an error
    if len(parts) != 4:
        raise ValueError("Invalid IP address format. Please enter a valid IPv4 address.")

    for part in parts:
        if not part.isdigit():
            raise ValueError("Invalid IP address format. Please enter a valid IPv4 address.")
        if int(part) < 0 or int(part) > 255:
            raise ValueError("Invalid IP address range. Each part of the IP address should be between 0 and 255.")

    first = int(parts[0])  # the first octate in the ip address


# This portion will figure out the class and the subnet mask of the ip address by looking at its first octate
    if first < 127:
        ipclass = "Class A"
        subnet_mask = "8"
        typ = "Public"
    elif first <= 191:
        if "127.0.0.0" <= ip_address <= "127.255.255.255":     # This is a special exception which is know as the loopback range so i defined it
            ipclass = "N/A"
            subnet_mask = "8" # Gave it this special subnet mask just to uniqly use it in further code
            typ = "Loopback Address"
        else:
            ipclass = "Class B"
            subnet_mask = "16"
            typ = "Public"
    elif first <= 223:
        ipclass = "Class C"
        subnet_mask = "24"
        typ = "Public"
    elif first >= 224:    # this portion states the class d and class e addresses  which are not suitable for public use.
        ipclass = "Class D or Class E"
        subnet_mask = "0"# Gave it this special subnet mask just ot uniqly use it in further code
        typ = "Multicast or Experimental"
    
    if first == 10 or (first == 172 and 16 <= int(parts[1]) <= 31) or (first == 192 and parts[1] == "168"):   # If the user puts in the private range of ip addresses then my code will test that as well
        typ = "Private"
    
    return ipclass, subnet_mask, typ  # This return statement of this fucntion finally gives me out the ip class, the subnet mask adn the type of address.

# The next function is  to decide if user give in the subnet 
# if he did use that 
# if not then use the upper functon that we just created


def final_input(ip, subnet):
    if subnet is not None:
        if subnet not in [8,16,24]:   # Again this thign handle the error if user tries to escape the range of task this code can do..
            raise ValueError (" I understand the cruisity but this code is only limited to class ip ranges not the CIDR")
        else:
            
            sbnt = subnet
    else:
        sbnt = ip_info(ip)[1]
    return int(sbnt)    # Here we finally got our subnet mask to use further...


# This simpel function is one of the lengthy one as it calculate so many things.
# it calculates  network id, broadcast id , ip address range for that ip address and also the number of host in that network
def simple_one(ip, subnet):
    octat_list = ip.split(".")  # getting the list of octates
    # creatign the empty strings of stuff that we will fill out further
    network_id = ""   
    av_host_start = ""
    av_host_end = ""
    broadcast_id = ""
    if  subnet == 8:
        if octat_list[0]=="172":
            network_id+=""
            broadcast_id+=""
            av_host_start="172.0.0.0"
            av_host_start="172.255.255.255"
        else:
            network_id += octat_list[0] + ".0.0.0"
            broadcast_id += octat_list[0] + ".255.255.255"
            av_host_start = octat_list[0] + ".0.0.1"
            av_host_end = octat_list[0] + ".255.255.254"
    elif subnet == 0 or subnet == 1:
        network_id = "N/A"
        broadcast_id = "N/A"
    elif  subnet == 16:
        
        network_id += octat_list[0] + "." + octat_list[1] + ".0.0"
        broadcast_id += octat_list[0] + "." + octat_list[1] + ".255.255"
        av_host_start = octat_list[0] + "." + octat_list[1] + ".0.1"
        av_host_end = octat_list[0] + "." + octat_list[1] + ".255.254"
    elif  subnet == 24:
        network_id += octat_list[0] + "." + octat_list[1] + "." + octat_list[2] + ".0"
        broadcast_id += octat_list[0] + "." + octat_list[1] + "." + octat_list[2] + ".255"
        av_host_start = octat_list[0] + "." + octat_list[1] + "." + octat_list[2] + ".1"
        av_host_end = octat_list[0] + "." + octat_list[1] + "." + octat_list[2] + ".254"
    else:
        network_id = ""
        broadcast_id = ""

    av_range = av_host_start + " - " + av_host_end
    hosts= (2**(32-subnet))-2

    return (network_id, broadcast_id, av_range, hosts)

# Yess  i took help from the internet resource to figure this out..
# This function convert. the  / notation subnet in to the dotted one
def slash_to_subnet(cidr):
    subnet = "255." * (int(cidr) // 8) + "0." * ((32 - int(cidr)) // 8)
    return subnet.rstrip(".")


# THis is the main Boss fucntion which is using the all above fucntions to give out the final  rerutn statement

def subnet_calculator(ip, subnet=None):
    class_ip = ip_info(ip)[0]
    ip_type = ip_info(ip)[2]
    
    subnet_mask = final_input(ip, subnet)
    dotted_form= slash_to_subnet(subnet_mask)
   # Agian this code is limited for the only class range ip addresses so it wont consider the CIDR  yet.. 
    if subnet_mask == 8 or subnet_mask == 16 or subnet_mask == 24 or subnet_mask == 0 or subnet_mask == 1:
        network_id, broadcast_id, available, num_host = simple_one(ip, subnet_mask)
    
    return class_ip, subnet_mask, network_id, broadcast_id, ip_type, available,num_host, dotted_form

title= """
 ▄█     ▄███████▄      ███▄▄▄▄    ▄█  ███▄▄▄▄        ▄█    ▄████████ 
███    ███    ███      ███▀▀▀██▄ ███  ███▀▀▀██▄     ███   ███    ███ 
███▌   ███    ███      ███   ███ ███▌ ███   ███     ███   ███    ███ 
███▌   ███    ███      ███   ███ ███▌ ███   ███     ███   ███    ███ 
███▌ ▀█████████▀       ███   ███ ███▌ ███   ███     ███ ▀███████████ 
███    ███             ███   ███ ███  ███   ███     ███   ███    ███ 
███    ███             ███   ███ ███  ███   ███     ███   ███    ███ 
█▀    ▄████▀            ▀█   █▀  █▀    ▀█   █▀  █▄ ▄███   ███    █▀  
                                                ▀▀▀▀▀▀               
"""
print(title)
address= input("IPv4 ADDRESS :")
#subnet= input("Subnet")


class_ip, subnet_mask, network_id, broadcast_id, ip_type, available, num_host, dotted_form= subnet_calculator(address)


print("** IP Subnet Analysis Results for", address, "(", ip_type, ")**"
     )
print("  Class:              ", class_ip)
print("  Subnet Mask (CIDR): ", dotted_form, "/"+str(int(subnet_mask)))  # Enhanced CIDR notation
print("  Network ID:         ", network_id)
print("  Broadcast ID:       ", broadcast_id)
print("  Usable IP Range:    ", available)
print("  Usable Hosts:       ", num_host)

