#!/usr/bin/env python3

import argparse

'''
Enter Your Code Here
'''
def get_ram_usage():
    # read '/proc/meminfo', use split to extract usage in kiB 
    # express as MiB or GiB according to user preference  
    # 

    f = open('/proc/meminfo', 'r')
    sys_stats = f.readlines()
    rt_raw = sys_stats[0].split()
    rt = int(rt_raw[1])
    ra_raw = sys_stats[2].split()
    ra = int(ra_raw[1])
    f.close()

    den = 1048576

    total = rt / den
    available = ra / den
    used = (rt -ra) / den
    
    return total, available, used

def display_ram_usage():
    total, available, used = get_ram_usage()
    print(f'System Memory\nTotal {total:.2f} GiB\nAvailable {available:.2f} GiB\nUsed {used:.2f} GiB')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "RAM monitor")

    parser.add_argument('--ram', action='store_true')

    args = parser.parse_args()

    if args.ram:
        get_ram_usage()


     






