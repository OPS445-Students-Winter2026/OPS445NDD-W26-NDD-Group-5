#!/usr/bin/env python3

import argparse

'''
Enter Your Code Here
'''
class RAM:
    def __init__(self,total=0,available=0,used=0):
        self.total = total_ram
        self.available = available_ram
        self.used = used_ram

    def __repr__(self):
        return f'Total System Memory: {self.total} \nAvailable System Memory: {self.available} \nSystem Memory In Use: {self.used}'

    def __str__(self):
         return f'Total System Memory: {self.total} \nAvailable System Memory: {self.available} \nSystem Memory In Use: {self.used}'
    def get_ram_usage(den):
        # read '/proc/meminfo', use split to extract usage in kiB 
        # express as MiB or GiB according to user preference  
        # 

        f = open('/proc/meminfo', 'r')
        sys_stats = f.readlines()
        rt_raw = sys_stats[0].split()
        rt = float(rt_raw[1])
        ra_raw = sys_stats[2].split()
        ra = float(ra_raw[1])
        f.close()

        if den == G:
            den == 1048576
        elif den == M:
            den == 1024
        else:
            return('Invalid unit. Please specify \'G\' for Gigabytes or \'M\' for Megabytes')
            exit(1)
        self.total = rt * den
        self.available = ra * den
        self.used = (rt -ra) * den


     






