
from scapy.all import TCP

# TCP package types {'A', 'FPA', 'S', 'FA', 'R', 'SA', 'PA'}
def is_tcp(packet):
    sub_str_1 = 'Ethernet'
    sub_str_2 = 'TCP'
    if (packet.find(sub_str_1) != -1) and (packet.find(sub_str_2) != -1):
        return True
    return False

def get_tcp_type(packet):
    if(is_tcp(packet.show(dump=True))):
        return str(packet[TCP].flags)
    return 'NOT_TCP'

def is_icmp(packet):
    sub_str = 'ICMPv6'
    if packet.find(sub_str) == -1:
        return False
    return True

def is_arp(packet):
    sub_str = 'ARP'
    if packet.find(sub_str) == -1:
        return False
    return True 

def is_enip(packet):
    sub_str_1 = 'ENIP_TCP'
    sub_str_2 = 'RegisterSession'
    if (packet.find(sub_str_1) != -1) and (packet.find(sub_str_2) != -1):
        return True
    return False

def is_cip_req(packet):
    sub_str_1 = 'ENIP_TCP'
    sub_str_2 = 'SendRRData'
    sub_str_3 = ' CIP '
    sub_str_4 = 'direction = request'
    if (packet.find(sub_str_1) != -1) and (packet.find(sub_str_2) != -1) \
        and (packet.find(sub_str_3) != -1) and (packet.find(sub_str_4) != -1):
        return True
    return False

def is_cip_res(packet):
    sub_str_1 = 'ENIP_TCP'
    sub_str_2 = 'SendRRData'
    sub_str_3 = ' CIP '
    sub_str_4 = 'direction = response'
    if (packet.find(sub_str_1) != -1) and (packet.find(sub_str_2) != -1) \
        and (packet.find(sub_str_3) != -1) and (packet.find(sub_str_4) != -1):
        return True
    return False

def check_pckt(packet):
    pt = ['icmp', 'arp', 'enip', 'cip_req', 'cip_res', 'tcp']
    ys = [False, False, False, False, False, False]
    packet_str = packet.show(dump=True)
    count = 0
    if(is_icmp(packet_str)):
        count += 1
        ys[0] = True
    if(is_arp(packet_str)):
        count += 1
        ys[1] = True
    if(is_enip(packet_str)):
        count += 1
        ys[2] = True
    if(is_cip_req(packet_str)):
        count += 1
        ys[3] = True
    if(is_cip_res(packet_str)):
        count += 1
        ys[4] = True
    #check for raw TCP only if no other proto found
    if(count==0 and is_tcp(packet_str)):
        count += 1
        ys[5] = True
    print(f"Count: {count}")
    for x in range(6):
        print(f"{pt[x]}: {ys[x]}")
    print("")


def get_packet_type(packet):
    #pt = ['icmp', 'arp', 'enip', 'cip_req', 'cip_res', 'tcp']
    packet_str = packet.show(dump=True)
    packet_type = 'na'
    count = 0
    if(is_icmp(packet_str)):
        count += 1
        packet_type = 'icmp'
    if(is_arp(packet_str)):
        count += 1
        packet_type = 'arp'
    if(is_enip(packet_str)):
        count += 1
        packet_type = 'enip'
    if(is_cip_req(packet_str)):
        count += 1
        packet_type = 'cip_req'
    if(is_cip_res(packet_str)):
        count += 1
        packet_type = 'cip_res'
    #check for raw TCP only if no other proto found
    if(count==0 and is_tcp(packet_str)):
        count += 1
        packet_type = 'tcp_' + get_tcp_type(packet)
    if count != 1:
        raise Exception("Ambiguous protocol. Couldn't determine protocol type")
    return packet_type