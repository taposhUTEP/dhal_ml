import csv
import util

file = 'data/050_PLC1-eth0.csv'

truth_file = file.replace('.', '_ground_truth.')

trigger_loop_st = 648
trigger_loop_end = 792

exp_st = ''
exp_end = ''
trigger_st = ''
trigger_end = ''

with open(truth_file) as f:
        # Skips the heading Using next() method 
        heading = next(f)  
        reader = csv.reader(f)
        rows = list(reader)
        exp_st = rows[0][1]
        exp_end = rows[-1][1]
        trigger_st = rows[trigger_loop_st][1]
        trigger_end = rows[trigger_loop_end][1]
        #print(rows[248])
packet_capture_st = 0
with open(file) as f:
        # Skips the heading Using next() method 
        heading = next(f)  
        reader = csv.reader(f)
        for row in reader:
                #print(row)
                packet_capture_st = float(row[1])
                break
'''
print(f"Exp st {util.dt_2_timestamp(exp_st)}")
print(f"Exp end {util.dt_2_timestamp(exp_end)}")
print(f"tr st {util.dt_2_timestamp(trigger_st)}")
print(f"tr end {util.dt_2_timestamp(trigger_end)}")
print(f"Capture time {packet_capture_st}")
print(f"sync {util.dt_2_timestamp(exp_st) - packet_capture_st}")
'''
print(f"""'file': '{file}', 'exp_start': {util.dt_2_timestamp(exp_st)}, 'exp_end': {util.dt_2_timestamp(exp_end)}, 'trigger_start': {util.dt_2_timestamp(trigger_st)}, 'trigger_end': {util.dt_2_timestamp(trigger_end)}, 'sync_val': {util.dt_2_timestamp(exp_st) - packet_capture_st},  'category': 'd_0_l_0'""")

