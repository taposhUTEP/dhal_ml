from scapy.all import *
from datetime import datetime
import binascii
import cip

packets = rdpcap('../network_anomalies/output_001/PLC1-eth0.pcap')


def get_packet_layers(packet):
    counter = 0
    while True:
        layer = packet.getlayer(counter)
        if layer is None:
            break

        yield layer
        counter += 1


count = 0
prev_time = 0.0
for packet in packets:
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
    prev_time = packet.time
    #print(datetime.fromtimestamp(float(prev_time)).isoformat())
    #print((raw(packet)))
    print(f"taposh {count}")
    packet.show()
    if count == 100:
        break