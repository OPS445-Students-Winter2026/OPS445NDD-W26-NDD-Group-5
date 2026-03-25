#!/usr/bin/env python3

import argparse

'''
Enter Your Code Here
'''
def get_disk_usage():
#Get disk stats from main drive
#os.statvfs will help give the details of the drive
    stats = os.statvfs('/')

# calculate total, used and free space

# calculate percentage
    percent = (used / total) * 100

def display_disk():
#Get information from get_disk_usage

#print the results, converting bytes to GB
    print("hardrive usage")