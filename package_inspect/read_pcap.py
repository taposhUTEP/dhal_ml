from scapy.all import *
import cip
from datetime import datetime
import binascii
import packet_type
import csv

#input_files = ['../network_anomalies/output_001/PLC1-eth0.pcap',
#               '../network_anomalies/output_152/PLC1-eth0.pcap']
input_files = ['../network_anomalies/output_025/PLC1-eth0.pcap',
               '../network_anomalies/output_050/PLC1-eth0.pcap']
output_files = []
for in_f in input_files:
    out_f = in_f.replace('pcap', 'csv')
    packets = rdpcap(in_f)
    with open(out_f, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        rows = [['id', 'time_stamp', 'protocol']]
        id = 0
        for packet in packets:
            rows.append([id, packet.time, packet_type.get_packet_type(packet)])
            id += 1
        writer.writerows(rows)



"""
count = 0
prev_time = 0.0
pack_set = set()
for packet in packets:
    #packet_type.check_pckt(packet)
    tcp_type = packet_type.get_tcp_type(packet)
    pack_set.add(tcp_type)
    continue
    #print(type(packet))
    #packet.show()
    #if packet.haslayer(ARP):
    #    print('ARP')
    #layer = get_packet_layers(packet)
    #print(layer)
    #eth_pkt = packet.payload
    #proto_field = eth_pkt.get_field('proto')
    #proto_field.i2s[pkt.proto]
    #print(proto_field)
    #print(proto_field.i2s[packet.proto])
    #layers = packet.payload.layers()
    #print(type(layers[0]))
    count += 1
    #print(packet.fields)
    #print(packet.summary())
    if prev_time == 0.0:
        prev_time = packet.time
        continue
    #print((packet.time - prev_time) * 1000)
    print(f"taposh {count} - {(packet.time - prev_time) * 1000}")
    prev_time = packet.time
    #print(datetime.fromtimestamp(float(prev_time)).isoformat())
    #print((raw(packet)))
    #print(f"taposh {count} - ")
    #packet.show()
    #if count == 100:
    #    break
print(pack_set)
"""