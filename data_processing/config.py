
protocols = ['icmp', 'arp', 'enip', 'cip_req', 'cip_res', 
            'tcp_A', 'tcp_FPA', 'tcp_S', 'tcp_FA', 'tcp_R', 
            'tcp_SA', 'tcp_PA', 'tcp_NOT_TCP']

ICMP = 0
ARP = 1
ENIP = 2
CIP_REQ = 3 
CIP_RES = 4 
TCP_A = 5
TCP_FPA = 6
TCP_S = 7
TCP_FA = 8 
TCP_R = 9 
TCP_SA = 10
TCP_PA = 11
UNKNOWN = 12

ONE_STEP = 1000 # in milliseconds
#[001, 152, 025, 050]
CATEGORY = ['d_0_l_0', 'd_2750_l_50', 'd_2500_l_5', 'd_1750_l_15']

#conf = [{'file': 'data/001_PLC1-eth0.csv', 'exp_start': 1650711213.151942, 'exp_end': 1650712793.552691, 'trigger_start': 1650711213.151942, 'trigger_end': 1650712793.552691, 'sync_val': 50400.96654009819, 'category': 'd_0_l_0'},
#        {'file': 'data/152_PLC1-eth0.csv', 'exp_start': 1651625928.491925, 'exp_end': 1651628929.15746, 'trigger_start': 1651626252.115359, 'trigger_end': 1651627763.617304, 'sync_val': 50400.59410190582,  'category': 'd_2750_l_50'},
#         {'file': 'data/025_PLC1-eth0.csv', 'exp_start': 2022-05-04 06:22:09.209862, 'exp_end': 2022-05-04 07:11:37.804865, 'trigger_start': 2022-05-04 06:27:19.511678, 'trigger_end': 2022-05-04 06:52:36.745530, 'sync_val': 50400.864438056946,  'category': 'd_2500_l_5'}]

# 'file': 'data/025_PLC1-eth0.csv', 'exp_start': 1651666929.209862, 'exp_end': 1651669897.804865, 'trigger_start': 1651667239.511678, 'trigger_end': 1651668756.74553, 'sync_val': 50400.864438056946,  'category': 'd_0_l_0'
# 'file': 'data/050_PLC1-eth0.csv', 'exp_start': 1651797666.051147, 'exp_end': 1651801046.57232, 'trigger_start': 1651798053.333506, 'trigger_end': 1651799777.621263, 'sync_val': 50401.22172689438,  'category': 'd_0_l_0'
conf = [{'file': 'data/050_PLC1-eth0.csv', 'exp_start': 1651797666.051147, 'exp_end': 1651801046.57232, 'trigger_start': 1651798053.333506, 'trigger_end': 1651799777.621263, 'sync_val': 50401.22172689438,  'category': 'd_1750_l_15'}]