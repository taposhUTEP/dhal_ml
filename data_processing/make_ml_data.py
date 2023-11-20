from config import *
import util
import csv

headers = protocols.copy()
headers.append('Y')
empty_row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in conf:
    input_f = x['file']
    out_f = input_f.replace('.csv', '_ml.csv')
    start_t = float(x['trigger_start']) - float(x['sync_val'])
    end_t = float(x['trigger_end']) - float(x['sync_val'])

    #next_boundary = start_t + ONE_STEP

    rows = [headers]
    time_windows = util.get_time_windows(ONE_STEP, start_t, end_t)
    #print(start_t)
    input_data = []
    with open(input_f) as f:
        # Skips the heading Using next() method 
        heading = next(f)  
        reader = csv.reader(f)
        for r in reader:
            input_data.append(r)
    count = 0
    for (start, end) in time_windows:
        #print(f"{start} - {end} - {end-start}")
        #continue
        row = empty_row.copy()
        row.append(CATEGORY.index(x['category']))
        for data_row in input_data:
            """
            print(f"{start} - {float(data_row[1])} - {end}")
            if float(data_row[1]) < start:
                continue
            if float(data_row[1]) > end:
                break
            """
            #print(data_row[1])
            #print(f"{start} - {float(data_row[1])} - {end}")
            #break
            if(util.within_boundary(float(data_row[1]), end, start)):
                indx = protocols.index(data_row[2])
                if data_row[2] == 'tcp_R':
                    print(data_row)
                print(f"{data_row} -- {indx}")
                row[indx] += 1
            #print(f"{start} - {float(data_row[1])} - {end}")
        rows.append(row)
        #print(rows)
        #if count == 20:
        #    break
        #count += 1
    with open(out_f, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)