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

### Argparse
- **argparse documentation:**
  https://docs.python.org/3/library/argparse.html#name-or-flags
  - parser = argparse.ArgumentParser()
  - parser.add_argument() for adding flags
  - args = parser.parse_args() to read user input
