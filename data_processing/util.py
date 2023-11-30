from datetime import datetime, timedelta

def dt_2_timestamp(dt_str):
    nofrag, frag = dt_str.split('.')
    nofrag_dt = datetime.strptime(nofrag, "%Y-%m-%d %H:%M:%S")
    dt = nofrag_dt.replace(microsecond=int(frag))
    return datetime.timestamp(dt)

#delta dt in ms
def next_step_time(curr_ts, dt):
    return curr_ts + dt*0.001

def within_boundary(val, upper, lower):
    if(val<=upper and val>=lower):
        return True
    return False

def get_time_windows(dt, start, end):
    windows = []
    while(start < end):
        next = next_step_time(start, dt)
        windows.append((start, next))
        start = next
    return windows

#windows = get_time_windows(50, 1651626252.115359, 1651627763.617304)
#print(windows)

#ts = dt_2_timestamp('2022-05-04 06:22:09.209862')
ts = dt_2_timestamp('2022-05-03 19:04:12.115359')
print(ts)
print(next_step_time(ts, 50))
print(next_step_time(ts, 50) - ts)
'''
def testing():
    
    e_st = 1650711213.151942
    e_nd = 1650712793.552691
    p_st = 1650660812.185402
    p_nd = 1650662394.129645
    """
    e_st = 1651625928.491925
    e_nd = 1651628929.15746
    p_st = 1651575527.897823
    p_nd = 1651578529.609670
    """
    print(e_st - p_st)
    print(e_nd - p_nd)

testing()
'''