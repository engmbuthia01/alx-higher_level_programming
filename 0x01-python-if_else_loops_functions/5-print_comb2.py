#!/usr/bin/python3
for num in range(0, 99, 2):
    print("{:d}".format(num), end='\n' if num == 99 else ",")
