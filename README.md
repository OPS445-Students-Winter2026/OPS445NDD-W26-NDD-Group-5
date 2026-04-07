# <term> <year> Assignment 2

## Project Name:
RAM and Storage Monitor
## Description:
a python tool that takes a snapshot of RAM and disk storage usage on a linux machine

## Input:

The get_ram_usage function reads memory statistics from /proc/meminfo using readlines, along with the split method to isolate the relevant fields: MemTotal and MemAvailable.
These values are then used to calculate the value of Used which is in turn used to calculate Used percentage of Total.
In their original form, these values are presented in kB, so the Total, Available and Used values are then divided by 1048576 (the number of kB in 1 GiB). 

The display_ram_usage function takes in the Total, Available, Used and Percentage values from get_ram_usage and plugs these values into an f-string for display using the print function. 

## Output:
- Total RAM/Available RAM/RAM in Use/Percentage of Total RAM used
- Percentage of Disk space used/free/total

## Resources Consulted:

  ## RAM Usage:
  https://docs.python.org/3/library/subprocess.html#subprocess.run
  https://docs.python.org/3/library/resource.html#resource.RLIMIT_NICE
  https://www.w3schools.com/python/python_ref_modules.asp
  https://www.w3schools.com/python/ref_module_argparse.asp
  https://psutil.readthedocs.io/latest/api.html#memory

  ## Disk Usage:
