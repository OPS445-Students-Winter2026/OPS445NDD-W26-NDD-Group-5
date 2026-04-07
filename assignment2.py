#!/usr/bin/env python3

import argparse

'''
Enter Your Code Here
'''
def get_ram_usage():
    # Use readlines to process '/proc/meminfo', split to isolate desired field  

    f = open('/proc/meminfo', 'r')
    sys_stats = f.readlines()
    rt_raw = sys_stats[0].split() # line 1 of meminfo - Total Memory - split to remove excess whitespace 
    rt = int(rt_raw[1])           # extract second item (memory as kiB) in list
    ra_raw = sys_stats[2].split() # line 3 of meminfo - Available Memory - split to remove excess whitespace
    ra = int(ra_raw[1])           # as above, extract memory as kiB
    f.close()   

    # Convert kiB to GiB

    den = 1048576 # kiB in 1 GiB

    total = rt / den
    available = ra / den
    used = (rt -ra) / den
    percent = used / total * 100
    
    return total, available, used, percent

def display_ram_usage():
    # Call get_ram_usage and process the output for display using an f-string

    total, available, used, percent = get_ram_usage()
    print(f'System Memory\nTotal: {total:.2f} GiB\nAvailable: {available:.2f} GiB\nUsed: {used:.2f} GiB\nPercent Used: {percent:.1f}\%')

# Main Block - incl. argparse implementation for RAM function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "RAM monitor")

    parser.add_argument('--ram', action='store_true')

    args = parser.parse_args()

    if args.ram:
        display_ram_usage()


     






