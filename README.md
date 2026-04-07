# <term> <year> Assignment 2

## Project Name:
RAM and Storage Monitor
## Description:
a python tool that takes a snapshot of RAM and disk storage usage on a linux machine

## Output:
- percentage of RAM used
- Percentage of Disk space used/free/total

## Research Notes

### Hard Drive Storage
- **os.statvfs() / fstatvfs documentation:**
  https://man7.org/linux/man-pages/man2/fstatvfs.2.html
  - f_bfree = Number of free blocks
  - f_bsize = Filesystem block size
  - f_frsize = Fragment size

- **How to use statvfs to get total and free filesystem size:**
  https://unix.stackexchange.com/questions/672113/using-statvfs-to-get-total-and-free-filesystem-size
  - To get total filesystem size: f_blocks * f_frsize
  - f_blocks = total number of blocks on the drive
  - f_frsize = size of one block in bytes
  - f_bfree = number of blocks that are free

- **Converting bytes to GB:**
  https://www.sharepointdiary.com/2022/02/convert-between-bytes-kb-mb-gb-tb-in-powershell.html
  - 1 Byte = 1 / 1024^3 GB
  - 1024 ** 3 in Python = 1,073,741,824 bytes = 1 GB
  ### RAM Usage:
  ## Consulted but not used:
  https://docs.python.org/3/library/subprocess.html#subprocess.run
  https://docs.python.org/3/library/resource.html#resource.RLIMIT_NICE
  https://www.howtogeek.com/659529/how-to-check-memory-usage-from-the-linux-terminal/

  ** documentation for psutil: **  
  https://psutil.readthedocs.io/latest/api.html#memor
 - psutil itself was not used in any form, as it is a third-party module
 -the documentation was consulted for methodology, as this module contains a similar function
 -psutil uses  /proc/meminfo for system memory stats
 - get_ram_usage function reads memory statistics from /proc/meminfo using readlines, lines 1 and 3    being of particular interest: MemTotal and MemAvailable
 - the split method is used to split the above lines into three substrings, the second of which is a numerical value in kB 
- Total - Available = Used
- Used/Total x 100 = Percent
- 1024 x 1024 = 1048576  kB in 1 GiB

-display_ram_usage function takes in the Total, Available, Used and Percentage values from get_ram_usage
-uses print function to output a formatted string   
  
### Argparse
- **argparse documentation:**
  https://docs.python.org/3/library/argparse.html#name-or-flags
  - parser = argparse.ArgumentParser()
  - parser.add_argument() for adding flags
  - args = parser.parse_args() to read user input
