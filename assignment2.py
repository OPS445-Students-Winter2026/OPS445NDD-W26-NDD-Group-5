#!/usr/bin/env python3

import argparse
import os

'''
Enter Your Code Here
'''
def get_disk_usage():
#Get disk stats from main drive
#os.statvfs will help give the details of the drive
    stats = os.statvfs('/')

# calculate total, used and free space
    total = stats.f_frsize * stats.f_blocks
    free = stats.f_frsize * stats.f_bfree
    used = total - free

# calculate percentage
    percent = (used / total) * 100

    return total, used, free, percent

def display_disk():
#Get information from get_disk_usage
    total, used, free, percent = get_disk_usage()

#print the results, converting bytes to GB
    print("hardrive usage")
    print(f"total: {total / (1024 ** 3):.2f} GB")
    print(f"used: {used / (1024 ** 3):.2f} GB")
    print(f"free: {free / (1024 ** 3):.2f} GB")
    print(f"percentage used: {percent:.1f} %")

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
    print(f'System Memory\nTotal: {total:.2f} GiB\nAvailable: {available:.2f} GiB\nUsed: {used:.2f} GiB\nPercent Used: {percent:.1f}%')

if __name__ == '__main__':
#creating the phraser
    parser = argparse.ArgumentParser()

#added the flag --disk 
    parser.add_argument('--disk', action='store_true')

    parser.add_argument('--ram', action='store_true')


#runs the parser and places the extracted data in a argparse object
    args = parser.parse_args()

#runs the function if --disk was used  
    if args.disk:
        display_disk()

    if args.ram:
        display_ram_usage()