#!/usr/bin/env python3

import argparse
import subprocess
'''
Enter Your Code Here
'''
def get_ram_usage():
  # use command 'free' to get snapshot of current state of ram usage in MiB
    free_parser = argparse.ArgumentParser()
    free_parser.add_argument("-M", help="Display RAM usage in mebibytes (MiB)")
    free_parser.add_argument("-G", help="Display RAM usage in gibibytes (GiB)")
    args = free_parser.parse_args()
    get_freem = subprocess.run(['free', '-m'], capture_output=True)
    get_freg = subprocess.run(['free', '-g'], capture_output=True)

    if args == "-M":
        get_freem

    elif args == '-G':
        get_freg


  # extract used, free, total from output
        # format with string slicing - which fields useful? 

def display_ram_usage():
  # using the data from above, format for display including used and free as percentage of total
        # fstring?
