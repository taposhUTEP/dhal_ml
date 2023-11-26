import numpy as np
import pandas as pd

files = ['../data_processing/data/001_PLC1-eth0_ml.csv',
         '../data_processing/data/152_PLC1-eth0_ml.csv']

xl = []
yl = []
"""
for input_f in files:
    with open(input_f) as f:
        # Skips the heading Using next() method 
        heading = next(f)  
        reader = csv.reader(f)
        for r in reader:
            xl.append(r[:-2])
            yl.append(r[-1])
print(xl[0])
"""
def get_now():
    for input_f in files:
        data = pd.read_csv(input_f, dtype={'icmp': 'float64', 
                                        'arp': 'float64', 
                                        'enip': 'float64', 
                                        'cip_req': 'float64', 
                                        'cip_res': 'float64', 
                                        'tcp_A': 'float64', 
                                        'tcp_FPA': 'float64', 
                                        'tcp_S': 'float64', 
                                        'tcp_FA': 'float64', 
                                        'tcp_R': 'float64', 
                                        'tcp_SA': 'float64', 
                                        'tcp_PA': 'float64', 
                                        'tcp_NOT_TCP': 'float64',
                                        'Y': 'Int64'})
        for key, val in data.iterrows():
            xl.append(val[:-2])
            yl.append(val[-1])
    X = np.array(xl)
    Y = np.array(yl)
    return (X, Y)
