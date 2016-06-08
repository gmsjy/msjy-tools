#!/bin/python

import time

stat_file = '/proc/stat'

with open(stat_file, 'rb') as file:
    first_contents = file.read()

time.sleep(60)

with open(stat_file, 'rb') as file:
    second_contents = file.read()

print first_contents

print second_contents

