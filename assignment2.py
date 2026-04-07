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

if __name__ == '__main__':
#creating the phraser
    parser = argparse.ArgumentParser(description = "Harddrive monitor")
#added the flag --disk 
    parser.add_argument('--disk', action='store_true')

#runs the parser and places the extracted data in a argparse object
    args = parser.parse_args()

#runs the function if --disk was used  
    if args.disk:
        display_disk()

